#!/usr/bin/python3
import os
import shutil
from fabric.api import local, run, env

# Set the hosts and user for the remote servers
env.hosts = ['18.209.224.119', '54.157.173.122']
env.user = "ubuntu"

def clean_releases(keep_count=2):
    """Clean up old releases on both local and remote servers"""
    clean_local_releases(keep_count)
    clean_remote_releases(keep_count)

def clean_local_releases(keep_count):
    """Clean up old releases on the local machine"""
    versions_dir = "versions"
    if os.path.exists(versions_dir):
        local_releases = sorted(os.listdir(versions_dir), reverse=True)
        for release in local_releases[keep_count:]:
            release_path = os.path.join(versions_dir, release)
            shutil.rmtree(release_path)

def clean_remote_releases(keep_count):
    """Clean up old releases on the remote servers"""
    releases_path = "/data/web_static/releases"
    with cd(releases_path):
        remote_releases = sorted(run("ls -t").stdout.strip().split("\n"), reverse=True)
        for release in remote_releases[keep_count:]:
            run("rm -rf {}".format(os.path.join(releases_path, release)))
