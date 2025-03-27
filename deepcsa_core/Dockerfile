FROM mambaorg/micromamba:2.0.5-debian12-slim

# Metadata
LABEL maintainer="bbglab <bbglab@irbbarcelona.org>"
LABEL version="0.0.1-alpha"
LABEL description="A Docker image with conda environment for deepcsa bin scripts."
LABEL source="https://github.com/bbglab/containers/deepcsa_core"

COPY --chown=$MAMBA_USER:$MAMBA_USER deepcsa.yml /tmp/conda.yml

RUN mkdir -p /home/bgdatacache/
ENV BGDATA_LOCAL="/home/bgdatacache"

RUN micromamba install -y -n base -f /tmp/conda.yml \
    # procps-ng is required for nextflow
    && micromamba install -y -n base conda-forge::procps-ng \ 
    && micromamba clean -a -y

USER root

RUN export PATH="$MAMBA_ROOT_PREFIX/bin:$PATH" \
    && bgdata get datasets/genomereference/hg38 \
    && bgdata get datasets/genomereference/mm39

RUN python -c "from bgreference import hg38, mm39; hg38(1, 1300000, 3000),  mm39(1, 1300000, 3000)"

ENV BGDATA_OFFLINE="True"
ENV PATH="$MAMBA_ROOT_PREFIX/bin:$PATH"