#!/bin/sh
echo "$CONDA/bin" >> "$GITHUB_PATH"
conda activate torch_base

python build.py

dvc get https://github.com/nclgbd/ML-Data-Configurations.git test_data/test_data.zip -o --verbose --show-url
dvc pull --verbose
unzip test_data.zip -d test_data/
rm -rf test_data.zip

unzip data/data.zip
