# import library here
import cv2
import matplotlib.pyplot as plt


def homework1_1(image_grayscale):
    # input -> image_grayscale - type -> np.ndarray, size of - (height, width)
    # output -> image_grayscale - type -> np.ndarray, size of - (height, width)
    
    # TO DO - Implement transformation based on the contrast stretching graph
  Image = image_grayscale.copy();
  r1 = 85.3;
  s1 = 32;
  r2 = 160;
  s2 = 224;
  for i in range(image.shape[0]):
    for j in range(image.shape[1]):
      x = image[i][j];
      image[i][j] = (x<=r1)*(x*s1/r1) + (x>r1 and x<=r2)*(x*(s2-s1)/(r2-r1)) + (x > r2)*(x*(255-s2)/(255-r2))
  filtered_image = image;
    
  return filtered_image
