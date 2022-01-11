
# Do not change any code in this file. You can add your code only on the areas provided

import cv2
import numpy as np
from matplotlib import pyplot as plt
# import other libraries here


# To count all objects in an input image
def count_all_objs(image_bgr):
  # input: image_bgr - is a bgr image read by opencv lib
  # output: (1) num_count is the number of all objects in image_bgr
  #         (2) result_image is a bgr image (your own design) to visualize the results PROPERLY.
  
  # write your code here
  
  return num_count, result_image 


# To count the number of circles in an input image
def count_circles(image_bgr):
  # input: image_bgr - is a bgr image read by opencv lib
  # output: (1) num_count is the number of circles in image_bgr
  #         (2) result_image is a bgr image (your own design) to visualize the results PROPERLY.

  # write your code here


  return num_count, result_image 


# To count the number of small-size circles in an input image
def count_small_circles(image_bgr):
  # input: image_bgr - is a bgr image read by opencv lib
  # output: (1) num_count is the number of small circles in image_bgr
  #         (2) result_image is a bgr image (your own design) to visualize the results PROPERLY.

  # write your code here


  return num_count, result_image 


# To count the number of medium-size circles in an input image
def count_med_circles(image_bgr):
  # input: image_bgr - is a bgr image read by opencv lib
  # output: (1) num_count is the number of medium-size circles in image_bgr
  #         (2) result_image is a bgr image (your own design) to visualize the results PROPERLY.

  # write your code here


  return num_count, result_image 

# To count the number of large-size circles in an input image
def count_large_circles(image_bgr):
  # input: image_bgr - is a bgr image read by opencv lib
  # output: (1) num_count is the number of large circles in image_bgr
  #         (2) result_image is a bgr image (your own design) to visualize the results PROPERLY.

  # write your code here


  return num_count, result_image 

# To count the number of triangles in an input image
def count_triangles(image_bgr):
  # input: image_bgr - is a bgr image read by opencv lib
  # output: (1) num_count is the number of triangles in image_bgr
  #         (2) result_image is a bgr image (your own design) to visualize the results PROPERLY.

  # write your code here


  return num_count, result_image 

# To count the number of rectangles in an input image
def count_rectangles(image_bgr):
  # input: image_bgr - is a bgr image read by opencv lib
  # output: (1) num_count is the number of rectangles in image_bgr
  #         (2) result_image is a bgr image (your own design) to visualize the results PROPERLY.

  # write your code here



  return num_count, result_image 

# To count the number of umbrellas in an input image
def count_umbrella(image_bgr):
  # input: image_bgr - is a bgr image read by opencv lib
  # output: (1) num_count is the number of umbrellas in image_bgr
  #         (2) result_image is a bgr image (your own design) to visualize the results PROPERLY.

  # write your code here



  return num_count, result_image 




# write your own function here (if needed)





# uncomment to test your program 
# img_rgb = cv2.imread("0000.png")
# num_count,result_image = count_all_objs(img_rgb)
# plt.imshow(result_image[:,:,::-1]);plt.show()
# print("Num of all objects: ", num_count)
# num_count,result_image = count_circles(img_rgb)
# print("Num of circles: ", num_count)
# num_count,result_image = count_small_circles(img_rgb)
# print("Num of small circles: ", num_count)
# num_count,result_image = count_med_circles(img_rgb)
# print("Num of medium circles: ", num_count)
# num_count,result_image = count_large_circles(img_rgb)
# print("Num of large circles: ", num_count)
# num_count,result_image = count_rectangles(img_rgb)
# print("Num of rectangles: ", num_count)
# num_count,result_image = count_triangles(img_rgb)
# print("Num of triangles: ", num_count)
# num_count,result_image = count_umbrella(img_rgb)
# print("Num of umbrella: ", num_count)
# print("----------------------------------------------")