import numpy as np
import scipy.spatial as spatial
import matplotlib.pyplot as plt
plt.rcParams["figure.dpi"] = 200



np.random.seed(6)
points = np.array([(1, 2), (3, 4), (4, 5), (100,100)])
coords = zip(*points)
x = 10*np.random.random_sample(1000)
y = 10*np.random.random_sample(1000)
# points = np.array([1, 2], [3, 4], [4, 5], [100,100])
tree = spatial.KDTree(np.stack((x,y),1))
radius = 1

neighbors = tree.query_ball_tree(tree, radius)
# print(neighbors)
# [[0, 1], [0, 1, 2], [1, 2], 


frequency = np.fromiter(map(len, neighbors), dtype = float)
# print(frequency)
# [2 3 2 1]
density = frequency/radius**2
# print(density)
# [ 0.22222222  0.33333333  0.22222222  0.11111111]
plt.figure()
plt.tricontourf(x,y,density,levels = 10)
plt.colorbar()
# plt.pcolormesh(points,density)
plt.plot(x,y,'.',markersize = 1,color = 'k')
# plt.contour(x,y,frequency)
maxi = np.where(frequency == max(frequency))[0][0]
densest = plt.Circle((x[maxi],y[maxi]),1,color = 'r', fill = False)
mini = np.where(frequency == min(frequency))[0][0]
sparsest = plt.Circle((x[mini],y[mini]),1,color = 'r', fill = False)
plt.text(x[maxi],y[maxi],'1',color = 'w')
plt.gca().add_patch(densest)
# plt.gca().add_patch(sparsest)
plt.gca().set_aspect('equal')
#%%
# plt.plot([1,2,3],[2,5,1])
coord = np.array([[1,2,3],[4,5,6]])
plt.plot(coord)
