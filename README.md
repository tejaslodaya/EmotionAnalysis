Emotion analysis of aggressive moods in automobile driving using mutual subspace method

Objectives:

• Parameterize appearance changes of face image sequences using mutual subspace method,and estimation of level of aggression. 
• Mutual subspace method cancels out short-term variations (emotions), and retains long-term changes (mood) by using Principal Component Analysis.

Steps taken:

1) Calculate the reference subspace, where a series of driver's pictures are taken, say N. PCA is performed to scale down the dimensions of matrices. EigenVectors are obtained from pca of reference subspace, say EV0

2) Calculate subsequent subspaces each at time interval T, and at each interval, a series of pictures are buffered and PCA is performed on them. EigenVectors obtained are denoted as EV1.

3) Using mutual subspace method, we calculate the cosine of the angle between them. We classify θ into 3 classes: 
  • θ > 80 and θ < 90 : Happy emotion was detected
  • θ > 70 and θ < 80 : Negetive emotion was detected 
  • θ <70 : No change in emotion

4) Play music accordingly, to soothen the driver's mood.

Implementation of the paper: http://ieeexplore.ieee.org/document/6460771/
