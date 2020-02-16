import cv2
import matplotlib.pyplot as plt
import numpy as np

path = "./storage/default_images/template.png"
icon = "./storage/default_images/rippro_logo_small.png"

img1 = cv2.imread(path)
img2 = cv2.imread(icon)

plt.imshow(img1)
plt.imshow(img2)

img2 = cv2.resize(img2,(190,190))
 
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
 
large_img = img1
small_img = img2

x_offset=35
y_offset=204
large_img[y_offset:y_offset+small_img.shape[0], x_offset:x_offset+small_img.shape[1]] = small_img

plt.imshow(large_img)
plt.show()