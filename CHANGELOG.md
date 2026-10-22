# Changelog

## [3.1.7](https://github.com/sivakov512/kicad-library/compare/v3.1.6...v3.1.7) (2026-10-22)


### Bug Fixes

* Omron B3FS-4000 symbols and footprints per plunger type ([bf77463](https://github.com/sivakov512/kicad-library/commit/bf77463245f0c6ead08b667d9e03668f20329ec7))

## [3.1.6](https://github.com/sivakov512/kicad-library/compare/v3.1.5...v3.1.6) (2026-10-22)


### Bug Fixes

* courtyards follow the part outline with KLC F5.3 clearance ([27bde47](https://github.com/sivakov512/kicad-library/commit/27bde4787dd5aeb5e145ba70e187c6a909023587))

## [3.1.5](https://github.com/sivakov512/kicad-library/compare/v3.1.4...v3.1.5) (2026-10-21)


### Bug Fixes

* courtyards cover pads and body with 0.25 mm clearance ([0a01f89](https://github.com/sivakov512/kicad-library/commit/0a01f8989a8adf472204925baab020d9df4c89ba))

## [3.1.4](https://github.com/sivakov512/kicad-library/compare/v3.1.3...v3.1.4) (2026-10-21)


### Bug Fixes

* B3FS-40xxP pad pairs are joined inside the switch ([10fc67b](https://github.com/sivakov512/kicad-library/commit/10fc67b9c0f08d888dedd4a5a90ce19e3b186896))

## [3.1.3](https://github.com/sivakov512/kicad-library/compare/v3.1.2...v3.1.3) (2026-10-21)


### Bug Fixes

* B3FS-40xxP pads paired per internal connection, not always closed ([6114770](https://github.com/sivakov512/kicad-library/commit/6114770c40329a6cb0662af9656153ceaa0947cc))

## [3.1.2](https://github.com/sivakov512/kicad-library/compare/v3.1.1...v3.1.2) (2026-10-21)


### Bug Fixes

* MAX17048G ALRT pin is open-drain, named per datasheet ([d3a0168](https://github.com/sivakov512/kicad-library/commit/d3a01681571a43c38c1d521ee964ebb9e4dd298d))

## [3.1.1](https://github.com/sivakov512/kicad-library/compare/v3.1.0...v3.1.1) (2026-10-13)


### Bug Fixes

* publish datasheets on GitHub Pages, linked by content hash ([cff02f6](https://github.com/sivakov512/kicad-library/commit/cff02f6dbb4eb95a6c6904ba7d1f998d02b31492))

## [3.1.0](https://github.com/sivakov512/kicad-library/compare/v3.0.0...v3.1.0) (2026-10-13)


### Features

* add 15 parts used in client projects with models and datasheets ([8ee6e73](https://github.com/sivakov512/kicad-library/commit/8ee6e73971c42e2677858bf105777d906852b165))

## [3.0.0](https://github.com/sivakov512/kicad-library/compare/v2.1.2...v3.0.0) (2026-10-13)


### ⚠ BREAKING CHANGES

* lowercase x for SIMCom footprint, Molex datasheet name
* listed pin stacks, 100mil pins, stock fields, A7672x GND
* drop unused CP_Radial D5/P1.5 and D16/P10 footprints
* KLJ-5020 land pattern and pads per datasheet
* rename symbols, footprints and datasheets per KLC
* bring symbols and footprints in line with KLC
* migrate all libraries to KiCad 10 format

### Bug Fixes

* bring symbols and footprints in line with KLC ([6072c72](https://github.com/sivakov512/kicad-library/commit/6072c725f3d93b9bc5928b503ca277937790f2d4))
* KLJ-5020 land pattern and pads per datasheet ([f4fb927](https://github.com/sivakov512/kicad-library/commit/f4fb92748aa864ad5f6f8708729b6f92099f82d1))
* listed pin stacks, 100mil pins, stock fields, A7672x GND ([d21d9d1](https://github.com/sivakov512/kicad-library/commit/d21d9d10bc049281f8d2eaa614fb0ca5d8aa9668))
* migrate all libraries to KiCad 10 format ([7ebd067](https://github.com/sivakov512/kicad-library/commit/7ebd067859d8d1978d92e3ec62b459818c4fee2c))
* replace wrong and missing 3D models, bake placement into STEP ([900b9f3](https://github.com/sivakov512/kicad-library/commit/900b9f3ce4ecfddeb52de18ca7612fd4a23b88dd))
* round non-pin-1 THT pads, KLC exception for Cvilux USB-C ([525a244](https://github.com/sivakov512/kicad-library/commit/525a2443855782195eda20c11be3fd881fdde7d2))


### Code Refactoring

* drop unused CP_Radial D5/P1.5 and D16/P10 footprints ([83d346a](https://github.com/sivakov512/kicad-library/commit/83d346a68ecd7a1ca611542ce499f6b6acac240b))
* lowercase x for SIMCom footprint, Molex datasheet name ([d7e347f](https://github.com/sivakov512/kicad-library/commit/d7e347fde274cb02c9ede95c26ed62b1188706f3))
* rename symbols, footprints and datasheets per KLC ([e671b88](https://github.com/sivakov512/kicad-library/commit/e671b88ae8bf9e0c68147373a267310245f8afe3))

## [2.1.2](https://github.com/sivakov512/kicad-library/compare/v2.1.1...v2.1.2) (2026-10-12)


### Bug Fixes

* pin datasheet links to the release tag in PCM packages ([1c2853b](https://github.com/sivakov512/kicad-library/commit/1c2853be4d187ce1b48bc0678ade4516d6960f41))

## [2.1.1](https://github.com/sivakov512/kicad-library/compare/v2.1.0...v2.1.1) (2026-10-01)


### Bug Fixes

* mark WaveShare_ESP32-C6-Zero power pins as bidirectional ([bcb569c](https://github.com/sivakov512/kicad-library/commit/bcb569c35790ede5b2799076737a393fd7bd45b1))

## [2.1.0](https://github.com/sivakov512/kicad-library/compare/v2.0.0...v2.1.0) (2026-05-10)


### Features

* A7672X/A7670X symbol, footprint, datasheet, 3d model ([16ec2bb](https://github.com/sivakov512/kicad-library/commit/16ec2bb8d9b94975df580dfbd7030d42988b2227))
* added datasheet for TE_OJ-SH-105HM_SPST relay ([62f06dc](https://github.com/sivakov512/kicad-library/commit/62f06dc60ce89252f69dc01246c687f1b3f9aa9d))
* BH-18650-A5BJ001-2D footprint and datasheet ([8e0c95d](https://github.com/sivakov512/kicad-library/commit/8e0c95db69a137e83a11b82320f94a2e5b7b9a89))
* DRV8316C symbol, footprint, datasheet, 3d model ([79721c2](https://github.com/sivakov512/kicad-library/commit/79721c22bb5ac0cf9d42e919fc77de3df274e9ac))
* KLJ-5020 footprint and datasheet ([6fca1ba](https://github.com/sivakov512/kicad-library/commit/6fca1ba8114e46c63fca72b15b899baea8c1f481))
* MAX17048 symbol, footprint, datasheet, 3d model ([3d69def](https://github.com/sivakov512/kicad-library/commit/3d69def99442a684d35b71835ec95ab0c70c1a6f))
* MMPC0402 footprint and datasheet ([f5487d3](https://github.com/sivakov512/kicad-library/commit/f5487d3da0d0626a2dcdd4f8500877f46768a01c))
* MOLEX_475532001 footprint, datasheet, 3d model ([eba6889](https://github.com/sivakov512/kicad-library/commit/eba68890f61b9ecb9057c8eee1640be9d2c63046))
* PJ-3126-5A footprint and datasheet ([868c2f9](https://github.com/sivakov512/kicad-library/commit/868c2f9a79d3ee0ba0d8feb9ad609e042d5ae573))
* SK6812-EC20 symbol, footprint, datasheet ([b094d22](https://github.com/sivakov512/kicad-library/commit/b094d22773402aa395469724b2470ca8f9215a19))
* TPS212x symbol, footprint, 3dmodel, datasheet ([1f0fe0d](https://github.com/sivakov512/kicad-library/commit/1f0fe0d5988d13665b691b5722d31a4a6bb5ea12))
* TPS56424x symbol ad datasheet ([246dd98](https://github.com/sivakov512/kicad-library/commit/246dd98a5fe2ed70ab40ff164ed75ed68abbce27))
* ZMPT101B symbol, footprint, datasheet ([ed343d9](https://github.com/sivakov512/kicad-library/commit/ed343d9a81b9d56fefc9ed90cf6aa9bfa3f4e4b9))


### Bug Fixes

* drop footprints for pinheaders and nettie ([fe5abb5](https://github.com/sivakov512/kicad-library/commit/fe5abb5e8dee1ea886d6a101c6d5f61893ee48d8))

## [2.0.0](https://github.com/sivakov512/kicad-library/compare/v1.5.0...v2.0.0) (2026-05-10)


### ⚠ BREAKING CHANGES

* restructure library to conform to KLC v3.0

### Features

* Add Quectel YC0010AA antenna footprint, 3d model and datasheet ([488c504](https://github.com/sivakov512/kicad-library/commit/488c504929ed61c1a45658c11ce38de63b9f2df1))
* Add Rohm BDXXKA5WF fixed regulator family ([ac27c7c](https://github.com/sivakov512/kicad-library/commit/ac27c7ceaf744c4510f24b1ae5a6fc0bfdd2aa4a))
* automatic releases ([291d61a](https://github.com/sivakov512/kicad-library/commit/291d61a46eeb1f4c21c2e6fa60063fbf9a5f1225))
* Cvilux CU3216SASBLR004-NH USB-C Receptacle footprint and datasheet ([8b6c870](https://github.com/sivakov512/kicad-library/commit/8b6c870bf7411b25819501f4252a07e6307e61c3))
* footprint for hybrid no name usb-c receptacle ([b5ffcaa](https://github.com/sivakov512/kicad-library/commit/b5ffcaab7ad96d41e73e187d46af671a1429e224))


### Code Refactoring

* restructure library to conform to KLC v3.0 ([74783ce](https://github.com/sivakov512/kicad-library/commit/74783ced278e6b3a8a71501cbcb9f27d40bde7cd))

## [1.5.0](https://github.com/sivakov512/kicad-library/compare/v1.4.0...v1.5.0) (2026-04-02)


### Features

* footprint for hybrid no name usb-c receptacle ([39a2cb9](https://github.com/sivakov512/kicad-library/commit/39a2cb96fb9b5454ee6d1675ec73d7ad36c9bb10))

## [1.4.0](https://github.com/sivakov512/kicad-library/compare/v1.3.0...v1.4.0) (2026-02-20)


### Features

* Add Rohm BDXXKA5WF fixed regulator family ([be41341](https://github.com/sivakov512/kicad-library/commit/be41341ac73d6ea3890dc7333feab7ab7dd3f7ca))

## [1.3.0](https://github.com/sivakov512/kicad-library/compare/v1.2.0...v1.3.0) (2026-02-19)


### Features

* Cvilux CU3216SASBLR004-NH USB-C Receptacle footprint and datasheet ([ffa2563](https://github.com/sivakov512/kicad-library/commit/ffa25637e98a2a9203a1ddffbbce5ce7b31f3776))

## [1.2.0](https://github.com/sivakov512/kicad-library/compare/v1.1.0...v1.2.0) (2026-02-19)


### Features

* Add Quectel YC0010AA antenna footprint, 3d model and datasheet ([ba895a3](https://github.com/sivakov512/kicad-library/commit/ba895a3e45716e3a765f42b6fad721a4fd76f5ec))

## [1.1.0](https://github.com/sivakov512/kicad-library/compare/1.0.23...v1.1.0) (2025-12-14)


### Features

* automatic releases ([8e25f44](https://github.com/sivakov512/kicad-library/commit/8e25f44ac70c4b7b9942ab078016746daab8a740))
