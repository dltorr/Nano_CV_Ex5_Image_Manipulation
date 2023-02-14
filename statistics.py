import glob
from PIL import Image,ImageStat
import numpy as np
from utils import check_results
import seaborn as sns

def calculate_mean_std(image_list):
    """
    calculate mean and std of image list
    args:
    - image_list [list[str]]: list of image paths
    returns:
    - mean [array]: 1x3 array of float, channel wise mean
    - std [array]: 1x3 array of float, channel wise std
    """
    # IMPLEMENT THIS FUNCTION
   
    Img_means = []
    Img_std = []
    
    for onePath in image_list :
        # Open each image
        newImage = Image.open(onePath).convert('RGB')
        # Take the image stats
        Img_stat = ImageStat.Stat(newImage)
        # Append mean and standard deviation to the list
        Img_means.append(np.array(Img_stat.mean))
        Img_std.append(np.array(Img_stat.stddev))
    
    # Calculate the mean of both lists
    Images_mean = np.mean(Img_means,axis=0)    
    Images_std = np.mean(Img_std,axis=0) 
    
    
    return Images_mean , Images_std


def channel_histogram(image_list):
    """
    calculate channel wise pixel value
    args:
    - image_list [list[str]]: list of image paths
    """
    # IMPLEMENT THIS FUNCTION
    red = []
    green = []
    blue = []
    for onePath in image_list :
        # Open each image
        newImage = np.array(Image.open(onePath).convert('RGB'))
        # Take each channel matrix
        R, G, B = newImage[..., 0], newImage[..., 1], newImage[..., 2]
        
        
        red.extend(R.flatten().tolist())
        green.extend(G.flatten().tolist())
        blue.extend(B.flatten().tolist())
    sns.kdeplot(red, color='r')
    sns.kdeplot(green, color='g')
    sns.kdeplot(blue, color='b')      
        
if __name__ == "__main__": 
    image_list = glob.glob('data/images/*')
    mean, std = calculate_mean_std(image_list)
    check_results(mean, std)
   # channel_histogram(image_list)
  