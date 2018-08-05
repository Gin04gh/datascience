# pilotnet_visualbackprop

## Description

PilotNet + Visual back prop.  
See, 
* https://arxiv.org/abs/1704.07911
* https://devblogs.nvidia.com/explaining-deep-learning-self-driving-car/

Using dataset is udacity self-driving dataset.  
See,
* https://github.com/udacity/self-driving-car
* https://github.com/rwightman/udacity-driving-reader

## How to run

```
docker build -t pilotnet_visualbackprop .
```

```
docker run --runtime=nvidia -v `pwd`:/tmp/work -w=/tmp/work -p 8888:8888 --rm -it pilotnet_visualbackprop jupyter notebook --no-browser --ip=* --notebook-dir=/tmp/work --allow-root
```
