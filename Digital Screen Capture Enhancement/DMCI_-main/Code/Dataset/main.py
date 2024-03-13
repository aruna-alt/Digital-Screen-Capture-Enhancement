import cv2
import numpy as np

def remove_moire(input_image_path):
    # Load the input image
    input_image = cv2.imread(input_image_path)

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce high-frequency details
    blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)

    # Apply FFT to the blurred image
    f_transform = np.fft.fft2(blurred_image)
    f_transform_shifted = np.fft.fftshift(f_transform)

    # Create a mask to filter out the moiré pattern's frequencies
    mask = np.ones_like(blurred_image)
    mask[200:300, 200:300] = 0  # Adjust these coordinates as needed

    # Apply the mask in the frequency domain
    filtered_f_transform = f_transform_shifted * mask

    # Inverse FFT to get the filtered image
    filtered_image = np.abs(np.fft.ifft2(np.fft.ifftshift(filtered_f_transform)))

    # Normalize the filtered image
    filtered_image = cv2.normalize(filtered_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    return filtered_image

# Specify the path to your input image
input_image_path = 'CAT.jpg'

# Call the remove_moire function to process the image
result_image = remove_moire(input_image_path)

# Display the original and processed images
cv2.imshow('Original Image', cv2.imread(input_image_path))
cv2.imshow('Processed Image', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('image_Processed_CAT.jpg',result_image)
