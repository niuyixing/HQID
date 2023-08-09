from mmdet.apis import init_detector, inference_detector, show_result
import os
import re
import sys

import matplotlib.pyplot as plt
from PIL import Image

fileList = os.listdir(r"/root/autodl-fs/autodl-tmp/pytorch-CycleGAN-and-pix2pix/datasets/label2image_cyclegan_cal/trainA/")  # 待修改文件夹
config_file = 'configs/faster_rcnn_r50_fpn_1x.py'
checkpoint_file = 'checkpoints/faster_rcnn_r50_fpn_1x_20181010-3d1b3351.pth'

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')


# test a list of images and write the results to image files
imgs = fileList
for i, result in enumerate(inference_detector(model, imgs)):
    show_result(imgs[i], result, model.CLASSES, out_file='result_{}.jpg'.format(i))