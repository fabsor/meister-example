node "mgmt" {
  class { 'systools': }
  class { 'puppet::master':
    server => "mgmt.fabsorize.me",
    certname => "mgmt.fabsorize.me"
  }
  class { 'drush': }
  class { 'jenkins': }
  class { 'postfix': }
  class { 'php': }
  class { 'mysql':
    hostname => 'mgmt',
  }
  class { 'aegir::master':
    hostmaster_url => 'mgmt.fabsorize.me',
    db_password => 'password',
    email => 'fabian@sorqvist.nu',
  }

  jenkins::job { "nodestream":
    jobfile => "puppet:///modules/jenkins/jobs/nodestream.xml"
  }

  jenkins::job { "nodestream-migrate":
    jobfile => "puppet:///modules/jenkins/jobs/nodestream_migrate.xml"
  }
  
}
