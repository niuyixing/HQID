import argparse
import cv2
import numpy as np
from skimage.metrics import structural_similarity as compare_ssim
from niqe import niqe
from piqe import piqe
import os
import re

parser = argparse.ArgumentParser('Test an image')
parser.add_argument('--path', required=True, help='directory path for the images')
args = parser.parse_args()


def compute_delete_ratio(ssim_avg):
    if 0.8 <= ssim_avg <= 1.0:
        return 0.4
    elif 0.6 <= ssim_avg < 0.8:
        return 0.3
    elif 0.4 <= ssim_avg < 0.6:
        return 0.2
    elif 0.2 <= ssim_avg < 0.4:
        return 0.1
    else:
        return 0


if __name__ == "__main__":
    fileList = os.listdir(args.path)
    print("Original files:" + str(fileList))

    os.chdir(args.path)
    scores = []
    ssim_values = []

    # Compute average SSIM for each image with all other images
    for fileName in fileList:
        pat = ".+\.(png)"
        pattern = re.findall(pat, fileName)

        if pattern:
            im = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)
            if im is None:
                print("{}- Skipped due to invalid image format".format(fileName))
                continue

            total_ssim = 0.0
            count = 0

            for otherFileName in fileList:
                if otherFileName != fileName:
                    otherImage = cv2.imread(otherFileName, cv2.IMREAD_GRAYSCALE)
                    if otherImage is not None:
                        ssim_value, _ = compare_ssim(im, otherImage, full=True)
                        total_ssim += ssim_value
                        count += 1

            average_ssim = total_ssim / count if count != 0 else 0
            ssim_values.append(average_ssim)
            print(average_ssim)
            score_niqe = niqe(im)
            score_piqe, _, _, _ = piqe(im)
            combined_score = 0.5 * score_niqe + 0.5 * score_piqe
            scores.append((fileName, combined_score))

    overall_ssim = min(ssim_values)
    print(overall_ssim)
    delete_ratio = compute_delete_ratio(overall_ssim)

    # Sort scores based on quality, worst first
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    num_to_delete = int(len(sorted_scores) * delete_ratio)

    for i in range(num_to_delete):
        os.remove(sorted_scores[i][0])
        print("Removed: {}".format(sorted_scores[i][0]))

    print("Process completed!")
