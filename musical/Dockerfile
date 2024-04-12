FROM python:3.10.5

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install git procps -y

RUN pip install numpy scipy scikit-learn matplotlib pandas seaborn click
RUN git clone https://github.com/parklab/MuSiCal.git && \
        cd MuSiCal && \
        pip install .
