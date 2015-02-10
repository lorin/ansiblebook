FROM ubuntu:trusty
MAINTAINER lorin@ansiblebook.com

# Based on
# https://www.digitalocean.com/community/tutorials/docker-explained-how-to-create-docker-containers-running-memcached

# Update the default application repository sources list
RUN apt-get update

# Install Memcached
RUN apt-get install -y memcached

# Port to expose (default: 11211)
EXPOSE 11211

# Default Memcached run command arguments
CMD ["-m", "128"]

# Set the user to run Memcached daemon
USER daemon

# Set the entrypoint to memcached binary
ENTRYPOINT memcached
