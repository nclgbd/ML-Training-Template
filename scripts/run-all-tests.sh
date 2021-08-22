#!/bin/bash
echo "$CONDA/bin" >> "$GITHUB_PATH"
conda activate torch_base
ls -la

dvc get https://github.com/nclgbd/ML-Data-Configurations.git data/data.zip -o 
dvc pull
unzip data.zip -d data/
rm -rf data.zip

pytest -v -s