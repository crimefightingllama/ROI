# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 18:25:32 2023

@author: shuyu
"""

import os
import gc
folder = r"C:\Users\Shuyu\OneDrive - Imperial College London\4th Year\MSci Project\ROI\csv"

os.chdir(folder)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["figure.figsize"] = (20,17)
plt.rcParams["xtick.labelsize"] = 15
plt.rcParams["ytick.labelsize"] = 15
plt.rcParams["axes.labelsize"] = 12

path = folder + "\\" + "SD.csv"
densities =pd.read_csv(path,sep=',')
densities.head()
df = densities[["file","density"]]
df.head()
pathopath = folder + '\\' + "Patho.csv"
patho = pd.read_csv(pathopath, sep = ',')
patho.head()
df_patho = patho[["Biopsy","ROI1 Density","ROI2 Density"]]

plt.figure()
# df.plot.scatter("file", "density")
# df_patho.plot.scatter("Biopsy", "ROI1 Density")]
plt.scatter(df["file"],df["density"], label = 'StarDist')
plt.scatter(df_patho["Biopsy"],df_patho["ROI1 Density"],label = 'ROI1')
plt.scatter(df_patho["Biopsy"],df_patho["ROI2 Density"],label = 'ROI2')
plt.xlabel("image")
plt.ylabel(r'cell density $({µm}^{-2})$')
plt.legend()
plt.savefig("roi_densities.png", dpi = 200)