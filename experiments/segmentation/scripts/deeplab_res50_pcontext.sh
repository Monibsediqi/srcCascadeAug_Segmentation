#!/usr/bin/env bash

#train
python --gpu 0 1 2 3  train.py --dataset pcontext \
    --model deeplab --jpu [JPU|JPU_X] --aux --aux-weight 0.4 \
    --backbone resnet50 --checkname deeplab_res50_pcontext

#test [single scale]
python --gpu 0 1 2 3  test.py --dataset pcontext \
    --model deeplab --jpu [JPU|JPU_X] --aux --aux-weight 0.4 \
    --backbone resnet50 --resume {MODEL_NAME} --split testval

#test [multi-scale]
python --gpu 0 1 2 3  test.py --dataset pcontext \
    --model deeplab --jpu [JPU|JPU_X] --aux --aux-weight 0.4 \
    --backbone resnet50 --resume {MODEL_NAME} --split testval --ms

#predict [single_scale]
python --gpu 0 1 2 3  test.py --dataset pcontext \
    --model deeplab --jpu [JPU|JPU_X] --aux --aux-weight 0.4 \
    --backbone resnet50 --resume {MODEL_NAME} --split val --mode test

#predict [multi-scale]
python --gpu 0 1 2 3  test.py --dataset pcontext \
    --model deeplab --jpu [JPU|JPU_X] --aux --aux-weight 0.4 \
    --backbone resnet50 --resume {MODEL_NAME} --split val --mode test --ms
