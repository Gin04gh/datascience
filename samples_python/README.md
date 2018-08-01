# samples_python

```
docker build -t samples_python .
docker run -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it samples_python jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
