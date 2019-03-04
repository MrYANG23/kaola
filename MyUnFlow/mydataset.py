import torch
import torch.utils.data as data
from torch.utils.data import DataLoader

import os
import math
import random
from os.path import *
import numpy as np
from glob import glob
from scipy.misc import imread,imresize
from torchvision import transforms

# def read_gen(file_name):
#     print("-------------------------------------检测是否进入read_gen")
#     ext=splitext(file_name)[-1]
#     print("-------------------------------------------ext",ext)
#     if ext =='.png' or ext =='.jpeg' or ext =='.ppm ' or ext== '.jpg':
#         print("---------------------------------------检测是否进入的选型")
#         im=imread(file_name)#imread_ndarray
#         print("------------------------ceshi2",im.shape)
#         if im.shape[2]>3:
#             return im[:,:,:3]
#         else:
#             return im
#
#     elif ext =='.bin' or ext =='.raw':
#         return np.load(file_name)
def read_gen(file_name):
    ext = splitext(file_name)[-1]
    if ext == '.png' or ext == '.jpeg' or ext == '.ppm' or ext == '.jpg':
        im = imread(file_name)
        if im.shape[2] > 3:
            return im[:,:,:3]
        else:
            return im
    elif ext == '.bin' or ext == '.raw':
        return np.load(file_name)
    # elif ext == '.flo':
    #     return flow_utils.readFlow(file_name).astype(np.float32)
    return []



class Flycharis(data.Dataset):
    def __init__(self,root='/home/yh/shujuji/FlyingChairs_release/data'):#root为存放数据集的绝对路径
        self.root=root
        images=sorted(glob(join(root,'*.ppm')))#glob用来遍历root路径下所有以.ppm结尾的路径并排序
        self.flow_list=sorted(glob(join(root,'*.flo')))

        assert (len(images))//2==len(self.flow_list)


        self.image_list=[]
        for i in range(len(self.flow_list)):
            image1=images[2*i]
            image2=images[2*i+1]

            self.image_list+=[[image1,image2]]

        assert len(self.image_list)==len(self.flow_list)

        self.size=len(self.image_list)


    def __getitem__(self, index):
        index=index%self.size#当index小于self.size时。index等于index，否则取余数
        img1=read_gen(self.image_list[index][0]).astype(np.float32)#将对应地址的图片通过scipy中的imread读取为对应数组

        img2=read_gen(self.image_list[index][1]).astype(np.float32)
        im1=torch.from_numpy(img1)
        im2=torch.from_numpy(img2)

        # traget_transforms=transforms.Compose([transforms.ToTensor()])


        # im1=traget_transforms(img1)
        # im2=traget_transforms(img2)
        images=[im1,im2]

        return images

    def __len__(self):
        return self.size


#
# myflychairs=Flycharis()
# train_dataloder=DataLoader(myflychairs,batch_size=4,num_workers=1,shuffle=True)
# print("------------------------",len(train_dataloder))
#
#
# #
# # print(len(train_dataloder))#5718
# # #
# # # print('--------------len_train_dataloader',len(train_dataloder))
# #
# #
# #
# #
# # images=myflychairs.get_batch(train_dataloder)
# # print(len(images))
# for i,images in enumerate(train_dataloder):
#     print(len(images))