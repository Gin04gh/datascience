FROM jupyter/datascience-notebook

USER root
RUN apt-get update
RUN apt-get install -y language-pack-ja-base language-pack-ja ibus-mozc
RUN apt-get install -y fonts-takao
RUN apt-get install -y mecab
RUN apt-get install -y libmecab-dev
RUN apt-get install -y mecab-ipadic-utf8
RUN apt-get install -y swig
RUN apt-get install -y git
RUN apt-get install -y make
RUN apt-get install -y curl
RUN apt-get install -y xz-utils
RUN apt-get install -y file
RUN apt-get install -y sudo
RUN apt-get install -y wget

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git\
    && cd mecab-ipadic-neologd\
    && bin/install-mecab-ipadic-neologd -n -y

USER jovyan
RUN pip install --upgrade pip
RUN pip install sklearn
RUN pip uninstall -y matplotlib && pip install matplotlib
RUN pip install gensim
RUN pip install mecab-python3
RUN pip install xgboost
RUN pip install chainer
RUN pip install tqdm
RUN pip install wordcloud
RUN pip install pyldavis
RUN pip install sentencepiece
