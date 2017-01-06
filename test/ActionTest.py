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
