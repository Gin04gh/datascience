# bayes_tennis

build docker container,

```
docker build -t bayes_tennis docker/.
```

run scripts,

Step 1/5 -- preprocess.py

```
docker run -v `pwd`:/home/jovyan/work -w=/home/jovyan/work --rm -it bayes_tennis python preprocess.py
```

Step 2/5 -- analyze_strength.py

```
docker run -v `pwd`:/home/jovyan/work -w=/home/jovyan/work --rm -it bayes_tennis python analyze_strength.py
```

Step 3/5 -- analyze_strength_ts.py

```
docker run -v `pwd`:/home/jovyan/work -w=/home/jovyan/work --rm -it bayes_tennis python analyze_strength_ts.py
```

Step 4/5 -- run jupyter notebook

```
docker run -v `pwd`:/home/jovyan/work -w=/home/jovyan/work -p 8888:8888 --rm -it bayes_tennis jupyter notebook --allow-root
```

Step 5/5 -- access jupyter notebook

open <localhost:8888> with internet browser, and open `notebook.ipynb`


