#!/usr/bin/python3
"""this  will Create and distributes then archive to web servers"""
from fabric.api import local, run, put, env, cd
from fabric.context_managers import shell_env
import os
import datetime

env.hosts = ['18.209.224.119', '54.157.173.122']

def do_pack():
    """Generate a tgz archive from the web_static folder."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"web_static_{timestamp}.tgz"
    archive_path = os.path.join("versions", archive_name)

    with shell_env(CURRENT_DIR=os.getcwd()):
        if not os.path.exists("versions"):
            local("mkdir versions")
        local(f"tar -czf {archive_path} web_static")

    if os.path.exists(archive_path):
        return archive_path
    return None

def do_deploy(archive_path):
    """it Distribute and archive web servers."""
    if not os.path.exists(archive_path):
        return False

    archive_name = os.path.basename(archive_path)
    release_path = f"/data/web_static/releases/{archive_name.split('.')[0]}"

    try:
        put(archive_path, "/tmp/")
        run(f"mkdir -p {release_path}")
        with cd(release_path):
            run(f"tar -xzf /tmp/{archive_name}")
            run("rm -rf web_static")
            run("mv static web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -sf {release_path} /data/web_static/current")
        print(f"Deployment done on {env.host}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def deploy():
    """Create & distribute to web servers."""
    archive_path = do_pack()
    if not archive_path:
        return False

    deployed = True
    for host in env.hosts:
        env.host = host
        if not do_deploy(archive_path):
            deployed = False

    return deployed
