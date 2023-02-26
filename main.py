# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 13:53:43 2023

@author: shuyu
"""
import os
folder = r"C:\Users\Shadow\OneDrive - Imperial College London\4th Year\MSci Project\SpyderCode"

os.chdir(folder)
import pandas as pd
from densitymap import densitymap
import matplotlib.pyplot as plt

plt.rcParams["figure.dpi"] = 200
plt.rcParams["figure.figsize"] = (200,170)

plt.rcParams["xtick.labelsize"] = 15
plt.rcParams["ytick.labelsize"] = 15
plt.rcParams["axes.labelsize"] = 15
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))



file = "\measurements.tsv"
path = folder + file
data=pd.read_csv(path,sep='\t')
data.head()
df = data.iloc[:,2:4]
df.head()

x = 'Centroid X µm'
y = 'Centroid Y µm'
plt.figure(1)
plt.xlabel('µm')
plt.ylabel('µm')
# plt.plot(df[x],df[y],'o',markersize=0.5,fillstyle = 'full')
# plt.savefig("coords.png", dpi = 200)
slide = densitymap.DM(df[x],df[y],100)
slide.plot()
plt.savefig("densitymap1.png", dpi = 200)
