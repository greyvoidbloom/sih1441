import json
import os
import re
from scriptfiles.packageloader import LOADER
dependecyload = LOADER(['pandas','numpy'])
import pandas as pd
import numpy as np

PATH = os.path.dirname(os.path.realpath(__file__))
