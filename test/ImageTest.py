import unittest
import Image


class TestItemColorsMethods(unittest.TestCase):
    def test_closet_dataset(self):
        item = Image.ItemColors()

        data, _, _ = item.get_closet_dataset([255, 255, 255])

        self.assertEqual(data, 0)

        data, _, _ = item.get_closet_dataset([0, 0, 0])

        self.assertEqual(data, 23)
