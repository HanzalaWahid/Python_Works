import cv2
import numpy as np

# Provide the correct file path to your image file
img_path = r"C:\Users\kk\Pictures\Saved Pictures\photo2-1618835962148-cf177563c6c0.jpg"

# Load the image
img = cv2.imread(img_path)

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not found or could not be loaded.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    # Apply bilateral filter to maintain colors while reducing noise
    color = cv2.bilateralFilter(img, 9, 3000, 3000)

    # Create the cartoon effect
    cartoon = cv2.bitwise_and(color, color, mask=gray)

    cv2.imshow("Original Image", img)
    cv2.imshow("Cartoon", cartoon)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
