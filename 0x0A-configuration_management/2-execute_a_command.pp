# Puppet manifest to kill a process named killmenow using pkill
exec { 'killmenow':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
}
