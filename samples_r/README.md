# samples_r

## Description

Rによるデータサイエンス関連のサンプルコード集.  
基本的にjupyter notebookで実行プログラムと結果を保存する.  
各ノートブックにはRバージョンを確認できるよう以下の実行セルを含めること.

```
sessionInfo()
```

## How to run

```
docker build -t samples_r .
docker run -p 8888:8888 -v `pwd`:/home/jovyan/work samples_r
```
