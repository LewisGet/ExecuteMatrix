import Helper as Hp
import numpy as np
import Frame


class Entity:
    """value type

    :type Frames: list[Frame.Entity]
    :type Fps: int
    :type FirstPlaceFps: int
    :type LastPlaceFps: int
    """
    Frames = []
    Fps = 0
    FirstPlaceFps = None
    LastPlaceFps = None

    def __init__(self, frames, correct_location=[0, 0, 0]):
        self.flush_frames(frames, correct_location)

    def flush_frames(self, frames, correct_location=[0, 0, 0]):
        """update all frames to this entity

        :type frames: [Frame.Entity]
        :type correct_location: list
        """
        correct_location = Hp.XYZ(correct_location).to_array()

        for fps, value in enumerate(frames):
            value = Frame.Entity(value)

            if value.is_place():
                if self.FirstPlaceFps is None:
                    self.FirstPlaceFps = fps

                self.LastPlaceFps = fps

            if value.is_execute():
                value.block += correct_location

            value.location += correct_location
            self.Frames.append(value)

    def correct_location_array(self, correct_location=[], fps=[]):
        """correct each frames by list

        :param correct_location: [numpy.ndarray]
        :param fps: [int]
        """

        if len(fps) > 0:
            self.correct_location_by_fps(correct_location, fps)
        else:
            self.correct_location_by_no_fps(correct_location)

    def correct_location_by_fps(self, correct_location=[], fps=[]):
        for index in fps:
            correct_value = Hp.XYZ(correct_location[index]).to_array()

            self.Frames[index].location += correct_value

    def correct_location_by_no_fps(self, correct_location=[]):
        for entity, correct_value in zip(self.Frames, correct_location):
            correct_value = Hp.XYZ(correct_value).to_array()

            entity.location += correct_value

            if entity.is_execute():
                entity.block += correct_value

    def get_first_fps(self):
        return 0

    def get_last_fps(self):
        return len(self.Frames) - 1

    def get_range(self, start, end):
        value_fps, value = [], []

        for fps in range(start, end):
            value_fps.append(fps)
            value.append(self.Frames[fps])

        return value_fps, value

    def get_start_half_sec(self):
        return self.get_range(self.get_first_fps(), self.get_first_fps() + 15)

    def get_end_half_sec(self):
        return self.get_range(self.get_last_fps() - 15, self.get_last_fps())

    def get_before_place_half_sec_fps(self):
        return self.get_range(self.FirstPlaceFps - 16, self.FirstPlaceFps - 1)

    def get_after_place_half_sec_fps(self):
        return self.get_range(self.LastPlaceFps + 1, self.LastPlaceFps + 16)

    def active_frame(self):
        return self.Frames[self.Fps]

    def remove_frames(self, fps=[]):
        for value in fps:
            del self.Frames[value]

        clone_frames = self.Frames[:]

        self.flush_frames(clone_frames)

    def get_last_place(self):
        return self.Frames[self.LastPlaceFps].block

    def get_first_place(self):
        return self.Frames[self.FirstPlaceFps].block

    def get_last_location(self):
        return self.Frames[self.get_last_fps()].location

    def get_first_location(self):
        return self.Frames[self.get_first_fps()].location


class Creator:
    """value type

    :type A: Frame.Entity
    :type B: Frame.Entity
    """
    A = None
    B = None

    def line_frames(self, fps=30, action=False):
        frames = []

        ax, ay, az = Hp.XYZ(self.A.location).to_array()
        bx, by, bz = Hp.XYZ(self.B.location).to_array()

        ab_location = np.linspace(ax, bx, num=fps), np.linspace(ay, by, num=fps), np.linspace(az, bz, num=fps)
        ab_location = np.array(ab_location)

        ax, ay, az = Hp.XYZ(self.A.direction).to_array()
        bx, by, bz = Hp.XYZ(self.B.direction).to_array()

        ab_direction = np.linspace(ax, bx, num=fps), np.linspace(ay, by, num=fps), np.linspace(az, bz, num=fps)
        ab_direction = np.array(ab_direction)

        for location, direction in zip(ab_location.T, ab_direction.T):
            entity = Frame.Entity(None)

            entity.location = Hp.XYZ(location).to_array()
            entity.direction = Hp.XYZ(direction).to_array()
            entity.block = Hp.XYZ([0, 0, 0]).to_array()
            entity.action = 0

            frames.append(entity)

        if action:
            entity = frames[len(frames) - 1]
            entity.block = Hp.XYZ(entity.location).to_array() + Hp.XYZ([0, -1.3, 0]).to_array()
            entity.action = "place"

            frames[len(frames) - 1] = entity

        return Entity(frames)

    def speed_limited_line_frames(self, max_speed=5, action=False):
        distance = Hp.get_distance(self.A.location, self.B.location)
        fps = int(distance / max_speed)

        return self.line_frames(fps, action)
