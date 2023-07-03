#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2

# Load .png image
image = cv2.imread('C:\\Users\jyotp\OneDrive\Pictures\Screenshots\Screenshot 2023-07-03 160604.png')

# Save .jpg image
cv2.imwrite('image.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])


# In[5]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('image.jpg')
plt.imshow(img)
plt.show()


# In[ ]:




