#!/bin/bash
./build
python -m pytorch_vision_utils.train --model_name="mobilenetv2" --debug="True"