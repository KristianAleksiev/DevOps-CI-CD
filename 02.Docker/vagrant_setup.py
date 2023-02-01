"""
vagrant init --minimal ~address~
notepad Vagrantfile

====
# _*_ mode: ruby _*_
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.vm.box = ~address~
    config.vm.network "forwarded_port", guest: 8080, host: 8080, auto_correect: true
    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "2048"
    end
end
====
vagrant up
vagrant ssh

"""