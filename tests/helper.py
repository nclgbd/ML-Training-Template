import pytest
import os
import json

from pytorch_vision_utils.Utilities import DataVisualizationUtilities, TrainingUtilities
from pytorch_vision_utils.Utilities import clear_dirs, time_to_predict


def build_env():
    """
    Creates all of the necessary folders
    """    
    with open("parameters.json", "r") as f:
        print("Loading parameters...\n")
        params = dict(json.load(f))
        
        DATA_DIR = params["DATA_DIR"]
        TEST_DIR = params["TEST_DIR"]
        MODEL_DIR = params["MODEL_DIR"]
        MEDIA_DIR = params["MEDIA_DIR"]
        INC_DIR = params["INC_DIR"]
            
    DIRS = [DATA_DIR, TEST_DIR, MODEL_DIR, MEDIA_DIR, INC_DIR]


    for dirs in DIRS:
        clear_dirs(dirs)
        print("Creating:", dirs)
        os.makedirs(dirs, exist_ok=True)