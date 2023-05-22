# Use the official Ubuntu base image
FROM ubuntu:latest

# Update the package list and install necessary packages
RUN apt-get update && \
    apt-get install -y openssh-server sudo

# Create a new user with the specified password and grant sudo privileges
RUN useradd -m -s /bin/bash john && \
    echo "john:geronimo" | chpasswd && \
    adduser john sudo

# Configure SSH
RUN mkdir /var/run/sshd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PermitEmptyPasswords no/PermitEmptyPasswords no/' /etc/ssh/sshd_config

# Expose the SSH port
EXPOSE 22

# Copy the contents of .files into the home directory of the container
COPY files/ /home/john/

# Start the SSH server
CMD ["/usr/sbin/sshd", "-D"]