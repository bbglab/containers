FROM python:3.8

ENV LC_ALL=C

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y bash \
    && pip install --upgrade pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /bgdatacache/ /home/user/.config/bbglab/

ENV BGDATA_LOCAL="/bgdatacache"
ENV BBGLAB_HOME="/home/user/.config/bbglab/"

RUN pip install bgdata bgreference 

RUN echo "# Version of the bgdata config file\n\
version = 2\n\
\n\
# The default local folder where you want to store the data packages\n\
local_repository = \"/bgdatacache\"\n\
\n\
# The remote URL from where do you want to download the data packages\n\
remote_repository = \"https://bbglab.irbbarcelona.org/bgdata\"\n\
\n\
# If you want to force bgdata to work only locally\n\
# offline = True\n\
\n\
# Cache repositories\n\
[cache_repositories]" > /home/user/.config/bbglab/bgdatav2.conf

RUN bgdata get datasets/genomereference/hg38 && bgdata get datasets/genomereference/hg19
RUN bgdata get datasets/genomereference/mm39 && bgdata get datasets/genomereference/mm10
# RUN python3 -c "from bgreference import hg38, hg19; hg38(1, 1300000, 3000); hg19(1, 1300000, 3000)"
RUN python3 -c "from bgreference import mm39, mm10; mm39(1, 1300000, 3000); mm10(1, 1300000, 3000)"

RUN chmod -R 777 /bgdatacache/*


COPY oncodrive3d ${DOCKER_ROOTFS}/oncodrive3d

RUN pip install /oncodrive3d

# Test the installation
CMD ["oncodrive3D", "run", "--help"]

LABEL Author="stefano.pellegrini@irbbarcelona.org"