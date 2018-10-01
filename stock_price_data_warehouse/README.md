# stock_price_data_warehouse

## Description

Using dataset is

* http://www.geocities.co.jp/WallStreet-Stock/9256/
* http://www.geocities.co.jp/WallStreet-Stock/9256/data2017.htm

## How to run

```
docker build -t stock_price_data_warehouse docker/.
docker run -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it stock_price_data_warehouse jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
