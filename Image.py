import PIL.Image as Image
import Helper as Hp
import numpy as np


class Targets:
    imageArray = None
    contours = []
    contents = []

    def __init__(self, imagePath):
        self.imageArray = self.get_image_array(imagePath)

        for x, row in enumerate(self.imageArray):
            for y, color in enumerate(row):
                if self.is_visible(color):
                    self.contents.append([x, y, color])

                    if self.is_contour(x, y):
                        self.contours.append([x, y, color])

    def get_image_array(self, path):
        image = Image.open(path).convert("RGBA")

        return np.array(image)

    def is_visible(self, rgba):
        return rgba[3] > 200

    def un_visible(self, rgba):
        return not self.is_visible(rgba)

    def is_border(self, x, y):
        return x in [0, self.imageArray.shape[0]] or y in [0, self.imageArray.shape[1]]

    def is_contour(self, x, y):
        if self.is_border(x, y):
            return True

        up = self.un_visible(self.imageArray[x][y - 1])
        down = self.un_visible(self.imageArray[x][y + 1])
        left = self.un_visible(self.imageArray[x - 1][y])
        right = self.un_visible(self.imageArray[x + 1][y])

        return True in [up, down, left, right]
