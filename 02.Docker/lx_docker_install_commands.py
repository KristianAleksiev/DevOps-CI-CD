"""
sudo dnf install docker-ce docker-ce-cli containerd.io

### Start and status
sudo systemctl start docker
systemctl status docker

### Run a container
sudo docker container run X -> Container from image X

### Docker containers
docker system info -> Images, containers, running containers etc.

### Autostart Docker
sudo systemctl enable docker -> On start

### Download an image to the host
docker pull / docker image pull

### Download an image to the host and run the container
docker run / container run

### Build an image on the host locally
docker build / image build

### Publish the image to a register
docker push

### Search the Docker Hub for images
docker search X

### List locally available images
docker image ls / images

### List containers
docker container ls / docker ps

### Delete container
docker container rm NAME

### Delete image
docker image rm NAME -> For images that are not used by containers

### Create container
docker create / docker container create -> Without starting it

### Rename a container
docker container rename CURRENT_NAME NEW_NAME

### Kill a running container
docker container kill ID

### Start a container
docker container start ID

### Restart a container
docker restart container ID

### Stop a running container
docker container stop ID

### Pause a running container
docker container pause ID -> Remain as a process

### Unpause a running container
docker container unpause ID

### Attach to a running container
docker container attach ID

### Create a version of an image - Tagging
docker image tag LOCAL_version REPO_version

### Export a container's filesystem as tar archive
docker container export CONTAINER

### Import a container
docker container import

### Load an image
docker image load

### Create an image from container
docker container commit ID name
"""