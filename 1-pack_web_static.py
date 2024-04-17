#!/usr/bin/python3
"""A module for Fabric script that generates a .tgz archive."""
import os
from datetime import datetime
from fabric.api import task

@task
def archive_files():  
    """Archives the static files."""
    output_file = get_archive_filename()
    
    if not os.path.isdir("versions"):
        os.mkdir("versions")

    try:
        print(f"Packing web_static to {output_file}")  
        run(f"tar -czf {output_file} web_static")
        size = get_file_size(output_file)
        print(f"web_static packed: {output_file} -> {size} Bytes")
    except Exception:
        output_file = None
        
    return output_file
    
def get_archive_filename():
   now = datetime.now()
   filename = f"versions/web_static_{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}.tgz"
   return filename
   
def get_file_size(filename):
   return os.stat(filename).st_size
   
def run(command):
   local(command)
