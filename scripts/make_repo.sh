#!/usr/bin/env bash

./scripts/qifw-qt5.sh

# Update all XMLS
./scripts/update_xmls.py

# Include Qttools in PATH
PATH=$PATH:$PWD/qifw/bin

# Generate Qt5 Windows
mkdir -p repositories/qt5_15_2/windows

pushd source/qt5_15_2/windows

./make.sh

popd 

repogen -p source/qt5_15_2/windows/packages \
   	-i in.antonyjr.QArchive,in.antonyjr.QArchive.windows.x64.msvc2019,in.antonyjr.libarchive.windows.x64.msvc2019 \
	repositories/qt5_15_2/windows/


pushd source/qt5_15_2/windows

./clean.sh

popd


rm -rf qifw
