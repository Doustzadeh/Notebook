## Building wxWidgets from the command line

#### Downloading the last stable wxWidgets library

The last stable wxWidgets distribution can be found at the wxWidgets website (https://www.wxwidgets.org/downloads/).

Unzip download file to "C:\wxWidgets-x.x.x" (e.g. "C:\wxWidgets-3.1.5") .



#### Building your own wxWidgets library

Before anything, add the bin directory of MinGW to the %PATH% variable. Now it is time to compile wxWidgets, open the command prompt and change to the wxWidgets directory:

```shell
cd C:\wxWidgets-x.x.x\build\msw
```

- ##### Builds static
```shell
mingw32-make -f makefile.gcc SHARED=0 MONOLITHIC=0 BUILD=release
```
```shell
mingw32-make -f makefile.gcc SHARED=0 MONOLITHIC=0 BUILD=debug
```

- ##### Builds dynamic

```shell
mingw32-make -f makefile.gcc SHARED=1 MONOLITHIC=1 BUILD=release
```
```shell
mingw32-make -f makefile.gcc SHARED=1 MONOLITHIC=1 BUILD=debug
```

- SHARED=0 : Builds static libraries

- SHARED=1 : Builds dynamic libraries
- MONOLITHIC=1 : Packages all libraries in a single file. (Note: do not combine this option with a static build.)
- UNICODE=1 : Builds wxWidgets with Unicode support. This is the default mode. Disable Unicode only if you really need to! That is not recommended.
- BUILD=debug
- BUILD=release

