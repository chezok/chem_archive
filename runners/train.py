import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
import os
import numpy as np
import random
import logging
from tqdm import tqdm


class BaseTrainer():
    def __init__(self):
        