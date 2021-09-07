## Building Boost from the command line

#### Downloading the last stable Boost library

The last stable Boost distribution can be found at the Boost website (https://www.boost.org/users/download/).

Unzip download file to "C:\boost_x_x_x" (e.g. "C:\boost_1_77_0") .

#### Building your own Boost library

Before anything, add the bin directory of MinGW to the %PATH% variable.

1. Open Command Prompt and navigate to:

```bash
cd C:\boost_x_x_x\tools\build
```
2. Run:

```bash
C:\boost_x_x_x\tools\build>bootstrap.bat gcc
```

3. Copy "b2.exe" from "C:\boost_x_x_x\tools\build" to "C:\boost_x_x_x"

4. Build 32-bit static:

```bash
cd C:\boost_x_x_x>
```
```bash
C:\boost_x_x_x>b2.exe --toolset=gcc architecture=x86 address-model=32 threading=multi variant=release link=static runtime-link=static --build-type=complete stage --stagedir=stage/x86
```
```bash
C:\boost_x_x_x>b2.exe --toolset=gcc architecture=x86 address-model=32 threading=multi variant=debug link=static runtime-link=static --build-type=complete stage --stagedir=stage/x86
```

5. Build 64-bit static:
```bash
C:\boost_x_x_x>b2.exe --toolset=gcc architecture=x86 address-model=64 threading=multi variant=release link=static runtime-link=static --build-type=complete stage --stagedir=stage/x64
```
```bash
C:\boost_x_x_x>b2.exe --toolset=gcc architecture=x86 address-model=64 threading=multi variant=debug link=static runtime-link=static --build-type=complete stage --stagedir=stage/x64
```

