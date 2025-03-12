FROM mambaorg/micromamba:2.0.5-debian12-slim

COPY --chown=$MAMBA_USER:$MAMBA_USER deepcsa.yml /tmp/conda.yml

RUN micromamba install -y -n base -f /tmp/conda.yml \
    # procps-ng is required for nextflow
    && micromamba install -y -n base conda-forge::procps-ng \ 
    && micromamba clean -a -y

USER root

ENV PATH="$MAMBA_ROOT_PREFIX/bin:$PATH"
