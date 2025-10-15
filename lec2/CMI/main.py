import cv2 as cv
import numpy as np

K = input("How many colors?: ")
K = int(K)

img = cv.imread("images/TCF.jpg")
cv.imshow("test!!", img)
cv.waitKey(0)

img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
original_shape = img.shape
img = img.reshape(-1, 3)

criteria = (cv.TERM_CRITERIA_MAX_ITER + cv.TERM_CRITERIA_EPS, 10, 1.0)
_, labels, centers = cv.kmeans(data=img.astype(np.float32), K=K, bestLabels=None, criteria=criteria, attempts=10, flags=cv.KMEANS_RANDOM_CENTERS)


black = np.ndarray([3], dtype=np.float32)

print(img[0])

for i in range(K):
    imgprime = []
    for j in range(len(labels)):
        if labels[j] == i:
            imgprime.append(img[j])
        else:
            imgprime.append(black)
    # imgprime = [centers[j] if j == i else black for j in labels]
    imgprime = np.array(imgprime)
    imgprime = imgprime.reshape(original_shape).astype(np.uint8)
    
    imgprime = cv.cvtColor(imgprime, cv.COLOR_HSV2BGR)
    cv.imshow(str(i), imgprime)
    cv.waitKey(0)

img = centers[labels].reshape(original_shape).astype(np.uint8)
img = cv.cvtColor(img, cv.COLOR_HSV2BGR)

cv.imshow("test2", img)
cv.waitKey(0)

