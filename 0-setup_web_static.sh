#!/usr/bin/env bash
# create and setup web servers for deployment
apt-get update
apt-get install nginx -y
mkdir /data/
mkdir /data/web_static/
mkdir /data/web_static/releases/
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/
printf %s "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > /data/web_static/releases/test/index.html
ln -s /data/web_static/current /data/web_static/releases/test/
chown -R ubuntu:ubuntu /data/
