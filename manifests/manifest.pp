class { 'systools': }
class { 'apache': }
class { 'php': }
class { 'drush': }
class { 'postfix': }
class { 'mongodb': }


class { 'mysql':
  local_only     => true,
  hostname => "devbox.dev"
}

apache::vhost { "drupal": }
