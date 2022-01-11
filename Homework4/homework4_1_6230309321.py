import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt
# Import library here


def rotated(image, angle):
  return imutils.rotate(image, angle=angle)

# Add other augmentation functions here
def horizontal_flip(img):
  return cv2.flip(img,1)
def vertical_flip(img):
  return cv2.flip(img,0)
def brightness(img,float_brightness):
  hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
  hsvImg[...,2] = hsvImg[...,2]*float_brightness
  img = cv2.cvtColor(hsvImg,cv2.COLOR_HSV2RGB)
  return img
def translateImg(img, offsetx, offsety):
  height, width = img.shape[:2]
  T = np.float32([[1, 0, offsetx], [0, 1, offsety]])
  return cv2.warpAffine(img, T, (width,height))


image = cv2.imread("kitty.jpg")
plt.imshow(image[:,:,::-1]);plt.title("original")
plt.show()

angle = 30
img_30 = rotated(image,angle)
plt.imshow(img_30[:,:,::-1]);plt.title("rotated by "+str(angle))
plt.show()

# show how to use your function and show your modified versions of the original image here
kitty = image
collie = cv2.imread('collie.jpg')

kitty_2 = translateImg(kitty,30,0)
plt.imshow(kitty_2[:,:,::-1])
plt.show()

collie_2 = translateImg(collie,30,0)
plt.imshow(collie_2[:,:,::-1])
plt.show()

kitty_3 = translateImg(kitty,0,30)
plt.imshow(kitty_3[:,:,::-1])
plt.show()

collie_3 = translateImg(collie,0,30)
plt.imshow(collie_3[:,:,::-1])
plt.show()

kitty_4 = horizontal_flip(kitty)
plt.imshow(kitty_4[:,:,::-1])
plt.show()

collie_4 = horizontal_flip(collie)
plt.imshow(collie_4[:,:,::-1])
plt.show()

kitty_5 = vertical_flip(kitty)
plt.imshow(kitty_5[:,:,::-1])
plt.show()

collie_5 = vertical_flip(collie)
plt.imshow(collie_5[:,:,::-1])
plt.show()

kitty_6 = brightness(kitty,0.9)
plt.imshow(kitty_6[:,:,::-1])
plt.show()

collie_6 = brightness(collie,0.9)
plt.imshow(collie_6[:,:,::-1])
plt.show()