#!/usr/bin/env bash

#TODO: Change the tag to latest once finished


wget -O data.zip "https://github.com/antony-jr/QArchive/releases/download/prebuilt/windows-msvc-qt-5.15.2-x64-Release.zip"
wget -O archive.zip "https://github.com/antony-jr/libarchive-windows-prebuilds/releases/download/continuous/libarchive-x64-windows.zip"

cp data.zip packages/in.antonyjr.QArchive.windows.x64.msvc2019/data/msvc2019_64/
cp archive.zip packages/in.antonyjr.libarchive.windows.x64.msvc2019/data/msvc2019_64/

pushd packages/in.antonyjr.QArchive.windows.x64.msvc2019/data/msvc2019_64/

unzip data.zip

rm -rf data.zip

mv QArchive/* .

rm -rf QArchive

popd

pushd packages/in.antonyjr.libarchive.windows.x64.msvc2019/data/msvc2019_64/

unzip archive.zip

rm -rf archive.zip

popd


rm -rf *.zip
