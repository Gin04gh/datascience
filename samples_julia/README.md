# samples_julia

## Description

juliaによるデータサイエンス関連のサンプルコード集.  
基本的にjupyter notebookで実行プログラムと結果を保存する.  

## How to run

```
docker build -t samples_julia docker/.
docker run -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it samples_julia jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
