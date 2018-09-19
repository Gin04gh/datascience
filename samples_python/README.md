# samples_python

## Description

Pythonによるデータサイエンス関連のサンプルコード集.  
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
docker build -t samples_python docker/.
docker run -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it samples_python jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```

if use Plotly, add jupyter notebook option `--NotebookApp.iopub_data_rate_limit=1.0e10`.
