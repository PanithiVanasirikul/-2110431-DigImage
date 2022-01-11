from math import log10, sqrt
from skimage import io,color
import cv2
import matplotlib.pyplot as plt
import numpy as np
def PSNR(original, compressed):
  mse = np.mean((original-compressed)**2)
  if(mse==0):
    return 100
  max_pixel = 255.0
  psnr = 20*log10(max_pixel/sqrt(mse))
  return psnr
image1 = cv2.imread("kitty55.png",0)
image2 = cv2.imread("noisy_kitty55.png",0)
F = np.fft.fft2(image1)
FShift = np.fft.fftshift(F)
magnitude_spectrum = np.log(1+np.abs(FShift))
plt.imshow(magnitude_spectrum, cmap='gray')
plt.show()

F = np.fft.fft2(image2)
FShift = np.fft.fftshift(F)
magnitude_spectrum = np.log(1+np.abs(FShift))
plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.show()
nx, ny = image1.shape
y = np.linspace(-nx/2,nx/2,nx)
x = np.linspace(-ny/2,ny/2,ny)
xv, yv = np.meshgrid(x,y) 
radiusCoor = np.sqrt(xv**2 + yv**2)
r1 = radiusCoor < 135
r2 = radiusCoor >= 170
mask1 = np.ones([nx,ny])
bandReject = cv2.bitwise_or(r1.astype(np.uint8),r2.astype(np.uint8),mask=mask1.astype(np.uint8))
plt.imshow(bandReject,cmap='gray')
plt.show()
img_bandReject = bandReject * FShift
img_ft_filter_hp_spectrum = np.log(1+np.abs(img_bandReject))
plt.imshow(img_ft_filter_hp_spectrum)
plt.show()
f_ishift_br = np.fft.ifftshift(img_bandReject)
img_restored = np.fft.ifft2(f_ishift_br)
img_restored = np.abs(img_restored)
print(PSNR(image1,image2))
print(PSNR(image1,img_restored))
plt.imshow(image1, cmap = 'gray',vmin = 0, vmax = 255); plt.title('original'); plt.show()
plt.imshow(image2, cmap = 'gray',vmin = 0, vmax = 255); plt.title('with noise'); plt.show()
plt.imshow(img_restored, cmap ='gray',vmin = 0, vmax = 255);plt.title('image after restored'); plt.show()