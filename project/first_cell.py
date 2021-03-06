%reload_ext autoreload
%autoreload 2

from paths import RAW_PATH, TREAT_PATH, OUTPUT_PATH, FIGURES_PATH, MODEL_PATH

import os
from copy import deepcopy
import numpy as np
import pandas as pd
pd.options.display.max_columns = 999

import warnings
warnings.filterwarnings('ignore')

# Plotting
import plotly
import plotly.graph_objs as go
import cufflinks as cf
plotly.offline.init_notebook_mode(connected=True)

# Network analysis
import networkx as nx
import operator
# import yaml

cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)

from utils import *

colorscale = ['#025951', '#8BD9CA', '#BF7F30', '#F2C124', '#8C470B', '#DFC27D']