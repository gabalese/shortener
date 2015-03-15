# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.synced_folder ".", "/vagrant"

$script = <<SCRIPT
sudo apt-get update
sudo apt-get install -y openjdk-7-jre
sudo apt-get install -y postgresql python-dev python-pip python-psycopg2
SCRIPT

  config.vm.provision "shell", inline: $script

end
