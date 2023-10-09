# Merge BWA and SAMTOOLS together to allow us to pipe bwa mem to samtools sort
# based on https://hub.docker.com/r/michaelfranklin/bwasamtools
FROM quay.io/pacbio/samtools:1.17

RUN apt-get update -y && apt-get upgrade -y

RUN wget https://github.com/samtools/samtools/releases/download/1.18/samtools-1.18.tar.bz2 \
    && tar -xjf samtools-1.18.tar.bz2 \
    && rm -rf samtools-1.18.tar.bz2  \
    && cd samtools-1.18/ \
    && make && make install

