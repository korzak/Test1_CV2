import cv2

image = cv2.imread(r'C:\Users\XE\Documents\SRC\Test1CV2\test1CV2\image.jpeg')

# Display the image in a window
cv2.imshow('Image', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

#r'C:\Users\XE\Documents\SRC\Test1CV2\test1CV2\image.jpeg'