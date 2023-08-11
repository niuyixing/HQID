# HQID
This study proposed a High-Quality Integration Domain framework for pedestrian recognition. 



A PyTorch implementation of NPIQE based on IEEE ACCESS paper 
[Multi-Source Domain Fusion Cross-Domain Pedestrian Recognition Based on High-Quality Intermediate Domains](https://ieeexplore.ieee.org/document/10188821?source=authoralert).
### Install

- Clone this repo:

```bash
git clone https://github.com/niuyixing/NPIQE/edit/main/
cd InternImage
```
## HCycleGAN
### Data Preparation

1. Download the dataset.

 For pedestrian detection, we train and test our model on [Caltech](http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/) and [CityPersons](https://bitbucket.org/shanshanzhang/citypersons), you should firstly download the datasets. By default, we assume the dataset is stored in `./data/`.

2. Dataset preparation.

 For Caltech, you can follow [./eval_caltech/extract_img_anno.m](./eval_caltech/extract_img_anno.m) to extract official seq files into images. Training and test are based on the new annotations provided by [Shanshan2016CVPR](https://www.mpi-inf.mpg.de/departments/computer-vision-and-multimodal-computing/research/people-detection-pose-estimation-and-tracking/how-far-are-we-from-solving-pedestrian-detection/). We use the train_10x setting (42782 images) for training, the official test set has 4024 images. By default, we assume that images and annotations are stored in `./data/caltech`, and the directory structure is

For citypersons, we use the training set (2975 images) for training and test on the validation set (500 images), we assume that images and annotations are stored in  `./data/citypersons`

### Dependencies
We use torch version 1.10.0, torchnet version 0.0.4, numpy version 1.21.4, dominate version 2.7.0, visdom version 0.1.8.9.
* torch                           >=1.4.0
* torchvision	     >=0.5.0
* dominate	     >=2.4.0
* visdom	                     >=0.1.8.8
* torchnet                      
* numpy		 
* fsspec
* tensorboard
* packaging
* psutil
* pyre_extensions
* typing_extensions
* setuptools
* tqdm
* wandb

### Usage
#### super-resolution
Our super-resolution code is developed on top of [ESPCN](https://github.com/leftthomas/ESPCN).




Store the caltech dataset in the following folder:

```
*data
	*caltech
		*train
        		*set00_V000_I00002.jpg
        		*...

		*val
        		*set06_V000_I00029.jpg
        		*...
```
python data_utils.py

The results are shown below:

```
*data
	*train
		*SRF_3
			*data
        		*set00_V000_I00002.jpg
        		*...
			*target
            		*set00_V000_I00002.jpg
        		*...
	*val
		*SRF_3
			*data
        		*set06_V000_I00029.jpg
        		*...
			*target
            		*set06_V000_I00029.jpg
        		*...
```
python -m visdom.server

python train_espcn.py


Store the caltech dataset in the following folder:
```
*data
	*test
		*SRF_3
			*data
        		*set00_V000_I00002.jpg
			*set06_V000_I00029.jpg
        		*...
```

python test_image.py


#### Style-transfer

Our Style-transfer code is developed on top of [CycleGAN](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix).

Store the caltech and cityperson dataset in the following folder:
```
*try
	*trainA
		*data
		*set00_V000_I00002.jpg
		*...
	*testA
		*data
		*set00_V000_I00002.jpg
		*...
	*trainB
		*data
		*bielefeld_000000_000321_leftImg8bit.png
		*...
	*testB
		*data
		*bielefeld_000000_000321_leftImg8bit.png
		*...
```


```bash
python train_CycleGAN.py --dataroot try  --name try  --model cycle_gan --pool_size 50 --no_dropout  --crop_size 640  --preprocess crop 
python test_CycleGAN.py --dataroot datasets/try   --name try  --model cycle_gan --phase test --no_dropout --preprocess none --load_size 640
cd InternImage
```

## NPIQE

In writing

## Citation
If you think our work is useful in your research, please consider citing:
```
@inproceedings{
  title={Multi-Source Domain Fusion Cross-Domain Pedestrian Recognition Based on High-Quality Intermediate Domains},
  author={Yixing Niu; Wansheng Cheng; Yushan Lai; Hongzhi Zhang; Mingrui Cao; Kang Cao; Song Fan},
  booktitle={IEEE Access},
  year={2023}
}
```
