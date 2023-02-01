"""
1. Containerization
- Virtualization of an operating system, the kernel allows the existence of multiple user space instances
- Independent work of processes

Types of containers:
- System containers - Jails, Zones
Multiple processes

- App containers - containerd - Docker
Single process

Containerization vs VMs and Containers with VMs

2. Containerization with Docker
- Container host is a physical or virtual computer system, configured with a container engine
- Container image shows the state of a container, registry or file system changes
- Container repository - Organizing images and their dependencies

- Container - Runnable instance of an image
- Image - Template of a container build from layers => Simpler software distribution
- Repository - Collection of different versions of an image identified by tags
- Registry - Collection of repositories

Image layered architecture:
- Allows the usage of the same base layer from multiple containers
- The container uses the last layer of the image (The writable layer)

Docker platform (Host):
Docker client => Docker API => Docker Daemon (dockerd) => Container Runtime (containerd)
Docker Daemon - Registry (Docker Hub)

Commands and workflow:
docker pull - Download an image to the host
docker run - Download an image to the host and run the container
docker build - Build an image on the host locally
docker push - Publish the image to a register

3. Creation of images from containers
- From container
- From file (dockerfile):
FROM image_base - Defines the base image to use to start the building process, no tags for latest version
LABEL maintainer="X" - Metadata about the image
RUN - Forms another layer, add software e.g. -> RUN apt-get -y update, single or pipeline commands
COPY - Copy files between host  and container -> COPY X.txt /root
ADD - Inject files from URL into the new image
CMD - Defaults for an executing container

- Heredoc container - Creating new images from StdIn
docker build -t htop - << EOF
"""