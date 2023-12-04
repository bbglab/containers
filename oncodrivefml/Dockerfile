FROM python:3.6

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install git
# RUN pip --no-cache-dir install oncodrivefml
RUN git clone https://bitbucket.org/bbglab/oncodrivefml.git
RUN cd oncodrivefml && git checkout feature/mutability_n_depth && pip install .

RUN python3 -c "from bgreference import hg38; hg38(1, 1300000, 3000)"

RUN oncodrivefml --help