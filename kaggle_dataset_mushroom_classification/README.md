# kaggle_dataset_mushroom_classification

## Description

https://www.kaggle.com/uciml/mushroom-classification

## How to run

Get the kaggle api on my kaggle account page.  
Set up kaggle api token file, `./.kaggle/kaggle.json`.  
Then, build docker image and download data using kaggle-api,    

```
# on host
docker build -t kaggle_dataset_mushroom_classification docker/.
docker run -v `pwd`:/root -it -w=/root kaggle_dataset_mushroom_classification bash
```

```
# on client
mkdir data
chmod 600 .kaggle/kaggle.json
kaggle datasets download -d uciml/mushroom-classification -p data
exit
```

Then, restart container, 

```
docker run -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it kaggle_dataset_mushroom_classification jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
