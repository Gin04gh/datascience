FROM kaggle/python

USER root
RUN apt-get update
RUN apt-get -y install git

RUN cd / && \
    git clone https://github.com/JeffSackmann/tennis_atp.git

RUN jupyter notebook --generate-config && \
    echo "c.NotebookApp.password = ''" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.token = ''" >> /root/.jupyter/jupyter_notebook_config.py

RUN apt-get -y install --upgrade gcc++
