import open3d as o3d
import numpy as np

a = np.load("data.npy")

# print(o3d.__version__)

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(a[:, :3])
pcd.colors = o3d.utility.Vector3dVector(a[:,3:6]/255)


downpcd = pcd.voxel_down_sample(0.02)

o3d.visualization.draw_geometries([downpcd])


import open3d.ml as ml3d