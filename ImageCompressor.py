
import os
import cv2
import json

imageFolder = "IMAGES"

count = 1
dictOfInputs = {}
for file in os.listdir(imageFolder):

    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
        image = cv2.imread(os.path.join(imageFolder, file))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (100, 100))
        image = image/255

        dictOfInputs[file] = image.tolist()

with open(os.path.join(imageFolder,"Database.json"), "w") as jsonFile:
    json.dump(dictOfInputs, jsonFile, indent=4)
