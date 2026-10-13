"""Minimal KiCad s-expression reader/writer used to generate the ERC/DRC test projects."""

import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Symbols reference footprints by the nickname the repository project uses;
# tools/pcm_package.py renames it to the PCM one for a release.
LOCAL_PREFIX = "LOCAL_"


class Q(str):
    """A quoted string token, kept distinct from bare atoms for round-tripping."""


def _tokenize(text):
    i, n = 0, len(text)
    while i < n:
        c = text[i]
        if c in "()":
            yield c
            i += 1
        elif c.isspace():
            i += 1
        elif c == '"':
            j, buf = i + 1, []
            while text[j] != '"':
                if text[j] == "\\":
                    buf.append({"n": "\n", "t": "\t"}.get(text[j + 1], text[j + 1]))
                    j += 2
                else:
                    buf.append(text[j])
                    j += 1
            yield Q("".join(buf))
            i = j + 1
        else:
            j = i
            while j < n and not text[j].isspace() and text[j] not in '()"':
                j += 1
            yield text[i:j]
            i = j


def parse(text):
    stack = [[]]
    for tok in _tokenize(text):
        if tok == "(" and not isinstance(tok, Q):
            stack.append([])
        elif tok == ")" and not isinstance(tok, Q):
            node = stack.pop()
            stack[-1].append(node)
        else:
            stack[-1].append(tok)
    return stack[0][0]


def load(path):
    with open(path, encoding="utf-8") as f:
        return parse(f.read())


def dump(node, indent=0):
    if isinstance(node, Q):
        return '"' + node.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'
    if not isinstance(node, list):
        return str(node)
    # Leading atoms stay on the opening line; everything after the first list
    # goes on its own line, preserving the original order.
    first_list = next((i for i, x in enumerate(node) if isinstance(x, list)), len(node))
    head = "(" + " ".join(dump(x) for x in node[:first_list])
    if first_list == len(node):
        return head + ")"
    pad = "\n" + "\t" * (indent + 1)
    body = "".join(pad + dump(x, indent + 1) for x in node[first_list:])
    return head + body + "\n" + "\t" * indent + ")"


def children(node, name):
    return [x for x in node if isinstance(x, list) and x and x[0] == name]


def child(node, name):
    found = children(node, name)
    return found[0] if found else None


def properties(node):
    return {p[1]: p for p in children(node, "property")}


def prop(node, name, default=None):
    p = properties(node).get(name)
    return p[2] if p else default


def symbol_libs():
    return sorted(glob.glob(os.path.join(ROOT, "symbols", "*.kicad_sym")))


def footprint_libs():
    return sorted(glob.glob(os.path.join(ROOT, "footprints", "*.pretty")))


def lib_name(path):
    base = os.path.basename(path)
    return re.sub(r"\.(kicad_sym|kicad_mod|pretty)$", "", base)


def footprint_files(lib_dir):
    return sorted(glob.glob(os.path.join(lib_dir, "*.kicad_mod")))


def symbol_units(sym):
    """Unit numbers drawn by a symbol (unit 0 means common to all units)."""
    units = set()
    for sub in children(sym, "symbol"):
        m = re.search(r"_(\d+)_(\d+)$", sub[1])
        if m and int(m.group(1)) > 0:
            units.add(int(m.group(1)))
    return sorted(units) or [1]


def flatten_symbol(sym, lib_symbols):
    """Resolve `extends` the way KiCad does when embedding a symbol into a schematic."""
    ext = child(sym, "extends")
    if not ext:
        return sym
    base = flatten_symbol(lib_symbols[ext[1]], lib_symbols)
    own = properties(sym)
    out = [sym[0], sym[1]]
    for item in base[2:]:
        if not isinstance(item, list):
            out.append(item)
        elif item[0] == "property" and item[1] in own:
            out.append(own.pop(item[1]))
        elif item[0] == "symbol":
            out.append([item[0], Q(re.sub(r"^.*(_\d+_\d+)$", sym[1] + r"\1", item[1]))] + item[2:])
        else:
            out.append(item)
    insert_at = max(i for i, x in enumerate(out) if isinstance(x, list) and x[0] == "property") + 1
    out[insert_at:insert_at] = list(own.values())
    return out


def lib_table(kind, entries):
    """Render a sym/fp lib table; entries are (nickname, uri) pairs."""
    lines = ["(%s_lib_table" % kind, "\t(version 7)"]
    for name, uri in entries:
        lines.append('\t(lib (name "%s")(type "KiCad")(uri "%s")(options "")(descr ""))' % (name, uri))
    lines.append(")")
    return "\n".join(lines) + "\n"


def project_lib_tables(out_dir):
    """Write lib tables mapping the local nicknames to this repository's libraries."""
    rel = os.path.relpath(ROOT, out_dir)
    sym = [
        (LOCAL_PREFIX + lib_name(p), "${KIPRJMOD}/%s/symbols/%s" % (rel, os.path.basename(p)))
        for p in symbol_libs()
    ]
    fp = [
        (LOCAL_PREFIX + lib_name(p), "${KIPRJMOD}/%s/footprints/%s" % (rel, os.path.basename(p)))
        for p in footprint_libs()
    ]
    with open(os.path.join(out_dir, "sym-lib-table"), "w") as f:
        f.write(lib_table("sym", sym))
    with open(os.path.join(out_dir, "fp-lib-table"), "w") as f:
        f.write(lib_table("fp", fp))
