# bayes_tennis

build docker container,

```
docker build -t bayes_tennis docker/.
```

run scripts,

Step 1/3

science notebook docker,
```
docker run -v `pwd`:/home/jovyan/work -w=/home/jovyan/work -p 8888:8888 --rm -it bayes_tennis jupyter notebook --no-browser --ip=* --notebook-dir=/home/jovyan/work --allow-root
```

keggle dokcer,
```
docker run -v `pwd`:/home -w=/home -p 8888:8888 --rm -it bayes_tennis jupyter notebook --no-browser --ip=* --notebook-dir=/home --allow-root
```

Step 2/3

access [server ip adress]:8888

Step 3/3

open `analyze.ipynb`
and 
