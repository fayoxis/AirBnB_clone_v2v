#!/usr/bin/env bash
# Update packages and install Nginx
sudo apt-get update && sudo apt-get -y install nginx

# Allow Nginx through the firewall
sudo ufw allow 'Nginx HTTP'

# Create directories for web data
sudo mkdir -p /data/{web_static,web_static/releases,web_static/shared,web_static/releases/test}

# Create sample index.html file  
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Symlink current release 
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Change ownership of web files
sudo chown -R ubuntu:ubuntu /data/

# Configure Nginx for static files
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}'
/etc/nginx/sites-enabled/default

# Restart Nginx
sudo systemctl restart nginx
