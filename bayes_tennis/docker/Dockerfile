FROM jupyter/datascience-notebook

RUN pip install --upgrade pip
RUN pip install matplotlib
RUN pip install pystan

RUN pip install jupyter
RUN pip install jupyter-contrib-nbextensions
RUN pip install jupyter-nbextensions-configurator
RUN jupyter contrib nbextension install --user
RUN jupyter nbextensions_configurator enable --user

USER root
RUN apt-get update
RUN apt-get -y install git

RUN cd /home/jovyan/ && \
    git clone https://github.com/JeffSackmann/tennis_atp.git
