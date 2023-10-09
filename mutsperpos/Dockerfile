# Merge BWA and SAMTOOLS together to allow us to pipe bwa mem to samtools sort
# based on https://hub.docker.com/r/michaelfranklin/bwasamtools
FROM ubuntu:22.04

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y python3-pysam python3
RUN apt-get install pip -y
RUN pip install matplotlib numpy pandas