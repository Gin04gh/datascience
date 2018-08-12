# kaggle_dataset_association_of_tennis_professionals_matches

## Description

https://www.kaggle.com/gmadevs/atp-matches-dataset

## How to run

Get the kaggle api on my kaggle account page.  
Set up kaggle api token file, `./.kaggle/kaggle.json`.  
Then, build docker image and download data using kaggle-api,    

```
# on host
docker build -t kaggle_dataset_association_of_tennis_professionals_matches .
docker run -v `pwd`:/root -it -w=/root kaggle_dataset_association_of_tennis_professionals_matches bash
```

```
# on client
mkdir data
chmod 600 .kaggle/kaggle.json
kaggle datasets download -d gmadevs/atp-matches-dataset -p data
exit
```

Then, restart container, 

```
docker run -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it kaggle_dataset_association_of_tennis_professionals_matches jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
