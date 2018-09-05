# nlp_binary_relevance

## Description

note about Binary Relevance Learning.  
See http://www.aic.uniovi.es/~jdiez/Jorge_Diez/Journal_Papers_files/luaces2012a.pdf

## How to run

```
docker build -t nlp_binary_relevance docker/.
docker run -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it nlp_binary_relevance jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
