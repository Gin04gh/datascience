# latex

## build

```
docker build -t latex docker/,
```

## how to use

1. tex -> dvi using `uplatex`

```
docker run --rm -v $PWD:/workdir latex uplatex ***.tex
```

2. dvi -> pdf using dvipdfmx

```
docker run --rm -v ${PWD}:/workdir latex dvipdfmx ***.dvi
```
