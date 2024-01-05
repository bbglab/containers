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

# RUN pip --no-cache-dir install oncodrivefml
RUN git clone https://bitbucket.org/bbglab/oncodrivefml.git && \
    cd oncodrivefml && \
    git checkout feature/mutability_n_depth && \
    pip install .

RUN pip install typer

RUN export BGDATA_LOCAL="/bgdatacache" &&\
    python3 -c "from bgreference import hg38; hg38(1, 1300000, 3000)"

