# qiita_transfer_learining_fine_tuning_chainer

## Description


## How to run

Use nvidia-docker.  
Set up commands are

```
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
  sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update

sudo apt-get install -y nvidia-docker2
sudo pkill -SIGHUP dockerd

# Test nvidia-smi
docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi
```

See https://github.com/NVIDIA/nvidia-docker

Start command is

```
docker build -t qiita_transfer_learining_fine_tuning_chainer docker/.
```

Using container image is https://github.com/ufoym/deepo  

Using chainer pre-trained model, for example resnet, download weight files see, https://github.com/KaimingHe/deep-residual-networks
Make dir and put weight files to host `root/.chainer/dataset/pfnet/chainer/models/`, 

```
docker run --runtime=nvidia -v `pwd`:/tmp/work -v /root:/root -w=/tmp/work -p 8888:8888 --rm -it qiita_transfer_learining_fine_tuning_chainer jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
