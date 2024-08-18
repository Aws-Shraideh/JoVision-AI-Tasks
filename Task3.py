import cv2
import os
import pandas as pd
import numpy as np


def fingerPressureDetection(imagePath, fingerRegions):
    img = cv2.imread(imagePath)
    height, width, channels = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    pressureThreshold = 168
    pressureValues = [0] * 5

    for i, (finger, (xStart, xEnd, yStart, yEnd)) in enumerate(fingerRegions.items()):
        fingerRegion = gray[yStart: yEnd, xStart: xEnd]
        maxBrightness = np.max(fingerRegion)
        if maxBrightness > pressureThreshold:
            pressureValues[i] = 1
        else:

            pressureValues[i] = 0
    colorLine = img[256:height, 0:width]
    greenPixels = np.sum(colorLine[:, :, 1] > 200)
    pressureDetection = "Pressure Detected" if greenPixels > 0 else "No Pressure Detected"

    return pressureValues, pressureDetection


imageDir = os.path.join(os.getcwd(), "task3Images")

results = []
fingerRegions = {
    "Finger 1": (256, 383, 0, 23),
    "Finger 2": (256, 383, 48, 71),
    "Finger 3": (256, 383, 80, 103),
    "Finger 4": (256, 383, 120, 143),
    "Finger 5": (456, 487, 144, 255)
}

for fileName in os.listdir(imageDir):
    if fileName.endswith(".jpg"):
        imagePath = os.path.join(imageDir, fileName)
        pressureValue, pressureDetection = fingerPressureDetection(imagePath, fingerRegions)

        results.append({
            "Image": fileName,
            "Pinky": pressureValue[0],
            "Ring": pressureValue[1],
            "Middle": pressureValue[2],
            "Index": pressureValue[3],
            "Thumb": pressureValue[4],
            "Pressure": pressureDetection
        })

df = pd.DataFrame(results)
outputFile = "FingerPressureData.xlsx"
df.to_excel(outputFile, index=False)
print(f"Data saved to {outputFile}")
