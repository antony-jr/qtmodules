#!/usr/bin/env bash

mkdir qifw
wget -O installer.bin "https://download.qt.io/official_releases/qt-installer-framework/4.5.2/QtInstallerFramework-linux-x64-4.5.2.run"

chmod +x installer.bin

ldd installer.bin

./installer.bin in -t "$PWD/qifw" --am -c --al

rm -rf installer.bin
