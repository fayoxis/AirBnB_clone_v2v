#!/usr/bin/env bash
# Update package information
sudo apt-get update

# Install Nginx
sudo apt-get -y install nginx

# Allow Nginx HTTP traffic
sudo ufw allow 'Nginx HTTP'

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create index.html file with desired content
sudo bash -c 'cat > /data/web_static/releases/test/index.html << EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF'

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership of directories
sudo chown -R ubuntu:ubuntu /data/

# Add configuration for serving static files
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}'
/etc/nginx/sites-enabled/default

# Restart Nginx service
sudo service nginx restart
