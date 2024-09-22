# pip installs flask version 2.1.0

$package_name = 'flask'
package { $package_name:
  ensure   => '2.1.0' ,
}
