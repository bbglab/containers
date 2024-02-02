FROM python:3.6

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y git

RUN mkdir -p /bgdatacache/
ENV BGDATA_LOCAL="/bgdatacache"

RUN git clone https://bitbucket.org/bgframework/bgdata.git && \
    sed -i 's/local_repository = "~\/.bgdata"/local_repository = "\/bgdatacache"/' bgdata/bgdata/bgdatav2.conf.template && \
    cd bgdata && \
    pip install .

# RUN pip --no-cache-dir install oncodriveclustl
RUN git clone https://bitbucket.org/bbglab/oncodriveclustl.git && \
    cd oncodriveclustl && \
    git checkout dev/mutabilities && \
    pip install .

RUN pip install typer

RUN export BGDATA_LOCAL="/bgdatacache" &&\
    bgdata get datasets/genomereference/hg38 &&\
    bgdata get datasets/genomereference/mm10

