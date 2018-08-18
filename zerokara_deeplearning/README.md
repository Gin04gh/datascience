# samples_python

## Description

* https://www.oreilly.co.jp/books/9784873117584/
* https://www.oreilly.co.jp/books/9784873118369/

## How to run

```
docker build -t zerokara_deeplearning .
docker run -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it zerokara_deeplearning jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
