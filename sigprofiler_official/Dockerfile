# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

ENV SIGPROFILERMATRIXGENERATOR_VOLUME=/usr/src/app

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y procps

# Install SigProfilerMatrixGenerator from PyPI
RUN pip install SigProfilerMatrixGenerator==1.3.5

# Create a non-root user named 'spm_user'
RUN useradd -m -s /bin/bash spm_user

# Change the ownership of the /usr/src/app directory and its contents to the new non-root user
RUN chown -R spm_user:spm_user /usr/src/app

# Switch to the non-root user for subsequent commands and when running the container
USER spm_user

# Install the most recent version of the reference genomes
RUN SigProfilerMatrixGenerator install GRCh38
RUN SigProfilerMatrixGenerator install GRCh37
RUN SigProfilerMatrixGenerator install mm39
