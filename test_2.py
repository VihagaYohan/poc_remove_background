import cv2
import numpy as np
import os

# Directory where the images are stored
ASSETS_DIR = "assets"

def remove_background(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a binary threshold to get a binary image
    _, thresholded = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Invert the binary image (object should be white, background black)
    inverted = cv2.bitwise_not(thresholded)

    # Find contours from the inverted image
    contours, _ = cv2.findContours(inverted, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create an empty mask
    mask = np.zeros_like(image)

    # Draw the contours on the mask
    cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

    # Apply the mask to the image (bitwise_and keeps only the object)
    result = cv2.bitwise_and(image, mask)

    # Save the result
    cv2.imwrite(output_path, result)

    return output_path

# Function to process all images in the asset folder
def process_images():
    for filename in os.listdir(ASSETS_DIR):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(ASSETS_DIR, filename)
            output_path = os.path.join(ASSETS_DIR, 'output', 'no_bg_' + filename)

            # Remove the background
            remove_background(image_path, output_path)
            print(f"Processed: {output_path}")

if __name__ == "__main__":
    process_images()