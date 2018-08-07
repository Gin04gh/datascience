# nlp_binary_relevance

## Description

## How to run

```
docker build -t nlp_binary_relevance .
docker run -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it nlp_binary_relevance jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
