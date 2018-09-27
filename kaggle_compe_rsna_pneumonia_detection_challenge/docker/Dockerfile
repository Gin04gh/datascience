FROM ufoym/deepo:all-py36-jupyter

RUN apt-get update && apt-get install -y vim unzip imagemagick
RUN pip install --upgrade pip
RUN pip install seaborn
RUN pip install chainercv
RUN pip install tqdm
RUN pip install pydicom
RUN pip install kaggle

RUN apt-get update && apt-get install -y apt-utils protobuf-compiler python-setuptools python-pil python-lxml python-tk git wget sudo nano
RUN pip install --upgrade pip
RUN pip install Cython
RUN pip install contextlib2
RUN pip install lxml

RUN mkdir /tensorflow && cd /tensorflow && \
    git clone https://github.com/tensorflow/models.git && \
    git clone https://github.com/cocodataset/cocoapi.git && \
    cd cocoapi/PythonAPI && \
    python setup.py build_ext --inplace && \
    rm -rf build && \
    cp -r pycocotools /tensorflow/models/research/ && \
    cd /tensorflow/models/research && \
    wget -O protobuf.zip https://github.com/google/protobuf/releases/download/v3.0.0/protoc-3.0.0-linux-x86_64.zip && \
    unzip protobuf.zip && \
    ./bin/protoc object_detection/protos/*.proto --python_out=.

# https://github.com/tensorflow/models/issues/4982
RUN sed -i".bak" "s/unicode(category_name, 'utf-8')/str(category_name, 'utf-8')/" /tensorflow/models/research/object_detection/utils/object_detection_evaluation.py

WORKDIR /tensorflow/models/research
ENV PYTHONPATH $PYTHONPATH:/tensorflow/models/research:/tensorflow/models/research/slim
