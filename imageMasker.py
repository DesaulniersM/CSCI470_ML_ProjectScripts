import os
import cv2
import numpy as np


class Masker:
    def __init__(self, imagesDirectory, masksDirectoy, outputDirectory):
        self.imagesDirectory = imagesDirectory
        self.masksDirectory = masksDirectoy
        self.outputDirectory = outputDirectory

    def run(self):
        # This is a garbage way of doing it, but I dont know how to create pointers that I can freely increment and
        # it should only have to run once.
        for imageFile in os.listdir(self.imagesDirectory):
            imageBase = os.path.basename(imageFile)
            fullpath = self.imagesDirectory + "\\" + imageBase
            outputImage = cv2.imread(fullpath)
            for maskFile in os.listdir(self.masksDirectory):
                maskBase = os.path.basename(maskFile)
                if (maskBase == imageBase):
                    # Then we need to add them
                    maskImage = cv2.imread(self.masksDirectory+"\\"+maskFile)
                    outputImage = cv2.add(outputImage,maskImage)
                    break
            resized = cv2.resize(outputImage, (400,400))
            # cv2.imshow('test',resized)
            # key = cv2.waitKey(3000)
            # print(imageFile)
            cv2.imwrite(self.outputDirectory + "\\" + imageFile, resized)