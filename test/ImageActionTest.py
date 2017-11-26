import unittest
import ImageAction
import os

class TestBlocksToActionsMethods(unittest.TestCase):
    TestImagePath = None
    TestClassObject = None
    TestIsSetPixels = [[0, 0, [255, 255, 255]], [0, 1, [255, 255, 255]]]
    TestBlocks = []
    TestIsSetBlocks = []
    ImageToBlocks = None

    def setUp(self):
        self.ImageToBlocks = ImageAction.ImageToBlocks()
        self.TestImagePath = os.sep.join([os.path.dirname(os.path.abspath(__file__)), "test.jpg"])

        self.TestBlocks = self.ImageToBlocks.image_to_blocks(self.TestImagePath)
        self.TestIsSetBlocks = self.ImageToBlocks.arrays_to_blocks(self.TestIsSetPixels)

        self.TestClassObject = ImageAction.BlocksToActions(self.TestBlocks, self.TestIsSetBlocks)

    def test_is_this_is_set_block(self):
        block1 = self.ImageToBlocks.pixel_to_block([0, 0, [255, 255, 255]])
        block2 = self.ImageToBlocks.pixel_to_block([1, 0, [255, 255, 255]])

        is_block_set1 = self.TestClassObject.is_this_is_set_block(block1)
        is_block_set2 = self.TestClassObject.is_this_is_set_block(block2)

        self.assertTrue(is_block_set1)
        self.assertFalse(is_block_set2)
