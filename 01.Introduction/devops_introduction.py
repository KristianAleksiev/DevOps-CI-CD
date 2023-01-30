"""
1. DevOps culture and core values
- Process optimization
- Break down barriers between teams, safe environment
- Automation - Saves time, prevent defects, consistency
- Measurement
- Sharing - Tools, knowledge

2. Tools
- Planning (transparency)
- Tracking (feedback)
- Source control
- Building and testing
- Security assessment
- Continuous integration and deployment
- Config and infrastructure management (consistency)
- Monitoring and logging (measurement)

3. Virtualization - Principles and use cases

4. Vagrant
- Building and managing VM environments
- Supports VB, AWS, VMware
- Provision tools such as shell scripts, Chef or Puppet


- Basic commands:
vagrant init [options] [box] - Create a vagrant env
vagrant  ssh [options] [name|id]
vagrant up
vagrant halt
vagrant destroy
vagrant box <command>

VM to Vagrant box:
SSH port 22
vi /ssh/sshd_config, root log prohibition
systemctl restart ssh

    Hdd packages:
    sudo dnf install kernel-devel gcc make tar bzip2 wget elfutils-libelf-devel (centOS)

mount the disk - sudo mount /dev/sr0 /mnt
uncompress additions - sudo /mnt/VboxLinuxAdditions.run

from host: vagrant package --base vm_name

"""