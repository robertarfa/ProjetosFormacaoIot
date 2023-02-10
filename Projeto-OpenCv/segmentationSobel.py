import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img = cv.imread('leao2.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = cv.GaussianBlur(gray, (3, 3), 0)

sobelx = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)

sobely = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5)

sobelxy = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)

plt.figure(figsize=(18, 19))

plt.subplot(221)
plt.imshow(img, cmap='gray')
plt.title('original')
plt.axis('off')

plt.subplot(222)
plt.imshow(sobelxy, cmap='gray')
plt.title('Sobel X Y')
plt.axis('off')

plt.subplot(223)
plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X')
plt.axis('off')

plt.subplot(224)
plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y')
plt.axis('off')
