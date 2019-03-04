import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import time
from networks.FlowNetC import  FlowNetC
from losses import compute_loss
import image_warp
FLOW_SCALE=5.0





def train(img1,img2):
    img_f = torch.cat((img1, img2), 1)
    img_b = torch.cat((img2, img1), 1)
    flownetc = FlowNetC()
    flowf = flownetc(img_f)
    print(len(flowf))
    print(type(flowf))
    flowb = flownetc(img_b)
    loss=compute_loss(img1,img2,flowf,flowb)

    parameters=flownetc.parameters()
    optimizer = torch.optim.adam(parameters,lr=0.001)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    print('loss:',loss)



if __name__ == '__main__':

    a=torch.randn(1,3,256,256)
    b=torch.randn(1,3,256,256)

    for i in range(1000):
        train(a,b)







# a=torch.randn(1,3,256,256)
# b=torch.randn(1,3,256,256)
# start=time.time()
# flow_f,flow_b=flownet(a,b)
# end=time.time()
# print('costtime:',end-start)


#
# A=time.time()
# flownetc=FlowNetC()
# a=torch.randn(1,6,256,256)
# a1,a2,a3,a4,a5=flownetc(a)
# b=time.time()
# print('cost_time:',b-A)
# print(a1.size())
# print(a2.size())
# print(a3.size())
# print(a4.size())
# print(a5.size())
#







