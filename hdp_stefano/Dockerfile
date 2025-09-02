FROM rocker/r-ver:4.2.1

# Fix the /bin directory issue by installing usrmerge
RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    usrmerge && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install additional dependencies
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    zlib1g-dev \
    slurm-wlm \
    libhts-dev \
    libbz2-dev \
    liblzma-dev \
    libncurses-dev \
    libreadline-dev \
    git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install R libraries
RUN Rscript -e '.libPaths("/usr/local/lib/R/site-library")'
RUN Rscript -e 'install.packages(pkgs = "pkgdown");library("pkgdown")'
RUN Rscript -e 'install.packages(pkgs = "devtools");library("devtools")'
RUN Rscript -e 'devtools::install_github("nicolaroberts/hdp", build_vignettes = FALSE);library(hdp)'


RUN git clone https://github.com/McGranahanLab/HDP_sigExtraction.git /app/HDP_sigExtraction
RUN sed -i '/Sys.getenv("SLURM_ARRAY_TASK_ID")/c\
if (length(cmdArgs) >= 10 && cmdArgs[10] != "") {\n  iter <- as.numeric(cmdArgs[10])\n} else {\n  iter <- as.numeric(Sys.getenv("SLURM_ARRAY_TASK_ID"))\n}' /app/HDP_sigExtraction/R/run_HDP_chainSampling.R


RUN rm -r /app/HDP_sigExtraction/HDP_wrapper.sh /app/HDP_sigExtraction/data /app/HDP_sigExtraction/examples

# Install dependencies for HDP_sigExtraction
RUN Rscript -e 'install.packages(pkgs = "BiocManager");library("BiocManager")'
RUN Rscript -e 'BiocManager::install("BiocStyle");library("BiocStyle")'
RUN Rscript -e 'BiocManager::install("BiocGenerics");library("BiocGenerics")'
RUN Rscript -e 'BiocManager::install("Biostrings");library("Biostrings")'
RUN Rscript -e 'BiocManager::install("GenomicRanges");library("GenomicRanges")'
RUN Rscript -e 'BiocManager::install("IRanges");library("IRanges")'
RUN Rscript -e 'install.packages(pkgs = "ggplot2");library("ggplot2")'
RUN Rscript -e 'install.packages(pkgs = "lsa");library("lsa")'
RUN Rscript -e 'BiocManager::install("RColorBrewer");library("RColorBrewer")'
RUN Rscript -e 'BiocManager::install("Metrics");library("Metrics")'
RUN Rscript -e 'BiocManager::install("BSgenome");library("BSgenome")'
RUN Rscript -e 'BiocManager::install("BSgenome.Hsapiens.UCSC.hg19");library("BSgenome.Hsapiens.UCSC.hg19")'
RUN Rscript -e 'install.packages(pkgs = "deconstructSigs");library("deconstructSigs")'
RUN Rscript -e 'install.packages(pkgs = "dplyr");library("dplyr")'
RUN Rscript -e 'install.packages(pkgs = "cowplot");library("cowplot")'
RUN Rscript -e 'install.packages(pkgs = "gridExtra");library("gridExtra")'


ENV PATH="/app/HDP_sigExtraction/R:$PATH"


# # Install additional dependencies
# RUN apt-get update -y && \
#     apt-get install -y --no-install-recommends \
#     libbz2-dev \
#     liblzma-dev \
#     libncurses-dev \
#      \
#     libreadline-dev \
#     && \
#     apt-get clean && rm -rf /var/lib/apt/lists/*

# RUN Rscript -e 'BiocManager::install("GenomicFeatures");library("GenomicFeatures")'
