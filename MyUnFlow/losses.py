import torch
import torch.nn as nn
import numpy as np
import torch.nn.functional as F
from torch.nn.functional import conv2d
from image_warp import image_warp
import time

def create_mask(tensor,paddings):#输入为tensor
    print('------------------------------------------------j进入create_mask')
    shape=tensor.size()
    # print('shape:',shape,'type:',type(tensor.size()))
    inner_width=shape[2]-(paddings[0][0]+paddings[0][1])
    inner_height=shape[3]-(paddings[1][0]+paddings[1][1])
    # print('inner_width:',inner_width)
    # print('inner_height:',inner_height)
    inner=torch.ones([inner_width,inner_height])
    # print('inner:',inner)
    mask2d=np.pad(inner,paddings,'constant')
    # print('mask2D:',mask2d)
    # print('mask2D_size:',mask2d.shape)
    mask3d=np.tile(np.expand_dims(mask2d,0),[shape[0],1,1])
    # print('mask3d:',mask3d)
    mask4d=np.expand_dims(mask3d,1)
    return torch.Tensor(mask4d)
# g=torch.ones(2,3,4,5)
# h=torch.ones([2,2])
# print(h)
# print('__________________')
# print(g)

# B=torch.Tensor(2,3,4,5)
# print(B.size())
# print('___________________________')
# C=B.size()
# for i in range(4):
#     print(C[i])
# print('!!!!!!!!!!!!!!!!!!!!')
# for i in B.size():
#     print(i)

def create_border_mask(tensor,border_ratio=0.1):
    print('----------------------------------------------进入create_border_mask')
    num_batch,height,width,_=np.shape(tensor)
    min=np.minimum(height,width).astype('float32')
    sz=np.ceil(min*border_ratio).astype('int32')
    border_mask=create_mask(tensor,[[sz,sz],[sz,sz]])

    return torch.tensor(border_mask)

# b=torch.randn(1,1,6,6)
# print(b.size())
# print('_____________________')
# c=np.shape(b)
# print(type(c))
# n,h,w,_=c
# print('n:',n,'h:',h,'w:',w)

# a=torch.randn(1,1,6,6)
#
# print('a:',a)
# print(a.size())
# paddings=[[1,1],[1,1]]
# b=create_mask(a,paddings)
# print('b:',b)
# print(b.size())
# c=create_border_mask(b)
# print('c:',c)
# print('__________________________________')
# print(c.requires_grad)


def charbonnier_loss(x,mask=None,truncate=None,alpha=0.45,beta=1.0,epsilon=0.001):
    print('-------------------------------------------------进入charbonnier_loss')
    batch,height,width,channels=np.shape(x)
    #用torch
    normalization=torch.tensor(batch*height*width*channels).type(torch.FloatTensor)
    #用numpy
    # normalization=torch.tensor(np.float32(batch*height*width*channels))

    error=np.power(np.square(x*beta)+np.square(epsilon),alpha)
    # print('_______________')
    # print(type(error))
    # print(error.size())
    # print(type(mask))
    # print(mask.size())
    if mask is not None:
        error=np.multiply(mask,error)
    if truncate is not None:
        error=np.minimum(error,truncate)

    return torch.sum(error)/normalization
# 测试charbonnier_loss
# a=torch.randn((1,1,6,6))
# b=charbonnier_loss(a)
# print('b:',b)

def _gradient_delta(im1,im2_warped):
    print('-------------------------------------进入_gradient_delta')
    #im1,im2_warped输入为tensor
    print('im1_size:',im1.size())
    print('im2_size:',im2_warped.size())
    filter_x=[[-1,0,1],[-2,0,2],[-1,0,1]]#sobel 算子
    filter_y=np.transpose(filter_x)
    weight_array=np.zeros([6,3,3,3],dtype='float32')
    for c in range(3):
        weight_array[c*2,c,:,:]=filter_x
        weight_array[2*c+1,c,:,:]=filter_y
    weights=torch.from_numpy(weight_array)

    # print('weights_size:',weights.size())
    im1_grad=F.conv2d(im1,weights,padding=1)
    # print('im1_grad_size:',im1_grad.size())
    im2_warped_grad=F.conv2d(im2_warped,weights,padding=1)
    diff=im1_grad-im2_warped_grad
    return diff
# a1=torch.randn((1,3,8,8))
# a2=torch.randn((1,3,8,8))
# b=_gradient_delta(a1,a2)
# print(b.size())
#debug:
#im1_size: torch.Size([1, 3, 8, 8])
# im2_size: torch.Size([1, 3, 8, 8])
# weights_size: torch.Size([6, 3, 3, 3])
#torch.Size([1, 6, 6, 6])

def gaadient_loss(im1,im2_warped,mask):
    print('---------------------------------------------进入gaadient_loss')
    mask_x=create_mask(im1,[[0,0],[1,1]])
    mask_y=create_mask(im1,[[1,1],[0,0]])
    gradient_mask=torch.cat((mask_x,mask_y),1).repeat((1,3,1,1))
    print('gradient_mask_size:',gradient_mask.size())
    diff=_gradient_delta(im1,im2_warped)
    print('diff_size:',diff.size())
    return charbonnier_loss(diff,mask*gradient_mask)



def _smoothness_deltas(flow):
    print('------------------------------------------------进入_smoothness_deltas')
    mask_x=create_mask(flow,[[0,0],[0,1]])
    mask_y=create_mask(flow,[[0,1],[0,0]])
    print(mask_x.size())
    print('___________')
    print(mask_y.size())
    mask=torch.cat((mask_x,mask_y),1)
    filter_x=[[0,0,0],[0,1,-1],[0,0,0]]
    filter_y=[[0,0,0],[0,1,0],[0,-1,0]]
    weight_array=np.ones([2,1,3,3],dtype='float32')
    weight_array[0,0,:,:]=filter_x
    weight_array[1,0,:,:]=filter_y
    weights=torch.from_numpy(weight_array)
    flow_u,flow_v=torch.chunk(flow,2,dim=1)
    delta_u=F.conv2d(flow_u,weights,padding=1)
    delta_v=F.conv2d(flow_v,weights,padding=1)
    return delta_u,delta_v,mask


#_smoothness_deltas测试
# a=torch.randn((1,2,6,6))
# b,c,d=_smoothness_deltas(a)
# print('b_size:',b.size())
# print('c_size:',c.size())
# print('d_size:',d.size())
# print('finish')
#debug:
# b_size: torch.Size([1, 2, 4, 4])
# c_size: torch.Size([1, 2, 4, 4])
# d_size: torch.Size([1, 2, 6, 6])
# finish

def smoothness_loss(flow):
    print('--------------------------------------------------进入smoothness_loss')
    delta_u,delta_v,mask=_smoothness_deltas(flow)
    loss_u=charbonnier_loss(delta_u,mask)
    loss_v=charbonnier_loss(delta_v,mask)
    return loss_u+loss_v
#
# #smoothness_loss测试：
# a=torch.randn(1,2,256,256)
# b=smoothness_loss(a)
#debug:
# print('b_size():',b)
# b_size(): tensor(2.1584)


def _second_order_deltas(flow):
    print('---------------------------------------------------------进入_second_order_deltas')
    mask_x=create_mask(flow,[[0,0],[1,1]])
    mask_y=create_mask(flow,[[1,1],[0,0]])
    mask_diag=create_mask(flow,[[1,1],[1,1]])
    mask=torch.cat((mask_x,mask_y,mask_diag,mask_diag),1)
    filter_x=[[0,0,0],
              [1,-2,1],
              [0,0,0]]
    filter_y=[[0,1,0],
              [0,-2,0],
              [0,1,0]]
    filter_diag1=[[1,0,0],
                  [0,-2,0],
                  [0,0,1]]
    filter_diag2=[[0,0,1],
                  [0,-2,0],
                  [1,0,0]]
    weight_array=np.ones([4,1,3,3],dtype='float32')
    weight_array[0,0,:,:]=filter_x
    weight_array[1,0,:,:]=filter_y
    weight_array[2,0,:,:]=filter_diag1
    weight_array[3,0,:,:]=filter_diag2
    weights=torch.from_numpy(weight_array)
    flow_u,flow_v=torch.chunk(flow,2,dim=1)
    delta_u=F.conv2d(flow_u,weights,padding=1)#padding=same
    delta_v=F.conv2d(flow_v,weights,padding=1)
    return delta_u,delta_v,mask

def second_order_loss(flow):
    print('-------------------------------------------进入second_order_loss')
    delta_u,delta_v,mask=_second_order_deltas(flow)
    loss_u=charbonnier_loss(delta_u,mask)#charbonnier 需要delta 和mask维度相同
    loss_v=charbonnier_loss(delta_v,mask)
    return loss_u+loss_v
#测试second_order_loss:
# a=torch.randn(1,2,256,256)
# b=second_order_loss(a)
# print('second_order_loss',b)

#debug:
# second_order_loss tensor(3.5269)

def photometric_loss(im_diff,mask):
    print('-----------------------------------------------进入photometric_loss')
    return charbonnier_loss(im_diff,mask,beta=255)


def ternary_loss(im1,im2_warped,mask,max_distance=1):
    print('------------------------------------------------进入ternary_loss')
    patch_size=2*max_distance+1

def length_sq(x):
    return torch.sum(x*x,1,keepdim=True)

def compute_loss(img1,img2,flow_f,flow_b,border_mask=None,mask_occlusion='fb'):
    print('----------------------------------------进入compute_loss')
    losses={}

    im2_warped=image_warp(img2,flow_f)
    im1_warped=image_warp(img1,flow_b)

    im_diff_f=img1-im2_warped
    im_diff_b=img2-im1_warped

    if border_mask is None:
        mask_fw=create_border_mask(flow_f)
        mask_bw=create_border_mask(flow_b)
    else:
        mask_fw=border_mask
        mask_bw=border_mask
    flow_b_warped=image_warp(flow_b,flow_f)
    flow_f_warped=image_warp(flow_f,flow_b)
    flow_diff_fw=flow_f+flow_b_warped
    flow_diff_bw=flow_b+flow_f_warped

    mag_sq_fw=length_sq(flow_f)+length_sq(flow_b_warped)
    mag_sq_bw=length_sq(flow_b)+length_sq(flow_f_warped)
    occ_thresh_fw=0.01*mag_sq_fw+0.5
    occ_thresh_bw=0.01*mag_sq_bw+0.5

    fb_occ_fw=torch.tensor(np.array(length_sq(flow_diff_fw)>occ_thresh_fw).astype('float32'))
    fb_occ_bw=torch.tensor(np.array(length_sq(flow_diff_bw)>occ_thresh_bw).astype('float32'))

    if mask_occlusion=='fb':
        mask_fw*=(1-fb_occ_fw)
        mask_bw*=(1-fb_occ_bw)
    occ_fw=1-mask_fw
    occ_bw=1-mask_bw
    print('------------------------------------------------------------------------------计算occ_loss')

    losses['occ']=(charbonnier_loss(occ_fw)+charbonnier_loss(occ_bw))

    print('-----------------------------------------------------------------------------计算photo_loss')
    losses['photo']=(photometric_loss(im_diff_f,mask_fw)+photometric_loss(im_diff_b,mask_bw))
    print('--------------------------------------------------------------------------------计算grad_loss')
    # print('img1_size:',img1.size(),'im2_warped_size:',im2_warped.size(),'mask_size:',mask_fw.size())
    losses['grad']=(gaadient_loss(img1,im2_warped,mask_fw)+gaadient_loss(img2,im1_warped,mask_bw))
    print('-------------------------------------------------------------------------------计算smooth_1st')

    losses['smooth_1st']=(smoothness_loss(flow_f)+smoothness_loss(flow_b))
    print('---------------------------------------------------------------------------------计算smooth_2nd')

    losses['smooth_2nd']=(second_order_loss(flow_f)+second_order_loss(flow_b))
    print('------------------------------------------------------------------------------------------计算fb')

    losses['fb']=(charbonnier_loss(flow_diff_fw,mask_fw)+charbonnier_loss(flow_diff_bw,mask_bw))

    return losses

# def length_sq(x):
#     return torch.sum(x*x,1,keepdim=True)

if __name__ == '__main__':
    a=torch.randn((1,3,256,256),requrise=)
    b=torch.randn((1,3,256,256))
    c=torch.randn((1,2,256,256))
    d=torch.randn((1,2,256,256))
    start=time.time()
    All_loss=compute_loss(a,b,c,d)
    # print('--------------------------------------occ',All_loss['occ'])
    # print('--------------------------------------photo',All_loss['photo'])
    # print('----------------------------------------grad',All_loss['grad'])
    # print('-----------------------------------------smooth_1st',All_loss['smooth_1st'])
    # print('-----------------------------------------smooth_2nd',All_loss['smooth_2nd'])
    # print('---------------------------------------------fb',All_loss['fb'])
    end=time.time()
    print(All_loss)
    print('all_costtime:',end-start)
