
import os
import cv2
from Utils import applyConvolution

workFolder = "IMAGES"

count = 1
dictOfInputs = {}
for file in os.listdir(workFolder):

    image = cv2.imread(os.path.join(workFolder, file))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (100, 100))
    image = image/255
    dictOfInputs[file] = image
    print(count)
    count += 1
