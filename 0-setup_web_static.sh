#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

sudo sh -c 'echo "Hello form TutTrue >_<" >/data/web_static/releases/test/index.html'

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

# add config file
sudo sh -c 'echo "
server {
    listen 80;
    add_header X_Served_by \$HOSTNAME;
    listen [::]:80 default_server;
    server_name 331327-web-01;
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}" > /etc/nginx/sites-available/default'

sudo service nginx restart
