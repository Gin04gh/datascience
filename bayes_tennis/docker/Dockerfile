FROM jupyter/datascience-notebook

USER root
RUN apt-get update
RUN apt-get -y install git
RUN apt-get -y install build-essential

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --upgrade numpy==1.14.5
RUN pip install --no-cache-dir --upgrade Cython==0.28.4 
RUN pip install --no-cache-dir --upgrade pystan==2.17.1.0

RUN cd /home/jovyan/ && \
    git clone https://github.com/JeffSackmann/tennis_atp.git

RUN echo "c.NotebookApp.password = ''" >> /home/jovyan/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.token = ''" >> /home/jovyan/.jupyter/jupyter_notebook_config.py

#RUN apt-get -y install xvfb libfontconfig
#ENV WKHTMLTOPDF_VERSION 0.12.4
#RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/${WKHTMLTOPDF_VERSION}/wkhtmltox-${WKHTMLTOPDF_VERSION}_linux-generic-amd64.tar.xz
#RUN tar vxfJ wkhtmltox-${WKHTMLTOPDF_VERSION}_linux-generic-amd64.tar.xz && \
#    ln -s /opt/wkhtmltox/bin/wkhtmltopdf /usr/bin/wkhtmltopdf
#RUN apt-get -y install imagemagick
#RUN pip install imgkit
