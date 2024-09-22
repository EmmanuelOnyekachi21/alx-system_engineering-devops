# Killmenow
exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/bin/pgrep killmenow',  # Executes only if the process is running
  path    => ['/bin', '/usr/bin'],    # Ensure correct paths for commands
}
