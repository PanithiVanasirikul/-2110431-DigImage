import cv2
import numpy as np
from matplotlib import pyplot as plt


def homework3_2_count_spores(image_bgr):
    # input: image_bgr - is a bgr image read by opencv lib
    # output: (1) resulted_image is a bgr image with counted spores labelled
    #         (2) num_count is number of spore counted by your code
    img_rgb = image_bgr
    img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    ret, th1 = cv2.threshold(img, 80, 130, cv2.THRESH_BINARY_INV)
    th1 = (th1 != 0).astype(np.uint8)
    kernel = np.ones((25, 25), np.uint8)
    # You need to choose 4 or 8 for connectivity type
    opening = cv2.morphologyEx(th1, cv2.MORPH_OPEN, kernel)
    connectivity = 4
    output = cv2.connectedComponentsWithStats(
        opening, connectivity, cv2.CV_32S)
    # Get the results
    # The first cell is the number of labels
    num_labels = output[0]-1
    # The second cell is the label matrix
    labels = output[1]
    # The third cell is the stat matrix
    stats = output[2]
    # The fourth cell is the centroid matrix
    centroids = output[3]
    for i in range(1, num_labels+1):
        cv2.rectangle(img_rgb, (int(centroids[i][0])-70, int(centroids[i][1])-70), (int(
            centroids[i][0])+70, int(centroids[i][1])+70), (255, 0, 0), 6)
        cv2.putText(img_rgb, str(i), (int(centroids[i][0])-70, int(
            centroids[i][1])-70-10), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
    print(num_labels)
    num_count = num_labels
    resulted_image = img_rgb[:, :, ::-1]

    return resulted_image, num_count

# write your own function here (if needed)