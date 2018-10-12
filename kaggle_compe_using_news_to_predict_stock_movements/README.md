# kaggle_compe_using_news_to_predict_stock_movements

Get the kaggle api on my kaggle account page.  
Set up kaggle api token file, `./.kaggle/kaggle.json`.  
Then, build docker image and download data using kaggle-api,    

```
# on host
docker build -t kaggle_compe_using_news_to_predict_stock_movements docker/.
docker run -v `pwd`:/root -it -w=/root kaggle_compe_using_news_to_predict_stock_movements bash
```

```
# on client
mkdir data
chmod 600 .kaggle/kaggle.json
kaggle competitions download -c two-sigma-financial-news -p data
exit
```

Then, restart container, 

```
docker run -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it kaggle_compe_using_news_to_predict_stock_movements jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
