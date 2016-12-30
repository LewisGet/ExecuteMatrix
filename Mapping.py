import Frame
import Action
import Helper


class Entities:
    """create a Action between two List

    eg.
    input a: [1,2,3] b: [7,8,9]
    output A: [1] Mapping: [3,5,7] B: [9]

    :type A: Action.Entity
    :type B: Action.Entity
    :type Mapping: Action.Entity
    :type MaxSpeed: int
    """
    A = None
    B = None
    Mapping = None

    # TODO: In both execute, if two targets are too far away you need to add frames
    MaxSpeed = 5

    def __init__(self):
        pass

    def demo_execute(self, demo, execute, target_location):
        pass

    def execute_demo(self, execute, demo, target_location):
        pass

    def two_demo(self, a, b):
        pass

    def two_execute(self, a, b, a_target, b_target):
        pass
