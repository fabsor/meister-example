# Meister example configuration

This is an example meister example configuration that sets up a
"master" server, which is a puppet master, aegir hostmaster and
jenkins server, that is meant to be used as a controller for a set of
machines and an application server that can be used to run one or more
Drupal sites.

This is meant as a good starting point for getting a setup up and
running.

# Configuration

* Install [meister](https://github.com/WKLive/meister)
* Copy the meister.yml.dist to meister.yml and change the settings in
  there to something useful.
* Change the .dist files in the manifests/nodes folder to match your
  needs
* Go to manifests/nodes and edit the nodes so that domains and so on
  match your needs
* Edit the tasks.py to match whatever domain names you will be using.
* Run "make keys" to generate keys that will be used for communication
  between the machines.
