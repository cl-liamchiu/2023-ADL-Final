# 2023-ADL-Final

## Environment

CUDA 11.4

```bash!
conda create -n adl-final python=3.9.18
conda activate adl-final
pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
```

## Data
Please download by gdown
```
gdown https://drive.google.com/uc?id=1_-wJWI5fbTqEVM8OSsHDQZ6xBWBzoaC-
unzip lyrics.zip && rm lyrics.zip
```

## Prefix
⚠️ White spaces are not allowed

## Fine-tune
1. Ensure the singer folder is placed within the data/lyrics/lyrics_samples/raw directory to access the required data.
    ```
        Here's the hierarchical architecture of the dataset.:
        ├── data
        └── lyrics
            └── lyrics_samples
                └── raw
                    └── singer01
                        └── album01
                            ├── song01
                            │   ├── lyric_with_beat_global.txt
                            │   └── 
    ```
    Note that I ignore the album hierarchy, so all songs are in the same folder.

2. I've changed some files, so please remember to update the data.
    - train.py
    - prepare_train_data.py
    

3. Training:
    1. you need to modify a few parameters:
        - model_dir (output model path)
        - pretrained_model (downloaded from original github)
    2. (Optional)
        - epochs
        - batch_size

    ```
    bash train.sh
    ```

4. Generate
    1. you need to modify a few parameters:
        - model_dir (output model path)
    2. (Optional)
        - epochs
        - batch_size
        - prefix
        - temp
        - topk
        - topp
    ```
    bash generate.sh
    ```
