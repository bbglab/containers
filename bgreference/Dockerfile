FROM python:3.10.5

RUN mkdir -p /bgdatacache/
ENV BGDATA_LOCAL="/bgdatacache"

RUN useradd -m -d /home/user -s /bin/bash user && \
    echo "user:userpass" | chpasswd && \
    usermod -aG sudo user
    
RUN apt-get update -y && apt-get upgrade -y
RUN pip install matplotlib numpy pandas
RUN pip install bgdata
RUN pip install bgreference

RUN mkdir -p /home/user/.config/bbglab/ 
RUN chown user:user /home/user/.config/bbglab/ && \
    chmod 644 /home/user/.config/bbglab/
    
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
offline = True\n\
\n\
# Cache repositories\n\
[cache_repositories]" > /home/user/.config/bbglab/bgdatav2.conf

RUN chown user:user /home/user/.config/bbglab/bgdatav2.conf && \
    chmod 644 /home/user/.config/bbglab/bgdatav2.conf
    
RUN python3 -c "from bgreference import hg38; hg38(1, 1300000, 3000)"

USER user
WORKDIR /home/user
