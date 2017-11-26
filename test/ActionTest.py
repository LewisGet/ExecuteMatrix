import unittest
import Action
import Frame


class TestActionMethods(unittest.TestCase):
    def test_line_frames(self):
        a, b = Frame.Entity(None), Frame.Entity(None)
        a.location, b.location = [1, 2, 3], [31, 32, 33]
        a.direction, b.direction = [0.1, 0.2, 0.3], [0.5, 0.1, 0.1]

        action_creator = Action.Creator()
        action_creator.A = a
        action_creator.B = b

        actions = action_creator.line_frames(30)

        self.assertEqual(len(actions.Frames), 30)

        for frame_entity in actions.Frames:
            self.assertEqual(type(frame_entity), Frame.Entity)


class TestContainerMethods(unittest.TestCase):
    TestClassObject = None

    def setUp(self):
        self.TestClassObject = Action.Container()

    def test_vec_line(self):
        a, b = [1, 2, 3], [31, 32, 33]

        vec = self.TestClassObject.vec_line(30, a, b)

        self.assertEqual(len(vec), 30)
        self.assertEqual(vec[0], [1, 2, 3])

    def test_export_frames(self):
        self.TestClassObject.Location = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3]]
        self.TestClassObject.Direction = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 0, 4], [0, 0, 5]]

        frames = self.TestClassObject.export_frames()

        self.assertEqual(len(frames), 6)
        self.assertEqual(frames[5]['location'], [0, 0, 3])
        self.assertEqual(frames[5]['direction'], [0, 0, 5])
