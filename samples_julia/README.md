# samples_julia

## 概要

juliaによるデータサイエンス関連のサンプルコード集.  
基本的にjupyter notebookで実行プログラムと結果を保存する.  

## 実行

```
docker build -t samples_julia .
docker run -p 8888:8888 -v `pwd`:/home/jovyan/work samples_julia
```
