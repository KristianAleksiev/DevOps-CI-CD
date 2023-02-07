"""
1. Remote (slave) hosts
- Offloading - Register nodes and use them as executors, bad practice executing on the host
Diversity in platforms and environmnets

Procedure:
- Setup keys and credentials
- Register node
- Assign label
- Configure the executors and the workspace
- Deploy the agent

Cross-host build execution.
When a job is executed by a remote host-> Locally for the remote

2. Working with Jenkins using CLI (Command line interface)
- SSH access or CLI client -> Communication through HTTP, SSH or WebSocker
- Groovy based script console

Partial commands:
help
list-jobs - all available jobs
build - job execution
create-job - create a job out of XML
get-job - returns a job represented in XML
copy-job
delete-job
reload-configuration

3. Export and import jobs
- Export a job from one instance to another
- Useful for backup purposes
- Zero touch deployment (Automation)

4. Blue Ocean
- Collection of plugins focused on multibranch pipelines
- Visual editor
- GitHub and git integration
- Instant problem diagnostics (component based problems)

Jenkinsfile "parallel" branching pipelines

5. SCM Integration
Gitea plugin -> Jenkins endpoint, web hook
"""