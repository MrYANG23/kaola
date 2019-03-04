#-*-coding:utf-8-*-
import PIL
import matplotlib.pyplot as plt
import torch
import torchvision.transforms.functional as tf
from PIL import Image
import numpy as np
from scipy.misc import imread,imresize
import skimage.io
import torchvision.transforms
#用imread和PIL读取出来的图转为ndarray均为uint8
image_files='/home/yh/桌面/LBJ.jpg'


rpn_files='/home/yh/shujuji/ILSVRC2015_VID/vid15rpn_finetune/ILSVRC2015_train_00000000/000001.00.x_102.46_29.62.jpg'
rpn1_files='/home/yh/shujuji/ILSVRC2015_VID/ILSVRC2015/Data/VID/train/ILSVRC2015_VID_train_0000/ILSVRC2015_train_00000000/000000.JPEG'
im1=Image.open(rpn1_files)
print('------------------------PIL读取图片的形状',im1.size)
# ims=np.array(im)
#
# im_resize=imresize(im,(256,256))
# # print('----------------------------用imresize改变尺寸',im_resize.shape)
#
#
# im_1=imread('/home/yh/桌面/LBJ.jpg')
#
# print(im_1)
# print('imread读取的数据类型',im_1.dtype)
# print('--------------------------------------')
# print(ims.shape)
# print('PIL读取的数据类型',ims.dtype)
# plt.figure('god')
# plt.imshow(im)
# plt.show()
# print(im.size)
# print(type(im))
img = skimage.io.imread('/home/yh/桌面/LBJ.jpg')

# print('----------------------------------skimage读取出来的数据类型',type(img))
#
def image_resize(images):
    return tf.resize(images,(128,128))




a=torch.randn(3,256,256)
# print('-------------------------------type_a',type(a))
# b=a.numpy()
# print('-------------------------------type_b',type(b))
#
#
# print(b)
# print('----------------------------------type_im_1',type(im_1))
# array_PIL=Image.fromarray(b)
# print('------------------------------------array_PIL',type(array_PIL))
# image_resize2=image_resize(array_PIL)
# print(image_resize2.size)
# # plt.figure('god3')
# # plt.imshow(array_PIL)
# # plt.show()

#
def image_resize(images,h,w):
    # tensor_to_pil=torchvision.transforms.ToPILImage(images)
    return tf.resize(images,(h,w))

# im_resize=image_resize(im)
# plt.figure('god')
# plt.imshow(im_resize)
# plt.show()
# print(im_resize.size)
#
# plt.figure('god2')
# plt.imshow(im)
# plt.show()


#
# tensor_to_pil=torchvision.transforms.ToPILImage(a)
# print('-----------------------------type',type(tensor_to_pil))


# new=image_resize(tensor_to_pil,128,128)



