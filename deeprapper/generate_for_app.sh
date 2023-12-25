#!/bin/bash

python generate_for_app.py \
                      --device '3' \
                      --length 128 \
                      --batch_size 8 \
                      --nsamples 1 \
                      --temperature 1 \
                      --topk 8 \
                      --beam_samples_num 1 \
                      --topp 0 \
                      --repetition_penalty 1. \
                      --save_samples \
                      --save_samples_dir 'samples_save_dir' \
                      --samples_sign 'sample_name' \
                      --model_dir 'model/deeprapper-model' \
                      --model_config 'config.json' \
                      --enable_beat \
                      --enable_final \
                      --enable_sentence \
                      --enable_relative_pos \
                      --prefix '我长大的地方像一个简朴的寨' \
                      --reverse \
                      --pattern 'beam' \
                      --beam_sample_select_sg 'sample' \
                      --beam_cut_temperature 10 \
                      --rhyme_count 4 \
                      --rhyme_prob_bound 1.0 \
                      --rhyme_alpha 0.95 \