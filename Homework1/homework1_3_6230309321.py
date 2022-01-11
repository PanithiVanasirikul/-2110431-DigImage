import cv2
import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(6)
fig.tight_layout()

plt.xlim([0, 256])

def plot_hist(img, ax, title):
    chans = cv2.split(img)
    colors = ("b", "g", "r")
    for (chan, color) in zip(chans, colors):
    # create a histogram for the current channel and plot it
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        ax.plot(hist, color=color)
    ax.set_title(title)

img1 = cv2.imread("kitty.jpg")
img2 = 64*np.ones(img1.shape, dtype=np.uint8)
img2[:,:,:] = np.array([5,10,20])

plot_hist(img1, axs[0], "img1 histogram")
plot_hist(img2, axs[1], "img2 histogram")

img_add = cv2.add(img1, img2)
plot_hist(img_add, axs[2], "add function")

img_sub = cv2.subtract(img1, img2)
plot_hist(img_sub, axs[3], "subtract function")

img_mul = cv2.multiply(img1, img2)
plot_hist(img_mul, axs[4], "multiply function")

img_div = cv2.divide(img1, img2)
plot_hist(img_div, axs[5], "divide function")

plt.show()