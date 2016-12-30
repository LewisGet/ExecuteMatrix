import Action
import Helper as Hp


class Entities:
    """create a Action between two List

    eg.
    input a: [1,2,3] b: [7,8,9]
    output A: [1] Mapping: [3,5,7] B: [9]

    :type A: Action.Entity
    :type B: Action.Entity
    :type Mapping: Action.Entity
    :type MaxSpeed: int
    :type targetHumanized: numpy.ndarray
    """
    A = None
    B = None
    Mapping = None

    # TODO: In both execute, if two targets are too far away you need to add frames
    MaxSpeed = 5

    # note: target block humanized design 0.5
    targetHumanized = Hp.XYZ([0.5, 0.5, 0.5]).to_array()

    def __init__(self, a, b):
        self.A = Action.Entity(a)
        self.B = Action.Entity(b)

    def demo_execute(self, target_location):
        demo_correct = target_location - self.A.get_last_location()
        self.A.flush_frames(self.A.Frames[:], demo_correct)
        execute_correct = target_location - self.B.get_last_place()
        self.B.flush_frames(self.B.Frames[:], execute_correct)

        fps_a, half_a = self.A.get_end_half_sec()
        fps_b, half_b = self.B.get_before_place_half_sec_fps()

        self.Mapping = Action.Entity(half_a)
        self.Mapping.correct_location_array(half_b)

        self.A.remove_frames(fps_a)
        self.B.remove_frames(fps_b)

    def execute_demo(self, target_location):
        pass

    def two_demo(self):
        pass

    def two_execute(self, a_target, b_target):
        pass
