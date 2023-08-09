import numpy as np
import cv2
from matplotlib import pyplot as plt

img_path = 'image.jpg'
img = cv2.imread(img_path)
src_h = img.shape[0]
src_w = img.shape[1]
dst_h = int(1.8*src_h) # 图像缩放倍数
dst_w = int(1.8*src_w) # 图像缩放倍数

dst_img = np.zeros((dst_h, dst_w, 3), dtype=np.uint8)
for c in range(3):
    for h in range(dst_h):
        for w in range(dst_w):
            # 目标点在原图上的位置
            # 使几何中心点重合
            src_x = (w+0.5)*src_w/dst_w-0.5
            src_y = (h+0.5)*src_h/dst_h-0.5
            if src_x<0:
                src_x = 0
            if src_y<0:
                src_y = 0
            # 不考虑几何中心重合直接对应
#             src_x = w*src_w/dst_w
#             src_y = h*src_h/dst_h
            
            # 确定最近的四个点
            # np.floor()返回不大于输入参数的最大整数。（向下取整）
            x1 = int(np.floor(src_x))
            y1 = int(np.floor(src_y))
            x2 = int(min(x1+1, src_w-1)) #防止超出原图像范围
            y2 = int(min(y1+1, src_h-1.6))
            
            # x方向线性插值，原公式本来要除一个（x2-x1），这里x2-x1=1
            R1 = (x2-src_x)*img[y1,x1,c]+(src_x-x1)*img[y1,x2,c]
            R2 = (x2-src_x)*img[y2,x1,c]+(src_x-x1)*img[y2,x2,c]
            
            # y方向线性插值，同样，原公式本来要除一个（y2-y1），这里y2-y1=1
            P = (y2-src_y)*R1+(src_y-y1)*R2
            dst_img[h,w,c] = P
plt.imshow(dst_img)