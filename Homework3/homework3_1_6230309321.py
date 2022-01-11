from math import log10, sqrt
from skimage import io, color
import cv2
import matplotlib.pyplot as plt
import numpy as np


def homework3_1_read_a_simple_clock(image_gray):
    # input: image_gray - is a gray image read by opencv lib
    # output: displayed_time in HH:MM format where HH is hour and MM is minutes
    displayed_time = "00:00"
    img = image_gray
    img = 255-img
    img = img*bandpass(img)
    connectivity = 4
    output = cv2.connectedComponentsWithStats(img, connectivity, cv2.CV_32S)
    # Get the results
    # The first cell is the number of labels
    num_labels = output[0]-1
    # The second cell is the label matrix
    labels = output[1]
    # The third cell is the stat matrix
    stats = output[2]
    # The fourth cell is the centroid matrix
    centroids = output[3]

    img0 = (labels == 1).astype(np.uint8)*255
    img1 = (labels == 2).astype(np.uint8)*255
    if img0.sum() > img1.sum():
        long_pointer = img0
        short_pointer = img1
    else:
        long_pointer = img1
        short_pointer = img0

    edges = cv2.Canny(long_pointer, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 10, np.pi/180, 0)

    linesdegree = lines.copy()
    linesdegree[:, 0:1, 1:2] = linesdegree[:, 0:1, 1:2]*180/np.pi

    for i in range(0, 2):
        plt.scatter(linesdegree[i, 0:1, 1:2], linesdegree[i, 0:1, 0:1])

    print("zeta=", linesdegree[0, 0:1, 1:2])
    print("low=", linesdegree[0, 0:1, 0:1])

    zeta_long = linesdegree[0, 0:1, 1:2]

    edges = cv2.Canny(short_pointer, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 10, np.pi/180, 0)

    linesdegree = lines.copy()
    linesdegree[:, 0:1, 1:2] = linesdegree[:, 0:1, 1:2]*180/np.pi

    for i in range(0, 2):
        plt.scatter(linesdegree[i, 0:1, 1:2], linesdegree[i, 0:1, 0:1])

    print("zeta=", linesdegree[0, 0:1, 1:2])
    print("low=", linesdegree[0, 0:1, 0:1])

    zeta_short = linesdegree[0, 0:1, 1:2]
    # checkSpectrum1: 0 = à¸à¸±à¹ˆà¸‡à¸‹à¹‰à¸²à¸¢à¸¥à¹ˆà¸²à¸‡ 1 = à¸à¸±à¹ˆà¸‡à¸‚à¸§à¸²à¸šà¸™
    # checkSpectrum2: 0 = à¸à¸±à¹ˆà¸‡à¸‹à¹‰à¸²à¸¢à¸šà¸™ 1 = à¸à¸±à¹ˆà¸‡à¸‚à¸§à¸²à¸¥à¹ˆà¸²à¸‡

    bool_short1 = checkSpectrum1(short_pointer)
    bool_long1 = checkSpectrum1(long_pointer)

    bool_short2 = checkSpectrum2(short_pointer)
    bool_long2 = checkSpectrum2(long_pointer)

    if(zeta_long <= 90 and zeta_long > 0):
        if(bool_long1):
            print(zeta_long)
        else:
            zeta_long = zeta_long+180
            print(zeta_long)
    else:
        if(bool_long2):
            print(zeta_long)
        else:
            zeta_long = zeta_long+180
            print(zeta_long)
    if(zeta_short <= 90 and zeta_short > 0):
        if(bool_short1):
            print(zeta_short)
        else:
            zeta_short = zeta_short+180
            print(zeta_short)
    else:
        if(bool_short2):
            print(zeta_short)
        else:
            zeta_short = zeta_short+180
            print(zeta_short)

    print(int(zeta_short//30), int(zeta_long//6))

    short = str(int(zeta_short//30)).zfill(2)

    long = str(int(zeta_long//6)).zfill(2)

    displayed_time = short+":"+long

    return displayed_time

# write your own function here (if needed)


def bandpass(img):
    nx, ny = img.shape
    y = np.linspace(-nx/2, nx/2, nx)
    x = np.linspace(-ny/2, ny/2, ny)
    xv, yv = np.meshgrid(x, y)
    radiusCoor = np.sqrt(xv**2 + yv**2)
    r1 = radiusCoor < 13
    r2 = radiusCoor >= 120
    mask1 = np.ones([nx, ny])
    return 1-cv2.bitwise_or(r1.astype(np.uint8), r2.astype(np.uint8), mask=mask1.astype(np.uint8))


def checkSpectrum1(pointer):
    sum_first = 0
    for i in range(300):
        for j in range(i, 300):
            sum_first += (pointer[i][j] == 255)
    sum_second = 0
    for i in range(300):
        for j in range(0, i):
            sum_second += (pointer[i][j] == 255)
    if sum_first > sum_second:
        return 1
    return 0


def checkSpectrum2(pointer):
    sum_first = 0
    for i in range(300):
        for j in range(300-i, 300):
            sum_first += (pointer[i][j] == 255)
    sum_second = 0
    for i in range(300):
        for j in range(0, 300-i):
            sum_second += (pointer[i][j] == 255)
    if sum_first > sum_second:
        return 1
    return 0