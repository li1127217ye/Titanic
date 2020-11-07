# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 08:49:08 2020

@author: PC-4
"""

# %% import
from pandas_profiling import ProfileReport

import numpy as np
import pandas as pd

# from warnings import filterwarnings
# filterwarnings("ignore")

# %% data
df = pd.read_csv("train.csv", index_col="PassengerId")

# %% Overall
profile = ProfileReport(df, minimal=False, progress_bar=False, title="Overall")
profile.to_file("Overall.html")
