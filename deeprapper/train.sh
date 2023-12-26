#!/bin/bash

python train.py \
  --device '0,1' \
  --stride 1024 \
  --model_config 'config/model_config_small.json' \
  --model_dir '蛋堡2' \
  --root_path 'data/lyrics/' \
  --raw_data_dir 'lyrics_samples/' \
  --batch_size 2 \
  --epochs 10 \
  --enable_final \
  --enable_sentence \
  --enable_relative_pos \
  --enable_beat \
  --reverse \
  --model_sign 'samples' \
  --beat_mode 0 \
  --tokenize \
  --raw  \
  --pretrained_model /home/guest/r12922121/ADL_2023_NTU/final/deeprapper/2023-ADL-Final/deeprapper/model/deeprapper \