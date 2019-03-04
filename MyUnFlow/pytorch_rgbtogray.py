import numpy as np
import torch
from torchvision import transforms
import torch.nn.functional as F
from PIL import Image
import matplotlib.pyplot as plt
import torchvision.transforms.functional.to_grayscale
transforms1=transforms.Compose(
    [transforms.Grayscale(1)
]
)

im=Image.open(r'/home/yh/桌面/LBJ.jpeg')
# a=np.array(im)
# c=transforms1(a)
# print(type(c))
# print(c.size())


ims=F.to_grayscale(im,1)
plt.imshow(ims)
plt.show()

