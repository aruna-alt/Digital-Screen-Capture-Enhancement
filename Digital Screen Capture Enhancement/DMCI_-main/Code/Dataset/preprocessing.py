import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img = mpimg.imread('CAT.jpg')
print("\nType of image\n")
print(type(img))
print("\nShape of image\n")
print(img.shape)
print("\nImage Matrix is as follows \n")
print(img)


img_plot = plt.imshow(img)
plt.show()


from PIL import Image 

img = Image.open('CAT.jpg')
img_resized = img.resize((180, 180))

img_resized.save('CAT_image_resized.jpg')

img_res = mpimg.imread('CAT_image_resized.jpg')
img_res_plot = plt.imshow(img_res)
plt.show()

print(img_res.shape)


import cv2

img = cv2.imread('CAT.jpg')

grayscale_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
print(type(grayscale_image))

print(grayscale_image.shape)

cv2.imshow(grayscale_image)

cv2.imwrite('GrayScale_CAT.jpg',grayscale_image)
