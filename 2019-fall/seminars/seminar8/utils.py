import numpy as np
import os

from PIL import Image

import torch
import torch.nn as nn
from torch.utils.data import Dataset
from torchvision import transforms
from torch.optim.lr_scheduler import StepLR

import matplotlib.pyplot as plt
from matplotlib import gridspec

import pickle
from tqdm import trange

from IPython.display import clear_output

class WeizmannHorsesDataset(Dataset):
    """Weizmann Horses dataset."""

    def __init__(self, root, split, img_shape = (400,500), color = "rgb"):
        """
        Args:
            root (string): Directory with all the images.
            split - "train" or "val"
            color - "rgb" or "gray"
            
        """
        self.root = root
        self.color = color
        
        self.img_folder = os.path.join(root, color)
        self.mask_folder = os.path.join(root, "figure_ground")
        self.img_list = sorted([name for name in os.listdir(self.img_folder)])
        
        self.img_shape = img_shape
        
        split_index = int(len(self.img_list)*0.8)
        
        self.split = split
        
        if split == "train":
            self.img_list = self.img_list[:split_index]
        if split == "val":
            self.img_list = self.img_list[split_index:]

    def __len__(self):
        return len(self.img_list)

    def __getitem__(self, ind):
        # reading image
        img_name = os.path.join(self.img_folder,
                                self.img_list[ind])
        image = Image.open(img_name)
        
        # reading mask
        mask_name = os.path.join(self.mask_folder,
                                 self.img_list[ind])
        mask = Image.open(mask_name)
        mask = mask.convert('1')
            
        # resizing of mask and image
        img_transforms = transforms.Compose([transforms.Resize(self.img_shape, interpolation = Image.BILINEAR),
                                             transforms.ToTensor()])
        
        mask_transforms = transforms.Compose([transforms.Resize(self.img_shape, interpolation = Image.NEAREST),
                                              transforms.ToTensor()])
        
        image = img_transforms(image)
        mask = mask_transforms(mask)
        
        return (image, mask.long())

def show_sample(dataset,ind):
    fig, axs = plt.subplots(1, 2, figsize=(15, 4), constrained_layout=True)
    img, mask = dataset[ind]
    axs[0].imshow(img.permute(1,2,0))
    axs[0].axis('off')
    axs[1].imshow(mask.squeeze())
    axs[1].axis('off')
    plt.show()

def plot_batch_with_results(batch_imgs, batch_gts, results, outdir = None):
    """
    Plots images, GT segmentations and generated segmentations
    Input:
        batch_imgs - tensor of size (batch_size, 3, h, w)
        batch_gts - tensor of size (batch_size, 1, h, w)
        results - tensor of size (batch_size, 1, h, w)
        outdir - where the results should be saved
    """
    batch_size = batch_imgs.shape[0]
    rows = 3

    fig = plt.figure(figsize=(batch_size * 5, rows * 4))
    gs = gridspec.GridSpec(rows, batch_size, wspace=0.0, hspace=0.0)
    
    for img_num in range(batch_size):
        ax = plt.subplot(gs[0,img_num])
        ax.axis('off')
        ax.imshow(batch_imgs[img_num].permute(1,2,0))
        
        ax = plt.subplot(gs[1,img_num])
        ax.axis('off')
        ax.imshow(batch_gts[img_num].squeeze())

        ax = plt.subplot(gs[2,img_num])
        ax.axis('off')
        ax.imshow(results[img_num].squeeze())
        
    fig.tight_layout()
    clear_output()
    plt.show()

def plot_history(history, title='loss', save_dir = "results/"):
    
    plt.figure(figsize=(20,10))

    plt.subplot(221)
    plt.title('Loss')
    plt.plot(history["loss_train"], label='train', zorder=1)
    
    points = np.array(history["loss_val"])
    plt.plot(points[:, 0], points[:, 1], label='val', zorder=2)
    plt.xlabel('train steps')
    
    plt.legend(loc='best')
    plt.grid()
    
    for i, metric_name in enumerate(["iou", "pixel_acc", "mean_acc"]):
        plt.subplot(222 + i)
        plt.title(metric_name)
        plt.xlabel('epochs')
        plt.plot(history[metric_name + "_train"], label='train', zorder=2)
        plt.plot(history[metric_name + "_val"], label='validation', zorder=2)
        plt.legend(loc='best')
        plt.grid()

    plt.show()

def pixel_accuracy(pred, mask):
    """
        Computes pixel-wise accuracy: percentage of correctly predicted pixels 
    """
    return (pred == mask).float().mean()


def mean_accuracy(pred, mask):
    """
        Computes mean class accuracy
    """
    classes = [0,1]
    acc = 0
    for c in classes:
        TP = ((pred == mask)&(mask== c)).sum().float()
        TP_FN = (mask== c).sum().float()
        acc += TP /TP_FN
    return acc/len(classes)

def mean_iou(pred, mask, classes = [0,1]):
    """
        Computes IoU metrics for two segmentations only for given classes
            (if class is not presented in mask, it is not considered in mean)
        Input:
            pred - predicted segmentaion - torch tensor with shape (h,w)
            mask - ground truth segmentaion - torch tensor with shape (h,w)
            classes - list of considered classes numbers (default - all classes in mask)
            loss_mask = 1 for considered pixel, torch tensor with shape (h,w) (default - all pixels are True)
            device - torch.device
        Output: 
            mean IoU for given list of classes
    """
        
    iou = 0

    for c in classes:

        pred_ = (pred == c)
        labels_ = (mask == c)

        TP = (pred_*labels_).sum().float()
        FP = (pred_ * (~labels_)).sum().float()
        FN = ((~pred_) * labels_).sum().float()

        if TP + FP + FN != 0:
            iou += TP/(TP + FP + FN)

    return iou/len(classes)

