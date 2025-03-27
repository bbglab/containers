FROM quay.io/biocontainers/samtools:1.18--h50ea8bc_1

# Install rclone 1.62.2
RUN wget https://downloads.rclone.org/v1.62.2/rclone-v1.62.2-linux-amd64.zip && \
    unzip rclone-v1.62.2-linux-amd64.zip && \
    mv rclone-v1.62.2-linux-amd64/rclone /usr/bin/ 

# Verify installations
RUN samtools --version && rclone --version