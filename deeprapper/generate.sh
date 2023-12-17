#!/bin/bash

python generate.py \
                      --device '0' \
                      --length 300 \
                      --batch_size 1 \
                      --nsamples 1 \
                      --temperature 0.8 \
                      --topk 6 \
                      --topp 0.15 \
                      --repetition_penalty 1. \
                      --save_samples \
                      --save_samples_dir 'output' \
                      --samples_sign 'sample_name' \
                      --model_dir '/home/guest/r12922121/ADL_2023_NTU/final/deeprapper/2023-ADL-Final/deeprapper/softlipa/lyrics/lyrics_samples_reverse/samples/final_model' \
                      --model_config 'config.json' \
                      --enable_final \
                      --enable_sentence \
                      --enable_relative_pos \
                      --prefix '這是三分鐘之內的第五通' \
                      --enable_beat \
                      --with_beat \
                      --beat_mode 0 \
                      --tempo 2 \
                      --reverse \
                      --pattern 'beam' \
                      --beam_sample_select_sg 'sample' \
                      --beam_cut_temperature 10 \
                      --dynamic_rhyme \
                      --rhyme_count 3 \
                      --rhyme_prob_bound 1.0 \
                      --rhyme_alpha 0.95

