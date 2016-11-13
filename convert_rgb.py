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
    for file in glob.glob("*.jpg"):

        imlist.append(file)
        file_name=''
        file_ext=''
        spot_dot=False
        for i in range(len(file)):
            if(file[i]=='.'):
                spot_dot=True
            else:
                if(spot_dot==False):
                    file_name+=file[i]
                else:
                    file_ext+=file[i]

        try:
            file_gray = rgb2gray(scipy.ndimage.imread(file))
        except IndexError:
            print('File '+file_name+' already in grayscale')
            continue

        scipy.misc.imsave(file_name+'_gray.'+file_ext,file_gray)

    print('Images converted into grayscale')