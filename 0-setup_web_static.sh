#!/usr/bin/env bash
# create and setup web servers for deployment
apt-get update
apt-get install nginx -y
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data/
sed -i "/^\tserver_name/ a\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current; \n\t}\n"  /etc/nginx/sites-available/default
service nginx start
