# Use the official Ubuntu 22.04 base image
FROM ubuntu:22.04

# Set environment variables to avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install Python 3
RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get clean

# Copy the Hello World script into the image
COPY hello.py ~/ros2_training/docker_python/hello.py

# Set the entry point to the Hello World script
ENTRYPOINT ["python3", "~/ros2_training/docker_python/hello.py"]
