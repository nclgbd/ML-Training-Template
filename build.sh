#!/bin/sh
python build.py
dvc get https://github.com/nclgbd/ML-Data-Configurations.git data/data.zip -o data/
unzip data/data.zip
dvc pull
