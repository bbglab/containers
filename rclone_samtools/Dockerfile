FROM quay.io/biocontainers/samtools:1.18--h50ea8bc_1

USER root

# update 
RUN apt-get update -y && apt-get upgrade -y

# Install rclone 1.62.2
RUN wget https://downloads.rclone.org/v1.62.2/rclone-v1.62.2-linux-amd64.deb && \
    apt-get update && \
    apt-get install -y ./rclone-v1.62.2-linux-amd64.deb
