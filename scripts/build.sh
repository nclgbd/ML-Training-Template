#!/bin/bash --login

mkdir -p /workdir/media/ /workdir/incorrect_images/ /workdir/saved_models/
dvc get https://github.com/iterative/dataset-registry tutorials/versioning/data.zip
unzip data.zip
mv data/train .
mv data/validation .

# Remove the directories since they're not needed anymore
rm -f data.zip
rm -rf data/train
rm -rf data/validation
