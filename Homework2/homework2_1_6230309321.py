from math import log10, sqrt
from skimage import io,color
import cv2
import matplotlib.pyplot as plt
import numpy as np
image1 = cv2.imread("kitty55.png",0)
F = np.fft.fft2(image1)
FShift = np.fft.fftshift(F)
magnitude_spectrum = np.log(1+np.abs(FShift))

c = 27
ny, nx = image1.shape
x = np.linspace(-nx/2, nx/2-1, nx)
y = np.linspace(-ny/2, ny/2-1, ny)
new_x = np.array([list(x)]*ny)
new_y = np.array([list(y)]*nx).T

gaussian_filter = np.exp(-(new_x**2+new_y**2)/(2*(c**2)))

img_ft_filter = FShift*gaussian_filter
fshift_power = (np.abs(FShift)**2).sum()
filter_power = (np.abs(img_ft_filter)**2).sum()

alpha = 100*(filter_power/fshift_power)
print(c)
print(alpha)

f_ishift = np.fft.ifftshift(img_ft_filter)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.imshow(image1, cmap = 'gray'); plt.title("Original Image")
plt.show()
plt.imshow(magnitude_spectrum, cmap='gray'); plt.title("Fourier Spectrum of the Original Image")
plt.show()
plt.imshow(gaussian_filter, cmap = 'gray'); plt.title("Fourier Spectrum of the Filtered Image")
plt.show()
plt.imshow(img_back.astype(np.uint8), cmap = 'gray'); plt.title('Filtered image');
plt.show()