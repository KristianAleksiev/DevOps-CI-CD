"""
1. Introduction to Jenkins
Continuous integration - Merging code changes frequently
Continuous delivery - Ability to release at any time, every change CAN go to production
Continuous deployment - Release to production as part of an automated pipeline, every change GOES to production

Stages of CI/CD
Build -> Deploy -> Test -> Release

Jenkins - Open source automation server, lightweight, multiplatform
Jenkins project - Task configured in Jenkins
Jenkins pipeline - Project, created by a Pipeline plugin

sudo dnf install jenkins
sudo dnf install java-17-openjdk # Java runtime
sudo systemctl start jenkins
systemctl status jenkins
sudo systemctl enable jenkins
sudo firewall-cmd --permanent --add-port=8080/tcp -> jenkins
sudo firewall-cmd --permanent --add-port=80/tcp -> web app
su - #Log as root, cat the file

tail /etc/passwd
sudo usermod -s /bin/bash jenkins - Enable the current user to open bash session
sudo passwd jenkins

Generating public/private key pair for auth
ssh-keygen -t rsa -m PEM

Register the key in the authorized list
ssh-copy-id jenkins@localhost

Needed restart of service
sudo systemctl restart jenkins

2. Working with Jenkins
- Project builds
Remote credentials - User, password, key file
Firewall and SSH settings
- Remote tasks
- Schedules - Execute once at point in time or regular execution- schedule build plugin
- Plugins - Default set of plugins installed, Plugin manager
Github integration - local git client required

Creating a user on the Docker VM, register it on the Jenkins
sudo useradd jenkins
sudo passwd jenkins
sudo visudo -> jenkins ALL=(ALL)     NOPASSWD: ALL

Creating the connection between jenkins user and docker user, without password required.
Key copy needed from the jenkins vm to the docker vm
ssh-copy-id jenkins@dockervm (Password of docker vm user)
Test the connection -> SSH dockervm

3. Advanced Jenkins
- Building with Docker - Docker client required
- Pipelines - Long activity orchestration
SCS - Pipeline as code, Jenkinsfile
Jenkinsfile -> Written in Groovy, declarative or scriptive
"""