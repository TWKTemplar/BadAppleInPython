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
    pixel_data = list(img.getdata())
    # Make Image
    grid = np.zeros((img.height,img.width))
    for x in range(img.height):  # up and down
        for y in range(img.width):#left n right
            pixelBool = GetPixel(x,y,pixel_data, img.height, img.width)
            grid[x, y] = pixelBool
            print("x: "+ str(x) + " y: " + str(y) + " bool: " + str(pixelBool))
    SaveImage(grid)


def GetPixel(x, y, pixel_data, imgHeight, imgWidth):
    pixel_value = pixel_data[x * imgWidth + y]
    if ((sum(pixel_value) / 3 ) > 128):
        return 1  # Return 1 if pixel is bright
    return 0  # Return 0 if pixel is dark


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