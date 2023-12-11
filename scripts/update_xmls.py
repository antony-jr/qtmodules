#!/usr/bin/env python3
import os
import requests
import json
import time
import xml.etree.ElementTree as ET
from pathlib import Path

# Helper Functions
def update_version_xml(file, version):
    rel_date=time.strftime("%Y-%m-%d")

    tree = ET.parse(file)
    root = tree.getroot()

    ver_tag = root.find('Version')
    ver_tag.text = version

    rel_tag = root.find('ReleaseDate')
    rel_tag.text = rel_date

    tree.write(file)

    # Prepend
    with open(file, 'r+') as f:
        line = '<?xml version="1.0" encoding="UTF-8"?>'
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

    # Append
    with open(file, 'a+') as f:
        f.write('\n')

def get_dirs_with_prefix(directory, prefix):
  dirs = []
  for entry in os.listdir(directory):
    if os.path.isdir(os.path.join(directory, entry)) and entry.startswith(prefix):
      dirs.append(entry)
  return dirs

def update_packages(pkgdir, prefix, version):
    pkgs = get_dirs_with_prefix(pkgdir, prefix)
    for pkg in pkgs:
        path = "{}/{}/meta/package.xml".format(pkgdir, pkg)
        print("[+] UPDATING: {}".format(path))
        update_version_xml(path, version)

# Default Values
QARCHIVE_VERSION="2.2.8"
LIBARCHIVE_VERSION="3.6.2"

print("Update XML, A Simple Script to Update Qt Package XML.")
print("Copyright (C) 2023-Present, D. Antony J.R <contact@antonyjr.in>.")
print()

# Check Directory
dirName = Path.cwd().parts[-1:][0]

if dirName != "qtmodules":
    print("Fatal: please run this script in root of the repo.")
    os._exit(-1)

# Get QArchive Latest Version
resp = requests.get("https://api.github.com/repos/antony-jr/QArchive/tags")
if resp.status_code != 200:
    print("Error({}): Cannot get QArchive Version.".format(resp.status_code))
    os._exit(-1)

d = json.loads(resp.content)
QARCHIVE_VERSION = d[0]['name'][1:]

print("QARCHIVE_VERSION = {}".format(QARCHIVE_VERSION))
print("LIBARCHIVE_VERSION = {}".format(LIBARCHIVE_VERSION))

# TODO:
# Update this as the repos grow

pkgdirs = [
        "source/qt5_15_2/windows",
]

for pkgdir in pkgdirs:
    update_packages(pkgdir + "/packages", "in.antonyjr.QArchive", QARCHIVE_VERSION)
    update_packages(pkgdir + "/packages", "in.antonyjr.libarchive", LIBARCHIVE_VERSION)

print("\nDone.")
