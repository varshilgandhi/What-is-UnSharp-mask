# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 09:15:06 2021

@author: abc
"""

"""

Unsharp mask and how come 'unsharp' sharpens an image 

"""

import cv2
from skimage import io, img_as_float
from skimage.filters import unsharp_mask
from skimage.filters import gaussian

#read our image and convert it into floating point value
img = img_as_float(io.imread("einstein_blurred.jpg", as_gray=True))

#Define gaussian filter
gaussian_img = gaussian(img, sigma=1, mode='constant', cval=0.0)

#Apply Unsharp mask
amount = 1.0
img2 = (img - gaussian_img)*amount

img3 = img + img2

#show our image
cv2.imshow("Original image", img)
cv2.imshow("Blurred image", img2)
cv2.imshow("Unsharp mask image", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

########################################################

#Apply above thing into in real life
from skimage import io
from skimage.filters import unsharp_mask

#read our image
img = io.imread("einstein_blurred.jpg")

#Apply unsharp mask
unsharped_img = unsharp_mask(img, radius=3, amount=1.0)

#show our image
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img, cmap='gray')
ax1.title.set_text('Input Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(unsharped_img, cmap='gray')
ax2.title.set_text('Unsharped Image')

plt.show()



























