# Ensure SSH client configuration
file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => "
    # Managed by Puppet
    Include /etc/ssh/ssh_config.d/*.conf
    Host *
      PasswordAuthentication no
      IdentityFile ~/.ssh/school
      SendEnv LANG LC_*
      HashKnownHosts yes
      GSSAPIAuthentication yes
  ",
}

