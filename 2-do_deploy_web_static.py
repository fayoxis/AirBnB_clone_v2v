#!/usr/bin/python3
"""this archive to your web servers, using the function do_deploy"""
from fabric.api import env, run, put, local, cd
from contextlib import contextmanager
import os

env.hosts = ['18.209.224.119', '54.157.173.122']

@contextmanager
def source_code():
    """Context manager to create a temporary directory for the source code."""
    directory = run('mktemp -d --tmpdir=/tmp')
    try:
        yield directory
    finally:
        run(f'rm -rf {directory}')

def do_deploy(archive_path):
    """Distribute an archive to the web servers."""
    if not os.path.exists(archive_path):
        return False

    with source_code() as tmp_dir:
        # Upload the archive to the temporary directory
        archive_name = os.path.basename(archive_path)
        put(archive_path, f'{tmp_dir}/{archive_name}')

        # Extract the archive
        with cd(tmp_dir):
            run(f'tar -xzf {archive_name}')

        # Get the name of the extracted directory
        extracted_dir = run(f'ls {tmp_dir}').stdout.strip()

        # Create the release directory
        data_path = '/data/web_static/releases/'
        run(f'mkdir -p {data_path}')
        release_dir = f'{data_path}{extracted_dir}'

        # Move the extracted files to the release directory
        run(f'mv {tmp_dir}/{extracted_dir} {release_dir}')

        # Remove the current symbolic link, if it exists
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run(f'ln -s {release_dir} /data/web_static/current')

        return True

    return False
