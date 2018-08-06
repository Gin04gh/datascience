# stock_price_data_warehouse

## Description

## How to run

```
docker build -t stock_price_data_warehouse .
docker run -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it stock_price_data_warehouse jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
