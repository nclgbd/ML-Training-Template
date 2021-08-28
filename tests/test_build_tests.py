import os
import sys
import torch
import json

from pytorch_vision_utils.Utilities import DataVisualizationUtilities, TrainingUtilities
from pytorch_vision_utils.Utilities import clear_dirs, time_to_predict


def build_test():
    # Default directory names
    print("Creating folders...")
    with open("parameters.json", "r") as f:
        print("Loading parameters...\n")
        params = dict(json.load(f))
        
        DATA_DIR = params["DATA_DIR"]
        TEST_DIR = params["TEST_DIR"]
        MODEL_DIR = params["MODEL_DIR"]
        MEDIA_DIR = params["MEDIA_DIR"]
        INC_DIR = params["INC_DIR"]


    print("Initializing TrainingUtilities class...")
    TrainingUtilities(data_dir=TEST_DIR, model_dir=MODEL_DIR, model_name="mobilenetv2")
    TrainingUtilities(data_dir=TEST_DIR, model_dir=MODEL_DIR, model_name="xception")

    print("Initializing DatavisualizationUtilities class...")
    DataVisualizationUtilities()
    
    return 0


def test_build_test():
    assert build_test() == 0
