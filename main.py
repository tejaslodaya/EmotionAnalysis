import pygame
import pygame.camera
from pygame.locals import *
import pygame.image
import pygame.time
import time
import convert_rgb

import glob,os,shutil
from PIL import Image
import numpy
from pca import pca

pygame.init()
pygame.camera.init()

camlist=pygame.camera.list_cameras()
if not camlist:
	raise ValueError("Sorry, no cameras detected.")

############FIRST SUBSPACE#############
proceed=raw_input("Capturing images for first subspace. Do you want to proceed?(Y/n)")
if(proceed=='N' or proceed=='n'):
	raise Exception("Aborted")

#Recreate directories
if(os.path.isdir('firstsub')):
	shutil.rmtree('firstsub')
os.mkdir('firstsub',0777)

for i in range(10):
	
	print("Capturing Image "+str((i+1))+". Say cheese!")
	pygame.time.delay(2000)

	cam=pygame.camera.Camera(camlist[0],(640,480))
	cam.start()
	img=cam.get_image() #Snap!
	print("Snap!")
	cam.stop()

	pygame.image.save(img,'firstsub/'+str(i+1)+".jpg")
	
	pygame.time.delay(4000)

############SECOND SUBSPACE##############
proceed=raw_input("Capturing images for second subspace. Do you want to proceed?(Y/n)")
if(proceed=='N' or proceed=='n'):
	raise Exception("Aborted")

#Recreate directories
if(os.path.isdir('secondsub')):
	shutil.rmtree('secondsub')
os.mkdir('secondsub',0777)

for i in range(10):
	
	print("Capturing Image "+str((i+1))+". Say cheese!")
	pygame.time.delay(2000)

	cam=pygame.camera.Camera(camlist[0],(640,480))
	cam.start()
	img=cam.get_image() #Snap!
	print("Snap!")
	cam.stop()

	pygame.image.save(img,'secondsub/'+str(i+1)+".jpg")
	
	pygame.time.delay(4000)

pygame.camera.quit()

convert_rgb.run_rgb() #Convert rgb to black/white

###########OLD CODE#########

#create matrix to store all flattened images
immatrix1 = numpy.array([numpy.array(Image.open(file)).flatten() for file in glob.glob("firstsub/*.jpg")],'f')
immatrix2 = numpy.array([numpy.array(Image.open(file)).flatten() for file in glob.glob("secondsub/*.jpg")],'f')

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

magic_value=theta[-1]
print(theta)

if(magic_value > 80 and magic_value < 90):
    print("Happy emotion detected with theta = ", magic_value)
elif(magic_value > 70 and magic_value< 80):
    print("Negative emoton detected with theta = ", magic_value)
else:
    print("No change in emotion")