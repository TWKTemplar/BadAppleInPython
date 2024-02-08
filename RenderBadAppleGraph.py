from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import random
import math
import time
def Render(imgpath):
    # Get Data
    img = Image.open(imgpath)
    appleImageData = list(img.getdata())
    # Make Image
    graph = np.zeros((img.height,img.width))
    for x in range(img.height):  # up and down
        for y in range(img.width):#left n right
            graph[x, y] = GetPixel(x, y, appleImageData, img.width, graph[x, y])

    SaveImage(graph)
def GetPixel(x, y, pixel_data, imgWidth, currentPixel):
    appleImageValueRGB = pixel_data[x * imgWidth + y]
    targetVal = int(((sum(appleImageValueRGB) / 3 ) > 128))
    if (currentPixel == targetVal):
        return currentPixel
    ra = random.randint(0,1)
    rb = random.randint(0, 1)
    rc = random.randint(0, 1)
    rd = random.randint(0, 1)
    if (currentPixel == 0):
        return (ra*rb*rc*rd)
    if (currentPixel == 1):
        return (ra*rb*rc*rd)
def SaveImage(grid):
    plt.imshow(grid, vmin=0, vmax=1)  # Assuming binary grid, using grayscale colormap
    #plt.axis('off')  # Turn off axis
    if not os.path.exists("Render"):
        os.makedirs("Render")
    plt.savefig("Render/apple.png", dpi=300, bbox_inches='tight', pad_inches=0)  # Save the image
def GetSourceImagePath():
    if not os.path.exists("BadApple"):
        os.makedirs("BadApple")
    imageFolder = "BadApple"
    imageName = "86"
    imagePath = os.path.join(imageFolder, imageName + ".png")
    return imagePath
Render(GetSourceImagePath())