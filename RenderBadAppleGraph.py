from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import random
def Render(numberOfImagesToRender):
    if(numberOfImagesToRender <=0):
        numberOfImagesToRender = 1
    count = 0
    appleimg = Image.open(GetInputImagePath(count))
    graph = np.zeros((appleimg.height, appleimg.width))
    for i in range(numberOfImagesToRender):
        appleimg = Image.open(GetInputImagePath(count))
        appleImageData = list(appleimg.getdata())
        for x in range(appleimg.height):
            for y in range(appleimg.width):
                graph[x, y] = GetPixel(x, y, appleImageData, appleimg.width, graph[x, y])
        SaveImage(graph, count)
        count += 1
def GetPixel(x, y, pixel_data, imgWidth, currentPixel):
    appleImageValueRGB = pixel_data[x * imgWidth + y]
    targetVal = int(((sum(appleImageValueRGB) / 3 ) > 128))
    if (currentPixel == targetVal):
        return currentPixel
    ra = random.randint(0,5)
    if (currentPixel == 0):
        return int(ra==0)
    if (currentPixel == 1):
        return int(ra==0)
def SaveImage(grid, imageID):
    plt.imshow(grid, vmin=0, vmax=1)  # Assuming binary grid, using grayscale colormap
    #plt.axis('off')  # Turn off axis
    if not os.path.exists("Render"):
        os.makedirs("Render")
    name = "Render/A"+str(imageID)+".png"
    plt.savefig(name, dpi=50, bbox_inches='tight', pad_inches=0)  # Save the image
    print("Saved: " + name)
def GetInputImagePath(number):
    if not os.path.exists("BadApple"):
        os.makedirs("BadApple")
    imageFolder = "BadApple"
    imageName = str(number)
    imagePath = os.path.join(imageFolder, imageName + ".png")
    return imagePath
Render(2107)