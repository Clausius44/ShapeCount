
import matplotlib.pyplot as plt
from Utils import drawSquare
import os

size = [10, 10]
fig, ax = plt.subplots(figsize=size)

numberOfSquares = 15
for square in range(1, numberOfSquares+1):
    limitImageNum = 1000
    for imageNum in range(limitImageNum):
        vecOfCoordinates = []
        for num in range(square):
            drawSquare(ax, vecOfCoordinates)

        ax.set_xlim(0, size[0])
        ax.set_ylim(0, size[1])
        plt.axis("off")
        nameToSave = f"SQUARES_{square}_IMAGE_{imageNum}.jpg"

        plt.savefig(os.path.join(r"C:\Users\User\PycharmProjects\ShapeCount\IMAGES", nameToSave))
        ax.clear()
