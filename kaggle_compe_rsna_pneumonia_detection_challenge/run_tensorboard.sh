docker run --runtime=nvidia -it --rm -v $(pwd):/outdir -p 6006:6006 kaggle_compe_rsna_pneumonia_detection_challenge tensorboard --logdir=/outdir/result/
