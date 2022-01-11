# import library here
import cv2
import matplotlib.pyplot as plt
def homework1_2(rgbimage):
    # input -> rgbimage - type -> np.ndarray, size of - (height, width, 3)
    # output -> filtered_image - type -> np.ndarray, size of - (height, width, 3)
    
    # TO DO - Design your own filter
  threshold = 128;
  for i in range(rgbimage.shape[0]):
      for j in range(rgbimage.shape[1]):
          x = rgbimage[i][j];
          rgbimage[i][j][0] = (x[0]>=threshold)*255;
          rgbimage[i][j][1] = (x[1]>=threshold)*255;
          rgbimage[i][j][2] = (x[2]>=threshold)*255;
  filtered_image = rgbimage;
  return filtered_image;