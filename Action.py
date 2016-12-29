import Helper as Hp
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
