# kaggle_dataset_large_tennis_dataset_for_atp_itf_betting

## Description

https://www.kaggle.com/gmadevs/atp-matches-dataset

## How to run

Get the kaggle api on my kaggle account page.  
Set up kaggle api token file, `./.kaggle/kaggle.json`.  
Then, build docker image and download data using kaggle-api,    

```
# on host
docker build -t kaggle_dataset_large_tennis_dataset_for_atp_itf_betting docker/.
docker run -v `pwd`:/root -it -w=/root kaggle_dataset_large_tennis_dataset_for_atp_itf_betting bash
```

```
# on client
mkdir data
chmod 600 .kaggle/kaggle.json
kaggle datasets download -d ehallmar/a-large-tennis-dataset-for-atp-and-itf-betting -p data
unzip data/a-large-tennis-dataset-for-atp-and-itf-betting.zip -d data
exit
```

Then, restart container, 

```
docker run -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it kaggle_dataset_large_tennis_dataset_for_atp_itf_betting jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
