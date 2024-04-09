# import os
# import struct
# import numpy as np

# def read_mnist_images(filename):
#     with open(filename, 'rb') as f:
#         _, num_images, num_rows, num_cols = struct.unpack('>IIII', f.read(16))
#         images = np.fromfile(f, dtype=np.uint8).reshape(num_images, num_rows * num_cols)
#     return images

# def read_mnist_labels(filename):
#     with open(filename, 'rb') as f:
#         _, num_labels = struct.unpack('>II', f.read(8))
#         labels = np.fromfile(f, dtype=np.uint8)
#     return labels

# # 解析训练集
# train_images = read_mnist_images('data_set/train-images-idx3-ubyte')
# train_labels = read_mnist_labels('data_set/train-labels-idx1-ubyte')

# # 解析测试集
# test_images = read_mnist_images('data_set/t10k-images-idx3-ubyte')
# test_labels = read_mnist_labels('data_set/t10k-labels-idx1-ubyte')

# # 打印一些信息来验证
# print('训练集图像数量:', len(train_images))
# print('训练集标签数量:', len(train_labels))
# print('测试集图像数量:', len(test_images))
# print('测试集标签数量:', len(test_labels))

# # 可视化第一个图像
# import matplotlib.pyplot as plt

# plt.imshow(train_images[0].reshape(28, 28), cmap='gray')
# plt.title(f'Label: {train_labels[0]}')
# plt.show()



import gzip
import numpy as np
from array import array

def read_mnist_labels(filename):
    with gzip.open(filename, 'rb') as f:
        a = f.read(8)  # 跳过魔数和数量
        print(np.frombuffer(a, dtype='>u4'))
        buf = f.read()
        labels = np.frombuffer(buf, dtype=np.uint8)
    return labels

def read_mnist_images(filename):
    with gzip.open(filename, 'rb') as f:
        b = f.read(16)  # 跳过魔数、数量和尺寸
        print(np.frombuffer(b, dtype='>u4'))  # >u4 大端字节序的uint32数据类型
        buf = f.read()
        data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
        data = data.reshape(-1, 28 * 28)  # 28x28图像
        data = data / 255  # 归一化
    return data

# 读取压缩的MNIST数据集
train_images = read_mnist_images('data_set/train-images-idx3-ubyte.gz')
train_labels = read_mnist_labels('data_set/train-labels-idx1-ubyte.gz')
test_images = read_mnist_images('data_set/t10k-images-idx3-ubyte.gz')
test_labels = read_mnist_labels('data_set/t10k-labels-idx1-ubyte.gz')

# 打印一些信息来验证
print('训练集图像数量:', len(train_images))
print('训练集标签数量:', len(train_labels))
print('测试集图像数量:', len(test_images))
print('测试集标签数量:', len(test_labels))

# 可视化第一个图像
import matplotlib.pyplot as plt

plt.imshow(test_images[0].reshape(28, 28), cmap='gray')
plt.title(f'Label: {test_labels[0]}')
plt.show()
