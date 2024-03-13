import cv2
import numpy as np

# Load the input image
input_image = cv2.imread('CAT.jpg')

# Resize the image to a smaller size
resize_factor = 0.5
resized_image = cv2.resize(input_image, None, fx=resize_factor, fy=resize_factor)

# Apply Gaussian blur to reduce high-frequency details (Moiré patterns)
blur_radius = 5
blurred_image = cv2.GaussianBlur(resized_image, (blur_radius, blur_radius), 0)

# Apply a median filter to further reduce noise and patterns
median_filtered_image = cv2.medianBlur(blurred_image, 5)

# Display the preprocessed image
cv2.imshow('Preprocessed Image', median_filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the preprocessed image
cv2.imwrite('preprocessed_image_CAT.jpg', median_filtered_image)
