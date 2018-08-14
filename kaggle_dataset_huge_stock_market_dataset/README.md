# kaggle_dataset_huge_stock_market_dataset

## Description

https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs

## How to run

Get the kaggle api on my kaggle account page.  
Set up kaggle api token file, `./.kaggle/kaggle.json`.  
Then, build docker image and download data using kaggle-api,    

```
# on host
docker build -t kaggle_dataset_huge_stock_market_dataset .
docker run -v `pwd`:/root -it -w=/root kaggle_dataset_huge_stock_market_dataset bash
```

```
# on client
mkdir data
chmod 600 .kaggle/kaggle.json
kaggle datasets download -d borismarjanovic/price-volume-data-for-all-us-stocks-etfs -p data
unzip data/Data.zip -d data/
exit
```

Then, restart container, 

```
docker run -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it kaggle_dataset_huge_stock_market_dataset jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
