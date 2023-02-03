"""
1. Advanced techniques
- Networking
bridge driver - default driver, allows containers connected to the same bridge to communicate
command: docker network create -d bridge name

overlay driver - connects multiple daemons, swarm services communication
ipvlan - control over IPv4 and IPv6
macvlan - gives a container own MAC

docker network ls - List all networks
docker network connect - Connect a container to a network

- Volumes - Allow external data in containers
Data volumes, Data volume containers

2. Distributed applications
- Linking methods
docker container run -d .... --link c-db:db - by name alias - depricated
isolated manual network - docker container run .... --net app-network <===

- Docker compose - Define and run multi-container docker apps, isolated environmnets on single host
Preserve volume data when containers are created

3. Docker clusters - Azure, AWS deployment
Commands executed by swarm manager
Nodes that are not managers are called workers
Both managers and workers are running containers
- Components and principles
docker swarm init - Initialize cluster
docker swarm join - Join to a cluster (managers and workers)

Tasks - Units of work distributed to nodes
Service - Group of tasks deployed on swarm
Stack - Group of services
Stacks are deployed with docker-compose

Replicated and Global services distribution model
"""