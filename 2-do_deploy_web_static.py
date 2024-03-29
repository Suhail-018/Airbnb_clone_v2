#!/usr/bin/python3
"""create a list of file from a archived files"""
from fabric.api import task, put, run, env, local, sudo
import os
from datetime import datetime

env.user = "ubuntu"
env.hosts = ['54.90.31.60', '100.25.151.235']


@task
def do_pack():

    """a pack web_static folder to archive"""
    try:
        cur_date = datetime.now().strftime('%Y%m%d%H%M%S')
        arch = f'web_static_{cur_date}.tgz'
        local('mkdir -p versions')
        local(f'tar -cvzf versions/{arch} web_static')
        return f'versions/{arch}'
    except Exception:
        return None


@task
def do_deploy(archive_path):

    """the fun willdistributes an archive to a or urweb servers"""
    file_name = archive_path.split('/')[-1].split('.')[0]
    if not os.path.exists(archive_path):
        return False

    put(archive_path, '/tmp/')
    sudo(f'mkdir -p /data/web_static/releases/{file_name}/')
    sudo(f'tar -xzf /tmp/{file_name}.tgz -C \
    /data/web_static/releases/{file_name}/')
    sudo(f'rm /tmp/{file_name}.tgz')
    sudo(f'mv /data/web_static/releases/{file_name}/web_static/* \
    /data/web_static/releases/{file_name}/')
    sudo(f'rm -rf /data/web_static/releases/{file_name}/web_static')
    sudo('rm -rf /data/web_static/current')
    sudo(f'ln -s /data/web_static/releases/{file_name}/ \
    /data/web_static/current')
    print('New version deployed!')
    return True
