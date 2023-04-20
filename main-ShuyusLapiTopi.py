# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 13:53:43 2023

@author: shuyu
"""
import os
folder = r"C:\Users\Shuyu\OneDrive - Imperial College London\4th Year\MSci Project\ROI"

os.chdir(folder)
import pandas as pd
from densitymap import densitymap
import matplotlib.pyplot as plt
import numpy as np


# plt.rcParams["figure.dpi"] = 200
plt.rcParams["figure.figsize"] = (20,17)

plt.rcParams["xtick.labelsize"] = 15
plt.rcParams["ytick.labelsize"] = 15
plt.rcParams["axes.labelsize"] = 12


#%%
tsvfolder = folder + "\\tsvfiles"  
dir_list = os.listdir(tsvfolder)

def annotate(file):
    # file = "\measurements.tsv"
    # path = folder + file
    data=pd.read_csv(file,sep='\t')
    data.head()
    df = data.iloc[:,2:4]
    df.head()
    
    x = 'Centroid X µm'
    y = 'Centroid Y µm'
    DM = densitymap.DM(df[x].to_numpy(),df[y].to_numpy(),100,10)
    DM.plot()
    plt.savefig("densitymap" + file[:4] + ".png", dpi = 400)
for slide in dir_list:
    annotate(slide)
    print(slide, ' done')


#%%
np.random.seed(6)
x = 20*np.random.random_sample(150)
y = 17*np.random.random_sample(150)
slide1 = densitymap.DM(x, y, 1, 5)
slide1.plot()
plt.savefig("testplot.png", dpi = 200)