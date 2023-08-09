#批量修改文件名
#批量修改图片文件名
import os
import re
import sys
#这个库复制文件比较省事
import shutil

import matplotlib.pyplot as plt
from PIL import Image


def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)

def renameall():
    #fileList = os.listdir(r"D:\domain\ONCONTROL")       #待修改文件夹
    fileList = os.listdir(r"D:\domain\city——trans\all")  # 待修改文件夹
    aim_img_name = r'D:\domain\citycalttt2A'
    print("修改前："+str(fileList))     #输出文件夹中包含的文件
    currentpath = os.getcwd()       #得到进程当前工作目录
    os.chdir(r"D:\domain\city——trans\all")        #将当前工作目录修改为待修改文件夹的位置
    num=1       #名称变量
    for fileName in fileList:       #遍历文件夹中所有文件
        #pat=".+\.(jpg|png|gif|py|txt)"      #匹配文件名正则表达式
        pat = ".+\.(png)"  # 匹配文件名正则表达式
        pattern = re.findall(pat,fileName)      #进行匹配
        fileNamea = fileName.split(".")
        if fileNamea[1]=="png" :
            newnamea =fileNamea[0].split("_")
            print(newnamea)
           # newname = newnamea[0]+"_"+newnamea[1]+"_"+newnamea[2]+"_"+newnamea[3]+".png"
            newnameb = newnamea[0] + "_" + newnamea[1] + "_" + newnamea[2]  +"_"+newnamea[3]+ ".png"
            #os.rename(fileName,newnameb)       #文件重新命名
            #produceImage(newname,2048,1024,newnamea)
            path = aim_img_name + '/' + newnamea[0]
            if(not os.path.exists(path)):
                os.mkdir(path)

            shutil.copy(fileName, aim_img_name + '/' + newnamea[0] + '/' + newnameb)
            num = num+1     #改变编号，继续下一项
    print("---------------------------------------------------")

    # -*- codeing = utf-8 -*-
    # @Time : 2022/5/1 13:23
    # @Author : ning
    # @File : 5.1demo.py
    # @software : PyCharm



    os.chdir(currentpath)       #改回程序运行前的工作目录
    sys.stdin.flush()       #刷新
 #   print("修改后："+str(os.listdir(r"D:\domain\ONCONTROL")))       #输出修改后文件夹中包含的文件
renameall()

# Model loaded before prediction, predict n time points
