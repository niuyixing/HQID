import numpy as np
import cv2

def calc_ssim(img1, img2):
    img1=cv.
    img1 = img1.astype(np.float32) / 255.0
    img2 = img2.astype(np.float32) / 255.0
    C1 = (0.01 * 255)**2
    C2 = (0.03 * 255)**2
    mu1 = cv2.GaussianBlur(img1, (3,3), 0)
    mu2 = cv2.GaussianBlur(img2, (3,3), 0)
    mu1_sq = mu1 * mu1
    mu2_sq = mu2 * mu2
    mu1_mu2 = mu1 * mu2
    sigma1_sq = cv2.GaussianBlur(img1 * img1, (3,3), 0) - mu1_sq
    sigma2_sq = cv2.GaussianBlur(img2 * img2, (3,3), 0) - mu2_sq
    sigma12 = cv2.GaussianBlur(img1 * img2, (3,3), 0) - mu1_mu2
    ssim = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) * (sigma1_sq + sigma2_sq + C2))
    return np.mean(ssim)
if __name__ == "__main__":
    calc_ssim("newplot","newplot")