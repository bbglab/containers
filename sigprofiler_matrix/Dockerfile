FROM python:3.9.16-slim-bullseye

RUN apt-get update
RUN apt-get install procps wget -y

RUN pip3 install SigProfilerMatrixGenerator
RUN pip3 install click

COPY download_genomes.py /usr/local/bin/
RUN chmod +x /usr/local/bin/download_genomes.py

COPY SigProfilerMatrix.py /usr/local/bin/
RUN chmod +x /usr/local/bin/SigProfilerMatrix.py

RUN chmod -R 777 /usr/local/lib/python3.9/


RUN python3 /usr/local/bin/download_genomes.py


