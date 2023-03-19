[![PyPI Latest Release](https://img.shields.io/pypi/v/findent.svg)](https://pypi.org/project/findent/)
[![PyPi release](https://github.com/gnikit/findent-pypi/actions/workflows/main.yml/badge.svg)](https://github.com/gnikit/findent-pypi/actions/workflows/main.yml)

# findent: powerful Fortran formatter

![alt](https://raw.githubusercontent.com/gnikit/findent-pypi/main/doc/findent-demo.gif)

## What is it?

**findent** indents/beautifies/converts and can optionally generate the dependencies of Fortran sources.

## Features

- Supports Fortran-66 up to Fortran-2018
- Converts from Fixed Form to Free Form and vice-versa
- Honours `cpp` and `coco` preprocess statements
- Honours OpenMP conditionals
- Validated against all constructs in
  'Modern Fortran explained, Incorporating Fortran 2018, Metcalf e.a.'
- Supported platformrs: Unix and Windows
- High speed: 50K - 100K lines per second
- vim, gedit, emacs: findent optionally emits configuration files
  for these editors to use findent as a plugin.

## Installation

Normal installation using pip

```sh
pip install findent
```

## Supported platforms

| OS      | Architecture                            |
| ------- | --------------------------------------- |
| Linux   | x64, arm64, i686, aarch64, ppc64, s390x |
| MacOS   | x64, arm64                              |
| Windows | x64                                     |

## Examples

### Format file `in.f90` to `out.f90`

```sh
findent < in.f90 > out.f90
```

### Format with 4-space indentation and convert Fixed Form `in.f` to Free Form `out.f90`

```sh
findent -i4 -Rr < in.f > out.f90
```

### Format and refactor all files with `.f` extension in the current directory

```sh
wfindent -i4 -Rr *.f
```

### Generating Fortran source dependencies for use in Makefile

**findent** will generate a dependency list for:

- definitions and uses of modules and submodules
- `include`, `#include` and `??include` statements

In your Makefile add something similar to:

```Makefile
findent --makefdeps > makefdeps
chmod +x makefdeps

include deps
dep deps:
  ./makefdeps *.f90 > deps
```

The flag `--makefdeps` generates a script in the standard output.
Depending on your usecase the script might not suffice and you will need to write your own version.

## Editor incorporation

### (G) VIM users

Installation instructions:

```sh
findent --vim_help
```

Documentation:

`:help equalprg`

`:help indentexpr`

<!-- - vim/README -->
<!-- - and the comments in the files vim/findent.vim and vim/fortran.vim -->

### GEDIT users

Installation instructions:

```sh
findent --gedit_help
```

### EMACS users

Installation instructions:

```sh
findent --emacs_help
```
