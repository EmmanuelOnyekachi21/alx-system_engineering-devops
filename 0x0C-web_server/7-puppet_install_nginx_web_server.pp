# Ensure system package index is up to date.
exec { 'apt_update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  unless  => '/usr/bin/test -f /var/lib/apt/periodic/update-success-stamp',
}

# Install ufw
package { 'ufw':
  ensure => 'installed',
}

# Ensure UFW is running and enabled
service { 'ufw':
  ensure => 'running',
  enable => true,
}

# Install Nginx and configure the server
package{ 'nginx':
  ensure  => 'installed',  # Ensures Nginx is installed.
  require => Exec['apt_update'], # Ensure apt update runs before this
}

# Ensure Nginx is running
service { 'nginx':
  ensure  => 'running', # Ensures the service is running
  enable  => true,  # Enables Nginx to start at boot
  # Waits for Nginx to be installed
  require => Package['nginx'],
}

# Allow HTTP traffic via ufw
exec { 'allow_nginx_http':
  command => 'ufw allow "Nginx HTTP"',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
  unless  => 'ufw status | grep -q "Nginx HTTP"',
  require => Service['nginx'], # Ensure Nginx is running be4 opening firewall
}

# Ensure the root page serves "Hello World!"
file {'/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!\n',
  mode    => '0644',
  require => Package['nginx'], # Ensure Nginx is installed be$ creating D' file
}

# Update the Nginx default site configuration for Hello World and redirect
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {

        error_page 404 /custom_404.html;

        location /redirect_me {
                rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        }
                try_files \$uri \$uri/ =404;
        }
}",
  notify  => Service['nginx'], # Restart Nginx if the file is changed
}

# Custom 404 page
file { '/var/www/html/custom_404.html':
  ensure  => 'file',
  content => "Ceci n'est pas une page",
  mode    => '0644',
  require => Package['nginx'],
}
