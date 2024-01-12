FROM python:3.9.16-slim-bullseye

RUN apt-get update && \
    apt-get install procps wget rsync -y && \
    pip3 install SigProfilerMatrixGenerator==1.2.19 SigProfilerAssignment==0.1.0 SigProfilerExtractor==1.1.23 click

COPY SigProfilerMatrix.py SigProfilerAssignment.py /usr/local/bin/
RUN chmod +x /usr/local/bin/SigProfiler*

RUN SigProfilerMatrixGenerator install GRCh38 && \ 
    SigProfilerMatrixGenerator install mm10

RUN mkdir /usr/local/lib/python3.9/site-packages/SigProfilerAssignment/DecompositionPlots/CosmicTemplates && \
    chmod -R 777 /usr/local/lib/python3.9/

ENTRYPOINT ["python3", "/usr/local/bin/SigProfilerAssignment.py", "/usr/local/bin/SigProfilerMatrix.py"]

