import sys
import os
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import open3d as o3d
from scipy.spatial import Delaunay
import itertools

data_folder="/p/jmz9sadprojects/ml-project/data/modelnet/modelnet40_normal_resampled/airplane/"
#for i in range(726):
for i in range(6):
	dataset="airplane_%04d.txt"%i
	print(data_folder+dataset)
	pcd = o3d.io.read_point_cloud(data_folder+dataset)
	o3d.visualization.draw_geometries([pcd])
