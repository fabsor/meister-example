from fabric.api import settings, abort, run, cd, sudo, put, env, prompt, get
from fabric.contrib.project import rsync_project

def set_hostname(hostname):
    # Check if our host is there, if not add it.
    get('/etc/hosts', '/tmp/hosts-{0}'.format(hostname))
    hosts = open('/tmp/hosts-{0}'.format(hostname), 'r').read()

    if hosts.find(hostname) == -1:
        hosts = hosts.split("\n")
        new_hosts = "127.0.0.1 localhost {0}\n".format(hostname)
        new_hosts += "\n".join(hosts[1:])
        open('/tmp/hosts-{0}'.format(hostname), 'w').write(new_hosts)
        put('/tmp/hosts-{0}'.format(hostname), '/tmp/hosts')
        sudo('mv /tmp/hosts /etc/hosts')
        sudo('echo {0} > /etc/hostname'.format(hostname))
        sudo('service hostname start')

def copy_manifests():
    run("mkdir -p puppet")
    rsync_project("~/puppet", "manifests")
    rsync_project("~/puppet", "modules")

def install_puppet():
    sudo("apt-get install -y puppet")

def run_puppet():
    sudo("service puppet stop")
    sudo("puppet agent --verbose --no-daemonize --certname=application1 --server=mgmt.fabsorize.me --onetime")
    sudo("service puppet start")

def add_jenkins_user(user):
    sudo("adduser {0}".format(user))
    sudo("adduser {0} jenkins".format(user))

def install_puppet_master():
    sudo("apt-get update")
    sudo("apt-get install -y puppetmaster")
    sudo("rm -rf /etc/puppet/manifests")
    sudo("rm -rf /etc/puppet/modules")
    sudo("ln -s /home/ubuntu/puppet/manifests /etc/puppet/manifests")
    sudo("ln -s /home/ubuntu/puppet/modules /etc/puppet/modules")
    sudo("puppet apply --verbose /etc/puppet/manifests/nodes/master.pp")
    sudo("service puppetmaster restart")

def provision_master():
    copy_manifests()
    sudo("puppet apply --verbose /etc/puppet/manifests/nodes/master.pp")


def connect_to_master(certname, server):
    sudo("puppet agent --waitforcert 60 --certname {0} --server mgmt.fabsorize.me".format(certname))
    with settings(host_string=env.meister[server]):
        sudo("puppetca -s {0}".format(certname))
    sudo("service puppet stop")
    sudo("puppet agent --verbose --no-daemonize --certname=application1 --server=mgmt.fabsorize.me --onetime")
    
