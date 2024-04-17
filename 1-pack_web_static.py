#!/usr/bin/python3
"""A module for Fabric script that generates a .tgz archive."""
import os
import tarfile
from datetime import datetime
from fabric.api import local, task

@task
def archive_files():
    """Archives the static files."""
    output_file = get_archive_filename()

    os.makedirs("versions", exist_ok=True)

    try:
        with tarfile.open(output_file, "w:gz") as tar:
            tar.add("web_static", arcname="web_static")

        size = os.path.getsize(output_file)
        print(f"web_static packed: {output_file} -> {size} Bytes")
    except Exception as e:
        print(f"An error occurred: {e}")
        output_file = None

    return output_file

def get_archive_filename():
    now = datetime.now()
    filename = f"versions/web_static_{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}.tgz"
    return filename

def run(command):
    local(command)
