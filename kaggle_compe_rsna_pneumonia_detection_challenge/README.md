# kaggle_compe_rsna_pneumonia_detection_challenge

## Description

https://www.kaggle.com/c/rsna-pneumonia-detection-challenge

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
docker build -t kaggle_compe_rsna_pneumonia_detection_challenge docker/.
```

Using container image is https://github.com/ufoym/deepo  

Get the kaggle api on my kaggle account page.  
Set up kaggle api token file, `./.kaggle/kaggle.json`.  
Then, build docker image and download data using kaggle-api,    

```
# on host
docker build -t kaggle_compe_rsna_pneumonia_detection_challenge docker/.
docker run -v `pwd`:/root -it -w=/root kaggle_compe_rsna_pneumonia_detection_challenge bash
```

```
# on client
mkdir data
chmod 600 .kaggle/kaggle.json
kaggle competitions download -c rsna-pneumonia-detection-challenge -p ./data
unzip data/stage_1_detailed_class_info.csv.zip -d data/
unzip data/stage_1_train_labels.csv.zip -d data/
unzip data/stage_1_train_images.zip -d data/stage_1_train_images
unzip data/stage_1_test_images.zip -d data/stage_1_test_images
exit
```

Then, restart container, 

```
docker run --runtime=nvidia -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it kaggle_compe_rsna_pneumonia_detection_challenge jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
