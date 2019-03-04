#-*-coding:utf-8-*-
from PIL import Image
from networks.FlowNetC import FlowNetC
from networks.FlowNetS import FlowNetS
import torch
from losses import compute_loss
from mydataset import Flycharis
from torch.utils.data import DataLoader
from tqdm import tqdm
import torch.nn.functional
import time
import numpy as np
# import torchvision.transforms as transforms
import torchvision.transforms.functional as TF
flycharis=Flycharis()
mydataloder=DataLoader(flycharis,batch_size=4,shuffle=True,num_workers=1)
print(len(mydataloder))
flownets=FlowNetS()
flownets.train()
import torchvision.transforms.transforms

def pil_resize(tensor,h,w):
    return TF.resize(tensor,(h,w))


a=torch.randn(1,6,256,256)
A=flownets(a)

epoch_size=len(mydataloder)

device=("cuda" if torch.cuda.is_available() else "cpu")
# print(device)
# flownetc.to(device)


def resize_tensor(tensor,h,w):
    return torch.nn.functional.adaptive_avg_pool2d(tensor, (h,w))


for i in range(1):
    for j,images in tqdm(enumerate(mydataloder)):
        [im1,im2]=images

        im1_photo=im1
        im2_photo=im2

        im1=im1_photo.permute((0,3,1,2))

        im2=im2_photo.permute((0,3,1,2))
        #
        ims_f=torch.cat((im1,im2),1)
        ims_b=torch.cat((im2,im1),1)
        # # # ims_f.to(device)
        # # ims_b.to(device)
        # start=time.time()
        #
        flow_f=flownets(ims_f)
        flow_b=flownets(ims_b)
        flow_all=zip(flow_f,flow_b)

        for k,(flow_forward,flow_backward) in enumerate(flow_all):
            n,c,h,w=flow_forward.size()
            flow_ff=flow_forward.detach()
            flow_bb=flow_backward.detach()
            print('-------------------------------flow_forward_size()',flow_forward.size())
            print('------------------------------flow_backward_size()',flow_backward.size())
            img_1=resize_tensor(im1,h,w).detach()
            print('----------------------------==img_1.size',img_1.size())
            img_2=resize_tensor(im2,h,w).detach()
            print('-------------------------------img_2.size',img_2.size())
            loss=compute_loss(img_1,img_2,flow_ff,flow_bb)


        #







        # end=time.time()
        # print(len(flow_f))
        # print(len(flow_b))
        # print("all_cost:",end-start)


        # loss=compute_loss(im1_photo,im2_photo,flow_f,flow_b)
        # print(loss)








