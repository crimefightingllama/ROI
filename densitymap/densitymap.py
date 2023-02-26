# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 16:25:54 2023

@author: shuyu
"""
import numpy as np
import scipy.spatial as spatial
import matplotlib.pyplot as plt
plt.rcParams["figure.dpi"] = 200

class DM():
    def __init__(self, x,y,r):
        self.x = x
        self.y = y
        self.tree = spatial.KDTree(np.stack((x,y),1))
        self.radius = r
        self.neighbors = self.tree.query_ball_tree(self.tree, self.radius)
    
        self.frequency = np.fromiter(map(len, self.neighbors), dtype = float)
        self.density = self.frequency/self.radius**2
        
    def plot(self):
        plt.figure()
        plt.tricontourf(self.x,self.y,self.density,levels = 10)
        plt.colorbar()
        # plt.pcolormesh(points,density)
        # plt.plot(self.x,self.y,'.',markersize = 1,color = 'k')
        # plt.contour(x,y,frequency)
        maxi = np.where(self.frequency == max(self.frequency))[0][0]
        densest = plt.Circle((self.x[maxi],self.y[maxi]),self.radius,color = 'r', fill = False)
        # mini = np.where(frequency == min(frequency))[0][0]
        # sparsest = plt.Circle((x[mini],y[mini]),1,color = 'r', fill = False)
        plt.gca().add_patch(densest)
        # plt.gca().add_patch(sparsest)
        plt.gca().set_aspect('equal')
        plt.xlabel('µm')
        plt.ylabel('µm')
