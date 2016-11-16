from PIL import Image
from numpy import *

def pca(X):
  num_data,dim = X.shape

  mean_X = X.mean(axis=0)
  for i in range(num_data):
      X[i] -= mean_X

  M = dot(X,X.T)
  e,EV = linalg.eigh(M)
  
  tmp = dot(X.T,EV).T
  
  V = tmp[::-1]

  return V,mean_X,EV
