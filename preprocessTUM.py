
import numpy as np
import pandas as pd
from plyfile import PlyData, PlyElement
import open3d as o3d

# ply file
def read_ply_with_parameters(path):
    '''
    :param path: path to .ply(onlu) file
    :return: return point cloud data in array
    '''
    plydata = PlyData.read(path)
    data = plydata.elements[0].data
    print(plydata.elements)
    data_pd = pd.DataFrame(data)
    data_np = np.zeros(data_pd.shape, dtype=float)
    property_names = data[0].dtype.names
    for i, name in enumerate(property_names):
        print(name)  # print parameters
        data_np[:, i] = data_pd[name]
    return data_np[:, 0:3], data_np[:, 3]


if __name__ == "__main__":

    path = "/home/ge75jek/data/TUM-MLS/small/semantic_raw/mls2016_8class_20cm_ascii_area1.ply"
    point, label = read_ply_with_parameters(path)
    np.savetxt('/home/ge75jek/data/TUM-MLS/small/semantic_raw/mls2016_8class_20cm_ascii_area1.labels', label.astype(int),fmt='%i')   # X is an array
    pcd = o3d.io.read_point_cloud(path)
    o3d.io.write_point_cloud("/home/ge75jek/data/TUM-MLS/small/semantic_raw/mls2016_8class_20cm_ascii_area1.pcd", pcd)

