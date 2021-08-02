import os
import json
from helper import build_env

from pytorch_vision_utils.Utilities import DataVisualizationUtilities, TrainingUtilities
from pytorch_vision_utils.Utilities import clear_dirs, time_to_predict

build_env()


def train_tests():
    return 0

# # DIRECTORY NAMES
# cwd = os.getcwd()
# DATA_DIR = str(os.path.join(cwd, "data"))
# TEST_DIR = str(os.path.join(cwd, "test_data"))
# MODEL_DIR = str(os.path.join(cwd, "saved_models"))
# MEDIA_DIR = str(os.path.join(cwd, 'media'))
# INC_DIR = str(os.path.join(cwd, 'incorrect_images'))
# MODEL_NAME = ""

# train_utils = TrainingUtilities(data_dir=DATA_DIR, model_dir=MODEL_DIR, model_name=MODEL_NAME, mode="train")
# dataviz_utils = DataVisualizationUtilities()
# clear_dirs(INC_DIR)

# print(MODEL_DIR)
# print(DATA_DIR)
# print(MEDIA_DIR)

# train_utils.set_model_parameters(model_name=MODEL_NAME, mode="train")
# dataviz_utils.display_dataset(train_utils)

# train_utils.train(model_name="mobilenetv2", model_path=MODEL_DIR, inc_path=INC_DIR)

# return train_utils.load_weights(model_name="mobilenetv2", 
#                                 model_weights_path=MODEL_DIR, 
#                                 mode='test', 
#                                 debug=False)
