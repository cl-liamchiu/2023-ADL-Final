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
gdown https://drive.google.com/uc?id=1pHffO_PqqZUJLZHB9awhLjPYLNbcai4e
unzip adl_final_data.zip && rm adl_final_data.zip
```

## Prefix
⚠️ White space are not allowed


## Streamlit
```
pip install streamlit==1.29.0
streamlit run app.py
```