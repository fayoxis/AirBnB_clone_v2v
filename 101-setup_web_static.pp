# Puppet for setup
$nginx_conf = @("CONF"/L)
    server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By ${hostname};
        root /var/www/html;
        index index.html index.htm;

        location /hbnb_static {
            alias /data/web_static/current;
            index index.html index.htm;
        }

        location /redirect_me {
            return 301 https://hbibidunni.com/;
        }

        error_page 404 /404.html;
        location /404 {
            root /var/www/html;
            internal;
        }
    }
    CONF

class { 'nginx': }

file { '/data':
  ensure => 'directory',
}

file { '/data/web_static':
  ensure => 'directory',
}

file { '/data/web_static/releases':
  ensure => 'directory',
}

file { '/data/web_static/releases/test':
  ensure  => 'directory',
  content => "this webpage is found in data/web_static/releases/test/index.htm \n",
}

file { '/data/web_static/shared':
  ensure => 'directory',
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

exec { 'chown -R ubuntu:ubuntu /data/':
  path        => '/usr/bin:/usr/local/bin:/bin/',
  refreshonly => true,
  subscribe   => File['/data/web_static/releases/test'],
}

file { '/var/www':
  ensure => 'directory',
}

file { '/var/www/html':
  ensure  => 'directory',
  recurse => true,
  purge   => true,
  force   => true,
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "This is my first upload in /var/www/index.html***\n",
}

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page - Error page\n",
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf,
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}
