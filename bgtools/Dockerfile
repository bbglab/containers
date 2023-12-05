FROM python:3.10.5

RUN mkdir -p /bgdatacache/
ENV BGDATA_LOCAL="/bgdatacache"

RUN apt-get update -y && apt-get upgrade -y
# RUN apt-get install -y python3 pip libcurl4-openssl-dev libssl-dev
RUN pip install matplotlib numpy pandas
RUN pip install bgdata
RUN pip install bgreference

RUN python3 -c "from bgreference import hg38; hg38(1, 1300000, 3000)"

# CMD [ "python3" ]
# RUN pip install open-variant bgoncotree oncodriveclustl bgsignature oncodrivefml