# e-stat

## Description

e-stat のデータを使った分析.  
https://www.e-stat.go.jp/

## How to run

Set e-stat app id file `.appid` is

```
{
	"appid": "**************************"
}
```

Then, 

```
docker build -t e-stat docker/.
docker run -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it e-stat jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
