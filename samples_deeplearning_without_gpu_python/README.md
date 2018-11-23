# samples_deeplearning_without_gpu_python

## Description

Pythonによるディープラーニング関連の実験コード集.  

## How to run

```
docker build -t samples_deeplearning_python docker/.
```

If use jupyter notebook, 

```
docker run -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it samples_deeplearning_without_gpu_python jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```

If use bash,

```
docker run -v `pwd`:/tmp_work -w=/tmp/work --rm -it samples_deeplearning_without_gpu_python bash
```

Using chainer pre-trained model, for example resnet, download weight files see, https://github.com/KaimingHe/deep-residual-networks
Make dir and put weight files to host `root/.chainer/dataset/pfnet/chainer/models/`, 

```
docker run -v `pwd`:/tmp/work -v /root:/root -w=/tmp/work -p 8888:8888 --rm -it samples_deeplearning_without_gpu_python jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
