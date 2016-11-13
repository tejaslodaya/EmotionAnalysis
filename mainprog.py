import glob,os
from PIL import Image
import numpy
import pylab
from pca import pca
import matplotlib.image as mpi
import scipy.misc
import scipy.ndimage
import convert_rgb
import time
import sys

imlist=[]

convert=input('Do you want to convert images into grayscale? Type Y/N\n')
if(convert=='Y' or convert=='y'):
    convert_rgb.run_rgb()
elif(convert=='N' or convert=='n'):
    pass

for file in glob.glob("images\\*.jpg"):
    image=scipy.misc.imread(file)
    if(len(image.shape)<3):
        imlist.append(file)

print('\n'.join('{}: {}'.format(*k) for k in enumerate(imlist)))

sub1=[]
sub2=[]

print('\n****NOTE****')
print('1)The numbers on the left, correspond to the images on the right.')
print('2)After your\'e done, hit -1.')
print('3)Atleast one image necessary in each subspace')
print('4)Both subspaces should have same number of images.\n')

print('Pick images for 1st subspace.\n')
n=int(input('Enter number  '))
while(n!=-1):
    sub1.append(n)
    n=int(input('Enter number  '))

print('\nPick images for 2nd subspace.\n')
n=int(input('Enter number  '))
while(n!=-1):
    sub2.append(n)
    n=int(input('Enter number  '))

if(len(sub1)!=len(sub2)):
    print('ERROR:Both subspaces should have same number of images')
    sys.exit()
    

#create matrix to store all flattened images
immatrix1 = numpy.array([numpy.array(Image.open(imlist[i])).flatten() for i in sub1],'f')
immatrix2 = numpy.array([numpy.array(Image.open(imlist[i])).flatten() for i in sub2],'f')

#perform PCA
V0,immean0,EV0 = pca(immatrix1)
V1,immean1,EV1 = pca(immatrix2)

X=numpy.zeros_like(EV1)

for i in range(1):
    for j in range(1):
        total=numpy.float32(0.0)
        for k in range(1):
            total+=(numpy.inner(EV1[k],EV0[i])*numpy.inner(EV0[j],EV1[k]))
        
        X[i][j]=total

e,EV=numpy.linalg.eigh(X)
theta = numpy.rad2deg(numpy.arccos(numpy.sqrt(e)))
print(theta)

magic_value=theta[-1]


if(magic_value > 80 and magic_value < 90):
    print("Happy emotion detected with theta = ", magic_value)
    
elif(magic_value > 70 and magic_value< 80):
    print("Negative emoton detected with theta = ", magic_value)
    
else:
    print("No change in emotion")