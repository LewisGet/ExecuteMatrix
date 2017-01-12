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
                rgb = color[:-1]

                if self.is_visible(color):
                    self.contents.append([x, y, rgb])

                    if self.is_contour(x, y):
                        self.contours.append([x, y, rgb])

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


class ItemColors:
    items = [[35, 0], [35, 1], [35, 2], [35, 3], [35, 4], [35, 5], [35, 6], [35, 7], [159, 0], [159, 1], [159, 2], [159, 3], [159,4], [159,5], [159,6], [159,7], [35,8], [35,9], [35, 10], [35, 11], [35, 12], [35, 13], [35, 14], [35, 15], [159, 8], [159, 9], [159, 10], [159, 11], [159, 12], [159, 13], [159, 14], [159, 15]]
    colors = [None] * 32

    def __init__(self):
        for i in range(32):
            self.colors[i] = self.get_image_mean_colors(str(i + 1))

    def get_image_mean_colors(self, number):
        colors = []

        img = Image.open("./colors/" + number + ".png").convert("RGB")
        img = np.array(img)

        for xy in img:
            for y in xy:
                colors.append(y)

        colors = np.array(colors)
        rgb = np.mean(colors, axis=0)
        r, g, b = rgb

        return [int(round(r)), int(round(g)), int(round(b))]

    def get_color_distance(self, a, b):
        a = np.array(a)
        b = np.array(b)

        return np.linalg.norm(a - b)

    def get_closet_dataset(self, rgb):
        distance = None
        closest_index = None

        for index, color in enumerate(self.colors):
            this_color_distance = self.get_color_distance(rgb, color)

            if distance is None or distance > this_color_distance:
                distance = this_color_distance
                closest_index = index

        return closest_index, self.items[closest_index], self.colors[closest_index]


class ScriptBasic:
    targets = None
    itemColors = ItemColors()
    basicY = 5
    script = []

    def __init__(self, image_path):
        self.targets = Targets(image_path)
        self.execute()

    def execute(self):
        self.pre_execute()
        self.do_execute()
        self.post_execute()

    def do_execute(self):
        pass

    def pre_execute(self):
        pass

    def post_execute(self):
        pass

    def get_blocks(self, targets):
        blocks = []

        for pixel in targets:
            _, data, _ = self.itemColors.get_closet_dataset(pixel[2])

            block = type('', (), {})()
            block.y = self.basicY
            block.x, block.z = pixel[0], pixel[1]
            block.typeId, block.data = data

            blocks.append(block)

        return blocks


class ScriptJavascript(ScriptBasic):
    def javascript_template(self, value):
        return "create(" + str(value.x) + ", " + str(value.y) + ", " + str(value.z) + ", " + str(value.typeId) + ", " + str(value.data) + ");"

    def do_execute(self):
        blocks = self.get_blocks(self.targets.contents)

        for block in blocks:
            self.script.append(self.javascript_template(block))

    def post_execute(self):
        for line in self.script:
            print(line)
