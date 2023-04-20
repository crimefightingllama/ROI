# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 13:53:43 2023

@author: shuyu
"""
import os
import gc
folder = r"C:\Users\Shadow\OneDrive - Imperial College London\4th Year\MSci Project\ROI"

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
tsvfolder = folder + "\\tsvfiles\\preprocessed\\Cell detection"  
dir_list = os.listdir(tsvfolder)
print(dir_list)
#%%
def annotate(file):
    # file = "\measurements.tsv"
    path = tsvfolder +"\\" + file
    data=pd.read_csv(path,sep='\t')
    # data = data.loc[data['Class']=='Positive']
    # print(data.head())
    df = data.iloc[:,1:3]
    # print(df.head())
    
    x = 'Centroid X µm'
    y = 'Centroid Y µm'
    # name = file[9:13]
    name = file[11:15]

    DM = densitymap.DM(df[x].to_numpy(),df[y].to_numpy(),100,10,name)
    DM.plot()
    plt.savefig("preprocessed_" + name + ".png", dpi = 400)
    plt.clf()
    plt.close("all")
#%%
for slide in dir_list:
    annotate(slide)
    print(slide, ' done')
    gc.collect()
#%%
slide = dir_list[1]
annotate(slide)

#%%
np.random.seed(6)
x = 20*np.random.random_sample(150)
y = 17*np.random.random_sample(150)
slide1 = densitymap.DM(x, y, 1, 5)
slide1.plot()
plt.savefig("testplot.png", dpi = 200)