import numpy as np
import matplotlib.pyplot as plt
import torch
import os
import sys
import seaborn as sns
import json

from datetime import datetime
from PIL import Image
from statistics import mean
from torch import nn, optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm

from pytorch_vision_utils.Utilities import clear_dirs, time_to_predict, DataVisualizationUtilities, TrainingUtilities

print("Finished imports")
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print("Using: ", device)

sys.exit(0)