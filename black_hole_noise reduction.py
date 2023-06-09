import os
import cv2
import numpy as np

images_path = os.listdir("input/black_hole/4")

images =[]
for image_path in images_path:
    image = cv2.imread("input/black_hole/4/" + image_path)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = image.astype(np.float32)
    images.append(image)

result = np.zeros(image.shape)

for image in images:
    result += image

result = result / len(images)
result = result.astype(np.uint8)

cv2.imshow("result", result)
cv2.imwrite("output/black_hole/good_black_hole4.jpg", result)
cv2.waitKey()


