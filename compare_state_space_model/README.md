# compare_state_space_model

## Description

Compare state space model by statsmodels, PyStan, PyMC3, Edward.

## How to run

```
docker build -t compare_state_space_model .
docker run -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it compare_state_space_model jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
