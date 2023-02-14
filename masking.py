import numpy as np
from PIL import Image
import matplotlib.pyplot as plt



def create_mask(path, color_threshold):
    """
    create a binary mask of an image using a color threshold
    args:
    - path [str]: path to image file
    - color_threshold [array]: 1x3 array of RGB value
    returns:
    - img [array]: RGB image array
    - mask [array]: binary array
    """
    # IMPLEMENT THIS FUNCTION
    # open the path image converting to RGB
    img = np.array(Image.open(path).convert('RGB'))
    # extract the RGB matrices per pixel
    R_Matrix, G_Matrix, B_Matrix = img[..., 0], img[..., 1], img[..., 2] 
    # Thresshold the RGB matrces
    mask = (R_Matrix > color_threshold[0]) & (G_Matrix > color_threshold[1]) & (B_Matrix > color_threshold[2])
    
   
    return img, mask


def mask_and_display(img, mask):
    """
    display 3 plots next to each other: image, mask and masked image
    args:
    - img [array]: HxWxC image array
    - mask [array]: HxW mask array
    """
    # IMPLEMENT THIS FUNCTION
    # Original image
    
    img_mask = img*np.stack([mask]*3, axis=2)
    f,ax  = plt.subplots(1, 3,figsize=(30, 20))
    ax[0].imshow(img)
    ax[1].imshow(mask)
    ax[2].imshow(img_mask)   
    plt.show()
if __name__ == '__main__':
    path = 'data/images/segment-1231623110026745648_480_000_500_000_with_camera_labels_38.png'
    color_threshold = [100, 100, 128]
    img, mask = create_mask(path, color_threshold)
    mask_and_display(img, mask)