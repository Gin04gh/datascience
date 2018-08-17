# open_ai

## Description

強化学習のサンプルコード集.
環境は「Open AI Gym」を使う.

https://gym.openai.com/

基本的にjupyter notebookで実行プログラムと結果を保存する.  
各ノートブックにはPythonのバージョンとライブラリバージョンを確認できるよう以下の実行セルを含めること.

Pythonバージョン
```
!python --version
```

ライブラリバージョン
```
!pip freeze
```

## How to run

```
docker build -t open_ai .
docker run -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it open_ai jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
