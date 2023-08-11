import argparse

import cv2
from joblib import load
import numpy as np
from brisque import brisque
from niqe import niqe
from piqe import piqe
import os
import re
import sys

import matplotlib.pyplot as plt
from PIL import Image




parser = argparse.ArgumentParser('Test an image')
parser.add_argument('--path', required=True, help='directory path for the images')
args = parser.parse_args()

if __name__ == "__main__":
    '''
    test conventional blindly image quality assessment methods(niqe/piqe)
    '''

    fileList = os.listdir(args.path)
    print("Original files:" + str(fileList))

    os.chdir(args.path)
    scores = []  # Store combined scores for each image here

    for fileName in fileList:
        pat = ".+\.(png)"
        pattern = re.findall(pat, fileName)

        if pattern:  # Checking if the file is a png image
            im = cv2.imread(fileName)

            if im is None:
                print("{}- Skipped due to invalid image format".format(fileName))
                continue

            score_niqe = niqe(im)
            score_piqe, _, _, _ = piqe(im)

            combined_score = 0.5 * score_niqe + 0.5 * score_piqe
            scores.append((fileName, combined_score))
            print("{} --- combined score:{}".format(fileName, combined_score))

    # Sort the scores list by score in descending order
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # Compute the number of images to delete (33%)
    num_to_delete = int(len(sorted_scores) * 0.33)

    # Delete the images with the worst scores
    for i in range(num_to_delete):
        os.remove(sorted_scores[i][0])
        print("Removed: {}".format(sorted_scores[i][0]))

    print("Process completed!")