# kaggle_dataset_credit_card_fraud_detection

## Description

https://www.kaggle.com/uciml/mushroom-classification

## How to run

Get the kaggle api on my kaggle account page.  
Set up kaggle api token file, `./.kaggle/kaggle.json`.  
Then, build docker image and download data using kaggle-api,    

```
# on host
docker build -t kaggle_dataset_credit_card_fraud_detection .
docker run -v `pwd`:/root -it -w=/root kaggle_dataset_credit_card_fraud_detection bash
```

```
# on client
mkdir data
chmod 600 .kaggle/kaggle.json
kaggle datasets download -d mlg-ulb/creditcardfraud -p data
exit
```

Then, restart container, 

```
docker run -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it kaggle_dataset_credit_card_fraud_detection jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
