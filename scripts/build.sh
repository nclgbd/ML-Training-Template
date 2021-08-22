#!/bin/sh
echo "$CONDA/bin" >> "$GITHUB_PATH"
conda activate torch_base

python build.py
dvc get https://github.com/nclgbd/ML-Data-Configurations.git data/data.zip -o data/
dvc pull
unzip data/data.zip
