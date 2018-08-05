# pilotnet_visualbackprop

## Description

PilotNet + Visual back prop.  
See, 
* https://arxiv.org/abs/1704.07911
* https://devblogs.nvidia.com/explaining-deep-learning-self-driving-car/

Using dataset is udacity self-driving dataset.  
See,
* https://github.com/udacity/self-driving-car
* https://github.com/rwightman/udacity-driving-reader

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
docker build -t pilotnet_visualbackprop .
```

Using container image is https://github.com/ufoym/deepo  

Notebook start command is

```
docker run --runtime=nvidia -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it pilotnet_visualbackprop jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
