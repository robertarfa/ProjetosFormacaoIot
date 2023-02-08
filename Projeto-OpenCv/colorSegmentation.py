import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import sys

image = cv.imread(
    '/content/drive/MyDrive/Colab Notebooks/green-grass-and-blue-sky.jpg', cv.IMREAD_UNCHANGED)

bgr_im = image
rgb_im = cv.cvtColor(bgr_im, cv.COLOR_BGR2RGB)

figsize = (10, 10)
plt.figure(figsize=figsize)
plt.imshow(rgb_im)

plt.title("original image")
plt.show()

# Separar grama da imagem => RGB to HSV
# 3d array just because this is what cvtColor expects...
rgb_green = np.uint8([[[0, 255, 0]]])

hsv_green = cv.cvtColor(rgb_green, cv.COLOR_RGB2HSV)[0, 0, :]

print(hsv_green)

# Printar apenas o que for proximo de verde
# Convert rgb to hsv
hsv_im = cv.cvtColor(rgb_im, cv.COLOR_RGB2HSV)

# define range of hue and intensity
lower_th = hsv_green - np.array([70, 200, 200])
upper_th = hsv_green + np.array([30, 0, 0])

# Threshold the HSV image
mask = cv.inRange(hsv_im, lower_th, upper_th)

plt.figure(figsize=figsize)
plt.imshow(mask)
plt.title("result mask")
plt.show()

# Trick: apply 2d mask on 3d image
rgb_res = cv.bitwise_and(rgb_im, rgb_im, mask=mask)

plt.figure(figsize=figsize)
plt.imshow(rgb_res)
plt.title("output image")
plt.show()
