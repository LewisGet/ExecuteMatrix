import unittest
import Image
import os


class TestItemColorsMethods(unittest.TestCase):
    def test_closet_dataset(self):
        item = Image.DefaultBuildColors

        data = item.get_closet_dataset([255, 255, 255])

        self.assertEqual(data['id'], 35)
        self.assertEqual(data['type'], 0)

        data = item.get_closet_dataset([0, 0, 0])

        self.assertEqual(data['id'], 35)
        self.assertEqual(data['type'], 15)


class TestTargetImageToArraysMethods(unittest.TestCase):
    TestImagePath = None
    TestClassObject = None

    def setUp(self):
        self.TestImagePath = os.sep.join([os.path.dirname(os.path.abspath(__file__)), "test.jpg"])
        self.TestClassObject = Image.TargetImageToArrays(self.TestImagePath)

    def test_contours_working(self):
        contours = self.TestClassObject.contours
        first_contours = contours[0]
        x, y, rgb = first_contours

        self.assertEqual(x, 0)
        self.assertEqual(y, 0)
        self.assertEqual(rgb, [255, 255, 255])

    def test_contents_working(self):
        contents = self.TestClassObject.contents
        first_contents = contents[0]
        x, y, rgb = first_contents

        self.assertEqual(x, 0)
        self.assertEqual(y, 0)
        self.assertEqual(rgb, [255, 255, 255])

