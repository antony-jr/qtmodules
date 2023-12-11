#!/usr/bin/env bash

#TODO: Change the tag to latest once finished
QARCHIVE_VERSION=$(curl  "https://api.github.com/repos/antony-jr/QArchive/tags" | jq -r '.[0].name' | cut -c 2-)

###
### QArchive and LibArchive MSVC 2019 - Release x64
###
wget -O data.zip "https://github.com/antony-jr/QArchive/releases/download/prebuilt/windows-msvc-v14.2-qt-5.15.2-x64-Release.zip"
wget -O archive.zip "https://github.com/antony-jr/libarchive-windows-prebuilds/releases/download/continuous/libarchive-x64-windows.zip"

cp data.zip packages/in.antonyjr.QArchive.windows.x64.msvc2019/data/msvc2019_64/
cp archive.zip packages/in.antonyjr.libarchive.windows.x64.msvc2019/data/msvc2019_64/

pushd packages/in.antonyjr.QArchive.windows.x64.msvc2019/data/msvc2019_64/

unzip data.zip

rm -rf data.zip

mv QArchive/* .

rm -rf QArchive

popd

rm -rf data.zip

pushd packages/in.antonyjr.libarchive.windows.x64.msvc2019/data/msvc2019_64/

unzip archive.zip

rm -rf archive.zip

popd

rm -rf archive.zip
###
### ---
###

###
### QArchive and LibArchive MSVC 2015 - Release x64
wget -O data.zip "https://github.com/antony-jr/QArchive/releases/download/prebuilt/windows-msvc-v14-qt-5.15.2-x64-Release.zip"

#TODO: Build LibArchive for MSVC 2015
wget -O archive.zip "https://github.com/antony-jr/libarchive-windows-prebuilds/releases/download/continuous/libarchive-x64-windows.zip"

cp data.zip packages/in.antonyjr.QArchive.windows.x64.msvc2015/data/msvc2015_64/
cp archive.zip packages/in.antonyjr.libarchive.windows.x64.msvc2015/data/msvc2015_64/

pushd packages/in.antonyjr.QArchive.windows.x64.msvc2015/data/msvc2015_64/

unzip data.zip

rm -rf data.zip

mv QArchive/* .

rm -rf QArchive

popd

rm -rf data.zip

pushd packages/in.antonyjr.libarchive.windows.x64.msvc2015/data/msvc2015_64/

unzip archive.zip

rm -rf archive.zip

popd

rm -rf archive.zip

###
### ---
###
