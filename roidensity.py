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
plt.rcParams["figure.figsize"] = (20,9)
plt.rcParams["xtick.labelsize"] = 15
plt.rcParams["ytick.labelsize"] = 15
plt.rcParams["axes.labelsize"] = 25

path = folder + "\\" + "SD.csv"
densities =pd.read_csv(path,sep=',')
densities.head()
df = densities[["file","density"]]
df.head()
pathopath = folder + '\\' + "Patho.csv"
patho = pd.read_csv(pathopath, sep = ',')
patho.head()
df_patho = patho[["Biopsy","ROI1 Density","ROI2 Density"]]

fig, ax = plt.subplots()
# df.plot.scatter("file", "density")
# df_patho.plot.scatter("Biopsy", "ROI1 Density")]
# plt.scatter(df["file"],df["density"], label = 'StarDist')
# plt.scatter(df_patho["Biopsy"],df_patho["ROI1 Density"],label = 'ROI1')
# plt.scatter(df_patho["Biopsy"],df_patho["ROI2 Density"],label = 'ROI2')
pred = ax.boxplot(df["density"],positions = [1],patch_artist = True, vert = 0, boxprops=dict(facecolor="C3"))
roi1 = ax.boxplot(df_patho["ROI1 Density"], positions = [2],patch_artist = True,vert = 0)
roi2 = ax.boxplot(df_patho["ROI2 Density"], positions = [3], patch_artist = True,vert = 0)
# plt.xlabel("image")
ax.set_yticklabels(['predicted','pathologist ROI1', 'pathologist ROI2'], size = 25)
plt.xlabel(r'cell density $({µm}^{-2})$')
plt.legend()
plt.show()
fig.savefig("roi_densities.png", dpi = 200)