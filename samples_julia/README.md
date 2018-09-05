# samples_julia

## Description

juliaによるデータサイエンス関連のサンプルコード集.  
基本的にjupyter notebookで実行プログラムと結果を保存する.  

## How to run

```
docker build -t samples_julia docker/.
docker run -p 8888:8888 -v `pwd`:/home/jovyan/work samples_julia
```
