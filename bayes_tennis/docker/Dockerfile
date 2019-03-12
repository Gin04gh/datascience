FROM jupyter/datascience-notebook

USER root
RUN apt-get update
RUN apt-get -y install git

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --upgrade numpy==1.14.5
RUN pip install --no-cache-dir --upgrade Cython==0.28.4 
RUN pip install --no-cache-dir --upgrade pystan==2.17.1.0

RUN cd /home/jovyan/ && \
    git clone https://github.com/JeffSackmann/tennis_atp.git

RUN curl -L  "https://oscdl.ipa.go.jp/IPAexfont/ipaexg00301.zip" > font.zip
RUN unzip font.zip
RUN cp ipaexg00301/ipaexg.ttf /opt/conda/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf/ipaexg.ttf
RUN echo "font.family : IPAexGothic" >>  /opt/conda/lib/python3.6/site-packages/matplotlib/mpl-data/matplotlibrc
RUN rm -r ./.cache

RUN echo "c.NotebookApp.password = ''" >> /home/jovyan/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.token = ''" >> /home/jovyan/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.open_browser = False" >> /home/jovyan/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.notebook_dir = '/home/jovyan/work'" >> /home/jovyan/.jupyter/jupyter_notebook_config.py
