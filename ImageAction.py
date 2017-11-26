import Action
import Image


class ImageToBlocks:
    basic_height = 7

    def __init__(self, basic_height=7):
        self.basic_height = basic_height

    def pixel_to_block(self, pixel):
        pixel_x, pixel_y, pixel_color = pixel
        xyz = pixel_x, self.basic_height, pixel_y
        block = Image.DefaultBuildColors.get_closet_dataset(pixel_color)

        return xyz, block

    def arrays_to_blocks(self, arrays):
        blocks = []

        for i in arrays:
            block = self.pixel_to_block(i)
            blocks.append(block)

        return blocks

    def image_to_blocks(self, image_path):
        image = Image.TargetImageToArrays(image_path)
        pixels = image.contours[:] + image.without_contours_contents[:]

        return self.arrays_to_blocks(pixels)


class BlocksToActions:
    is_set_blocks = []
    blocks = []

    def __init__(self, blocks, is_set_blocks=[]):
        self.blocks = blocks
        self.is_set_blocks = is_set_blocks

    def is_this_is_set_block(self, block):
        xyz, type = block

        for have_xyz, have_block in self.is_set_blocks:
            if have_xyz == xyz:
                if have_block == type:
                    return True

        return False

