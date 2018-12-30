# news_corpus

## Description



## How to run

If use livedoor-news-corpus,

```
mkdir -p data/livedoor-news-corpus
cd data/livedoor-news-corpus
curl -O https://www.rondhuit.com/download/ldcc-20140209.tar.gz
tar -zxvf ldcc-20140209.tar.gz 
```

Docker run,

```
docker build -t news_corpus docker/.
docker run -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it news_corpus jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
