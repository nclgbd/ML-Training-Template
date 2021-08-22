#!/bin/bash
ls -la

dvc get https://github.com/nclgbd/ML-Data-Configurations.git test_data/test_data.zip -o 
dvc pull
unzip test_data.zip -d test_data/
rm -rf test_data.zip

pytest -v -s