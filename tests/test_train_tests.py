import os
import json
import sys
import torch
import zipfile

from mdutils.mdutils import MdUtils

from pytorch_vision_utils.Utilities import TrainingUtilities
from pytorch_vision_utils.Utilities import clear_dirs, build


# Default directory names
with open("parameters.json", "r") as f:
    print("Loading parameters...\n")
    params = dict(json.load(f))
    
    DATA_DIR = params["DATA_DIR"]
    TEST_DIR = params["TEST_DIR"]
    MODEL_DIR = params["MODEL_DIR"]
    MEDIA_DIR = params["MEDIA_DIR"]
    INC_DIR = params["INC_DIR"]
    
    print("Loading parameters complete!")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
train_utils = TrainingUtilities(data_dir=TEST_DIR, model_dir=MODEL_DIR, model_name="mobilenetv2")


def run_epoch():
    results = tuple() # empty tuple
    results = train_utils.train(model_name="mobilenetv2", model_path=MODEL_DIR, inc_path=INC_DIR, media_dir=MEDIA_DIR, show_graphs=False, dry_run=False, debug=True, max_epoch=1)
    return 0


def test_run_epoch():
    assert run_epoch() == 0