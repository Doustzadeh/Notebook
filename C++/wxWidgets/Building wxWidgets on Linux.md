## Building wxWidgets from source

#### Downloading the last stable wxWidgets library

The last stable wxWidgets distribution can be found at the wxWidgets website (https://www.wxwidgets.org/downloads/).

Extract download file to "/home/$USER/wxWidgets-x.x.x" (e.g. "/home/$USER/wxWidgets-3.1.5") .



#### Prerequisites

Install all necessary build tools, including g++ and autotools. One easy way to do this on many distros is to install the 'build-essential' package, e.g. for Ubuntu.

```shell
sudo apt install build-essential
```

```shell
sudo apt install libgtk-3-dev
```



#### Building your own wxWidgets library

```shell
cd ~/wxWidgets-3.1.5
```

- ##### Compile static

```shell
mkdir gtk-build-release           # the name is not really relevant
cd gtk-build-release
../configure --disable-shared --disable-debug
make
```
```shell
mkdir gtk-build-debug             # the name is not really relevant
cd gtk-build-debug
../configure --disable-shared --enable-debug
make
```

- ##### Compile shared/dynamic

```shell
mkdir gtk-build-release           # the name is not really relevant
cd gtk-build-release
../configure --enable-shared --disable-debug
make
```
```shell
mkdir gtk-build-debug             # the name is not really relevant
cd gtk-build-debug
../configure --enable-shared --enable-debug
make
```



- --disable-shared : Builds static libs (ending *.a)
- --enable-shared : Builds dynamic libraries (ending *.so)
- --enable-monolithic : Makes a single library (normal for wxMSW, but unusual to need this on Linux)
- --enable-unicode : Makes a Unicode build (default set for newer than 2.9)
- --enable-debug : Enable the adding of debug symbols. The debug libraries are much bigger.
- --disable-debug : Disable the adding of debug symbols

