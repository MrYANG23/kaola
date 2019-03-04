import torch
import torch.utils.data as data
from glob import glob
import os,math,random
from os.path import *
from scipy.misc import imread,imsave
import numpy as np
from PIL import Image
from path import Path
root='/home/yh/shujuji/FlyingChairs_release/data'
images=sorted(glob(join(root,'*.ppm')))
flow_list=sorted(glob(join(root,'*.flo')))
lenght=len(flow_list)
# print('images_lenght:',len(images))
# print('images_[0:10]:',images[0:10])
# print(lenght)
# --------------debug:
# images_lenght: 45744
# images_[0:10]: ['/home/yh/shujuji/FlyingChairs_release/data/00001_img1.ppm', '/home/yh/shujuji/FlyingChairs_release/data/00001_img2.ppm', '/home/yh/shujuji/FlyingChairs_release/data/00002_img1.ppm', '/home/yh/shujuji/FlyingChairs_release/data/00002_img2.ppm', '/home/yh/shujuji/FlyingChairs_release/data/00003_img1.ppm', '/home/yh/shujuji/FlyingChairs_release/data/00003_img2.ppm', '/home/yh/shujuji/FlyingChairs_release/data/00004_img1.ppm', '/home/yh/shujuji/FlyingChairs_release/data/00004_img2.ppm', '/home/yh/shujuji/FlyingChairs_release/data/00005_img1.ppm', '/home/yh/shujuji/FlyingChairs_release/data/00005_img2.ppm']
# 22872

images_list=[]
for i in range(lenght):
    im1=images[2*i]
    im2=images[2*i+1]
    images_list+=[[im1,im2]]
print(len(images_list))
print('--------splittext:',splitext(images_list[0][0]))


def read_gen(file_name):
    ext=splitext(file_name)[-1]
    if ext =='.png' or ext =='.jpeg' or ext =='.ppm ' or ext== '.jpg':
        im=imread(file_name)#imread_ndarray
        if im.shape[2]>3:
            return im[:,:,:3]
        else:
            return im
    elif ext =='.bin' or ext =='.raw':
        return np.load(file_name)
    return []

def readflow(file_name):
    with open(file_name,'rb') as f:
        magic=np.fromfile(f,np.float32,count=1)
        print('-------------my_magic:',magic)
        if 202021.25 !=magic:
            print('it is error with .flo file')
            return None
        else:
            w=np.fromfile(f,np.int32,count=1)[0]

            h=np.fromfile(f,np.int32,count=1)[0]
            print('reading %d x %d flo file\n'%(w,h))

            data=np.fromfile(f,np.float32,count=2*int(w)*int(h))
            return np.resize(data,(int(w),int(h),2))



def load_flo(path):
    with open(path, 'rb') as f:

        magic = np.fromfile(f, np.float32, count=1)
        assert(202021.25 == magic),'Magic number incorrect. Invalid .flo file'
        h = np.fromfile(f, np.int32, count=1)[0]
        w = np.fromfile(f, np.int32, count=1)[0]
        data = np.fromfile(f, np.float32, count=2*w*h)
    # Reshape data into 3D array (columns, rows, bands)
    data2D = np.resize(data, (w, h, 2))
    return data2D

def flow2rgb(flow_map, max_value):#
    flow_map_np = flow_map
    _,h, w = flow_map_np.shape
    print('--------------h',h,'------------------w',w)
    flow_map_np[:,(flow_map_np[0] == 0) & (flow_map_np[1] == 0)] = float('nan')
    rgb_map = np.ones((3,h,w)).astype(np.float32)
    print('-------------------rgb_map',rgb_map.shape)
    if max_value is not None:
        normalized_flow_map = flow_map_np / max_value
    else:
        normalized_flow_map = flow_map_np / (np.abs(flow_map_np).max())
    rgb_map[0] += normalized_flow_map[0]
    rgb_map[1] -= 0.5*(normalized_flow_map[0] + normalized_flow_map[1])
    rgb_map[2] += normalized_flow_map[1]
    return rgb_map.clip(0,1)


files='/home/yh/shujuji/FlyingChairs_release/data/00001_img1.ppm'
im=read_gen(files)
ims=imread('/home/yh/shujuji/FlyingChairs_release/data/00001_img1.ppm')
print(im)
print(ims.shape)


#
# flow_file='/home/yh/shujuji/out.flo'
# flow_file2='/home/yh/下载/pytorch-unflow-master/out.flo'
#
# flow_array=load_flo(flow_file2)
# flow_arrays=flow_array.transpose((2,0,1))
#

#
# c=Image.fromarray(flow_array,mode='RGB')
# c.show()

#
# print('-------------',flow_arrays.shape)
# print('----------------',type(flow_arrays))
# flow_2_rgb=flow2rgb(flow_arrays,None)
# print(flow_2_rgb.shape)
# # print(flow_2_rgb)
# to_save = (flow_2_rgb * 255).astype(np.uint8).transpose(1,2,0)#乘以255并转换为整形后交换通道
# print('')
#
#
# c=Image.fromarray(to_save,mode='RGB')#将数组转换为rgb图
# c.show()

# print('-----------------to_save',to_save)
# imsave(r'/home/yh/shujuji/data_stereo_flow/flow', to_save)
# #nilaninnknnalkdfadniansdfabubububububfgs
# flow_array=readflow(flow_file)
# print(flow_array.shape)
# print('flow_array:',flow_array)
#

#
# im=imread(r'/home/yh/shujuji/FlyingChairs_release/data/00001_img1.ppm')
# print(im.shape)#(384,512,3)
# print(type(im))#ndarray


# data_folder='/home/yh/shujuji/data_stereo_flow'
# data_folder_path=Path(data_folder)
# print(data_folder_path)
#
# new_data_folder_path=data_folder_path/'flow'
# print(new_data_folder_path)
# new_data_folder_path.makedirs_p
