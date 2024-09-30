import cv2

# Load an image
image = cv2.imread('/home/ahmed/ros2/opencv_python/image.jpg')

# Display the image
cv2.imshow('Hello World', image)
if image is None:
    print("Error: Could not load image.")
else:
    # Wait until a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()