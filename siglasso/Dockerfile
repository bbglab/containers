FROM r-base:4.2.1

RUN apt-get update -y
#RUN apt-get update -y && \
#    apt-get upgrade -y 

# Specify path for installing R libraries inside container
RUN Rscript -e '.libPaths("/usr/local/lib/R/site-library")'

RUN apt-get -y install libcurl4-openssl-dev libxml2-dev

# Install R package siglasso
RUN Rscript -e 'install.packages(pkgs = "remotes")'
RUN Rscript -e 'remotes::install_github(repo = "gersteinlab/siglasso")'

RUN apt-get -y install procps
