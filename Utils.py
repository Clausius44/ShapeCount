
import random
import cv2
from ColorList import colorList
import numpy as np

def drawSquare(ax, vec):

    overlap = True
    while overlap == True:
        # Generate two random points for the square
        corner1 = [random.uniform(0, 10), random.uniform(0, 10)]
        corner2 = [random.uniform(0, 10), random.uniform(0, 10)]

        # Save the coordinates in a sorted way.
        left = min(corner1[0], corner2[0])
        right = max(corner1[0], corner2[0])
        top = max(corner1[1], corner2[1])
        bottom = min(corner1[1], corner2[1])

        topLeft = [left, top]
        topRight = [right, top]
        bottomLeft = [left, bottom]
        bottomRight = [right, bottom]

        # Check if there is overlap with squares
        overlap = checkSquareInside([topLeft, topRight, bottomLeft, bottomRight], vec)

    # Get a random color and plot the square
    color = random.choice(colorList)
    ax.hlines(top, left, right, linewidth=5, color=color)
    ax.hlines(bottom, left, right, linewidth=5, color=color)
    ax.vlines(left,  bottom, top, linewidth=5, color=color)
    ax.vlines(right, bottom, top, linewidth=5, color=color)

    # Save the coordinates in a sorted way.
    left = min(corner1[0], corner2[0])
    right = max(corner1[0], corner2[0])
    top = max(corner1[1], corner2[1])
    bottom = min(corner1[1], corner2[1])

    topLeft = [left, top]
    topRight = [right, top]
    bottomLeft = [left, bottom]
    bottomRight = [right, bottom]

    vec.append([topLeft, topRight, bottomLeft, bottomRight])

def checkSquareInside(pos, vec):

    newLeft = pos[0][0]
    newRight = pos[1][0]
    newTop = pos[0][1]
    newBottom = pos[2][1]

    for square in vec:
        checkLeft = square[0][0]
        checkRight = square[1][0]
        checkTop = square[0][1]
        checkBottom = square[2][1]

        if not (newLeft > checkRight or
                newRight < checkLeft or
                newTop < checkBottom or
                newBottom > checkTop
                ):
            return True
    return False

def applyConvolution(image, kernelSize):

    kernel = np.ones((kernelSize, kernelSize), np.float32) / (kernelSize ** 2)

    result = cv2.filter2D(image, -1, kernel)

    return result