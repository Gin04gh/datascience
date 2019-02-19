# latex

how to use

1. tex -> dvi using `uplatex`

```
docker run --rm -v $PWD:/workdir paperist/alpine-texlive-ja uplatex ***.tex
```

2. dvi -> pdf using dvipdfmx

```
docker run --rm -v ${PWD}:/workdir paperist/alpine-texlive-ja dvipdfmx ***.dvi
```
