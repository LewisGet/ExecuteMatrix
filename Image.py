from PIL import ImageDraw, Image
import matplotlib.pyplot as plt
import numpy as np
import ntpath
import glob
import os

class ItemColors:
    colors = []

    def __init__(self, files_path):
        for file_path in files_path:
            var_id, var_type = self.get_image_id_and_type(file_path)
            var_rgb = self.get_image_mean_colors(file_path)

            self.colors.append({"id": var_id, "type": var_type, "rgb": var_rgb})

    def get_image_id_and_type(self, path):
        filename = ntpath.basename(path)
        filename = (filename.split("."))[0]

        return np.array(filename.split("-")).astype(int).tolist()

    def get_image_mean_colors(self, path):
        colors = []

        img = Image.open(path).convert("RGB")
        img = np.array(img)

        for xy in img:
            for y in xy:
                colors.append(y)

        colors = np.array(colors)
        rgb = np.mean(colors, axis=0)
        r, g, b = rgb

        return [int(round(r)), int(round(g)), int(round(b))]

    def get_color_distance(self, a, b):
        a = np.array(a).astype(int)
        b = np.array(b).astype(int)

        return np.linalg.norm(a - b)

    def get_closet_dataset(self, find_rgb, return_with_database_index=False):
        distance = None
        closest_index = None

        for index, reg_color in enumerate(self.colors):
            this_color_distance = self.get_color_distance(find_rgb, reg_color['rgb'])

            if distance is None or distance > this_color_distance:
                distance = this_color_distance
                closest_index = index

        if return_with_database_index:
            return closest_index, self.colors[closest_index]

        return self.colors[closest_index]

class TargetImageToArrays:
    imageArray = None
    contours = []
    contents = []
    without_contours_contents = []

    def __init__(self, image_path):
        self.imageArray = self.get_image_array(image_path)

        for x, row in enumerate(self.imageArray):
            for y, color in enumerate(row):
                rgb = (color[:-1]).tolist()

                if self.is_visible(color):
                    self.contents.append([x, y, rgb])

                    if self.is_contour(x, y):
                        self.contours.append([x, y, rgb])
                    else:
                        self.without_contours_contents.append([x, y, rgb])

    def get_image_array(self, path):
        image = Image.open(path).convert("RGBA")

        return np.array(image)

    def is_visible(self, rgba):
        return rgba[3] > 200

    def un_visible(self, rgba):
        return not self.is_visible(rgba)

    def is_border(self, x, y):
        return x in [0, self.imageArray.shape[0] - 1] or y in [0, self.imageArray.shape[1] - 1]

    def is_contour(self, x, y):
        if self.is_border(x, y):
            return True

        up = self.un_visible(self.imageArray[x][y - 1])
        down = self.un_visible(self.imageArray[x][y + 1])
        left = self.un_visible(self.imageArray[x - 1][y])
        right = self.un_visible(self.imageArray[x + 1][y])

        return True in [up, down, left, right]


default_files_path = os.sep.join([os.path.dirname(os.path.abspath(__file__)), "colors", "*.png"])
default_files_path = glob.glob(default_files_path)

DefaultBuildColors = ItemColors(default_files_path)