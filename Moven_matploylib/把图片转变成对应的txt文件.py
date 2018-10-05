#还没有ok
import os
from PIL import Image
import numpy as np


def load_data():
    data = np.empty((42000, 1, 28, 28), dtype="float32")
    label = np.empty((42000,), dtype="unit8")

    imgs = os.listdir("C:/Users/Administrator/PycharmProjects/莫凡教程/datasets/图片转变成txt/")
    num = len(imgs)
    for i in range(num):
        img = Image.open("C:/Users/Administrator/PycharmProjects/莫凡教程/datasets/图片转变成txt" + imgs[i])
        arr = np.asarray(img, dtype="float32")
        data[i, :, :, :] = arr
        label[i] = int(imgs[i].split('.')[0])

        return data, label