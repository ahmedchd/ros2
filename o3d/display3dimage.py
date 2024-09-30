import open3d as o3d
import numpy as np

# Create a simple point cloud
points = np.random.rand(100, 3)  # 100 random 3D points
colors = np.random.rand(100, 3)   # Random colors for each point

# Create an Open3D point cloud object
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
pcd.colors = o3d.utility.Vector3dVector(colors)

# Visualize the point cloud
#o3d.visualization.draw_geometries([pcd], window_name="Point Cloud", width=800, height=600, left=50, top=50)
o3d.visualization.draw_geometries([pcd])
