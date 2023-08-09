import cv2
import numpy as np

def ssim(img1, img2, C1=6.5025, C2=58.5225):
    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)

    mu1 = cv2.GaussianBlur(img1, (11, 11), 1.5)
    mu2 = cv2.GaussianBlur(img2, (11, 11), 1.5)

    mu1_sq = mu1 ** 2
    mu2_sq = mu2 ** 2
    mu1_mu2 = mu1 * mu2

    sigma1_sq = cv2.GaussianBlur(img1 * img1, (11, 11), 1.5) - mu1_sq
    sigma2_sq = cv2.GaussianBlur(img2 * img2, (11, 11), 1.5) - mu2_sq
    sigma12 = cv2.GaussianBlur(img1 * img2, (11, 11), 1.5) - mu1_mu2

    ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) * (sigma1_sq + sigma2_sq + C2))
    return ssim_map.mean()

# 读取两幅图像
img1 = cv2.imread('path/to/image1.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('path/to/image2.png', cv2.IMREAD_GRAYSCALE)

# 计算 SSIM
ssim_value = ssim(img1, img2)
print('SSIM:', ssim_value)