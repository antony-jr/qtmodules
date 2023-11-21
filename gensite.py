#!/usr/bin/env python3
import os
import datetime

INDEX_DIR = "repositories"

html_upper = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index of INDEX_OF</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        h1 {
            color: #000;
        }

        table {
            border-collapse: collapse;
            width: 100%;
            margin-top: 20px;
        }

        th, td {
            padding: 8px 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }

        th {
            background-color: #f2f2f2;
        }

        tr:hover {
            background-color: #f5f5f5;
        }
    </style>
</head>
<body>
    <h1>Index of INDEX_OF</h1>

    <table>
        <tr>
            <th>Name</th>
            <th>Last Modified</th>
            <th>Size</th>
        </tr>
'''

html_dir_entry = '''
        <tr>
            <td><a href="{}">{}/</a></td>
            <td>{}</td>
            <td>--</td>
        </tr> 
'''


html_file_entry = '''
        <tr>
            <td><a href="{}">{}</a></td>
            <td>{}</td>
            <td>{}</td>
        </tr> 
'''

html_lower = '''
    </table>
</body>
</html>
'''

def sizeof_fmt(num, suffix="B"):
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

def init_html(path, index):
    fp = open("{}/index.html".format(path), "wt")
    fp.write(html_upper.replace("INDEX_OF", index))
    fp.close()


def add_dir_html(path, root, dr):
    link = root + dr + "/"
    actual_path = "{}/{}/".format(path, dr)
    modified = os.path.getmtime(actual_path)
    mod_time = datetime.datetime.fromtimestamp(int(modified))

    fp = open("{}/index.html".format(path), "at")
    fp.write(html_dir_entry.format(link, dr, mod_time))
    fp.close()

def add_file_html(path, root, file):
    link = root + file
    actual_path = "{}/{}".format(path, file)
    modified = os.path.getmtime(actual_path)
    mod_time = datetime.datetime.fromtimestamp(int(modified))
    size = sizeof_fmt(os.path.getsize(actual_path))

    fp = open("{}/index.html".format(path), "at")
    fp.write(html_file_entry.format(link, file, mod_time, size))
    fp.close()

def finish_html(path):
    fp = open("{}/index.html".format(path), "at")
    fp.write(html_lower)
    fp.close()

for root, dirs, files in os.walk(INDEX_DIR):
    path = root
    root = root.removeprefix(INDEX_DIR) + "/"
    
    init_html(path, root)
    
    for dr in dirs:
        add_dir_html(path, root, dr)
    for file in files:
        add_file_html(path, root, file)

    finish_html(path)
