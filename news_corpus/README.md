# news_corpus

## Description



## How to run

```
docker build -t news_corpus docker/.
docker run -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it news_corpus jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
