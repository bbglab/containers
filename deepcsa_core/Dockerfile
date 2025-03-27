FROM mambaorg/micromamba:2.0.5-debian12-slim

# Metadata
LABEL maintainer="bbglab <bbglab@irbbarcelona.org>"
LABEL version="0.0.1-alpha"
LABEL description="A Docker image with conda environment for deepcsa bin scripts."
LABEL source="https://github.com/bbglab/containers/deepcsa_core"

COPY --chown=$MAMBA_USER:$MAMBA_USER deepcsa.yml /tmp/conda.yml

# Configure matplotlib
ENV MPLCONFIGDIR=/tmp/matplotlib_config
RUN mkdir -p "$MPLCONFIGDIR" && chmod -R 777 "$MPLCONFIGDIR"

# Set up BGDATA cache
ENV BGDATA_LOCAL="/home/bgdatacache"
RUN mkdir -p $BGDATA_LOCAL

RUN micromamba install -y -n base -f /tmp/conda.yml \
    && micromamba install -y -n base conda-forge::procps-ng \
    && micromamba clean -a -y

ENV PATH="$MAMBA_ROOT_PREFIX/bin:$PATH"

USER $MAMBA_USER

# Download genome reference datasets
RUN bgdata get datasets/genomereference/hg38 \
    && bgdata get datasets/genomereference/mm39

# Test dataset access with Python
RUN python -c "from bgreference import hg38, mm39; hg38(1, 1300000, 3000); mm39(1, 1300000, 3000)"

# Set offline mode after downloading
ENV BGDATA_OFFLINE="True"

CMD ["bash"]
