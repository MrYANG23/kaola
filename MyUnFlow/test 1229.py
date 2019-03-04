import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

image_raw_data = tf.gfile.GFile('/home/yh/桌面/LBJ.jpg', 'r').read()  # 加载原始图像

with tf.Session() as sess:
    img_data = tf.image.decode_jpeg(image_raw_data)  # 解码
    plt.imshow(img_data.eval())
    plt.show()
    resized = tf.image.resize_images(img_data, [64, 64], method=0)  # 第一个参数为原始图像，第二个参数为图像大小，第三个参数给出了指定的算法
    resized = np.asarray(resized.eval(), dtype='uint8')  # 变为uint8才能显示
    plt.imshow(resized)
    plt.show()
