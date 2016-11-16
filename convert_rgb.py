import glob,os
import scipy.misc
import scipy.ndimage

def rgb2gray(img):
    R = img[:, :, 0]
    G = img[:, :, 1]
    B = img[:, :, 2]
    img_gray = R * 299. / 1000 + G * 587. / 1000 + B * 114. / 1000
    return img_gray

def run_rgb():

    for file in glob.glob("firstsub/*.jpg"):
        
        try:
            file_gray=rgb2gray(scipy.ndimage.imread(file))
        except IndexError:
            print(str(file)+' already in grayscale')
            continue

        scipy.misc.imsave(file,file_gray)

    for file in glob.glob("secondsub/*.jpg"):

        try:
            file_gray=rgb2gray(scipy.ndimage.imread(file))
        except IndexError:
            print(str(file)+' already in grayscale')
            continue

        scipy.misc.imsave(file,file_gray)