import Helper as hp


class Entity:
    def __init__(self, training_data={}):
        if type(training_data).__name__ == 'dict':
            self.location = hp.XYZ(training_data['location']).toArray()
            self.direction = hp.XYZ(training_data['direction']).toArray()
            self.block = hp.XYZ(training_data['blockLocation']).toArray()
            self.action = training_data['block']
        elif training_data is not None:
            self.location = hp.XYZ(training_data.location).to_array()
            self.direction = hp.XYZ(training_data.direction).to_array()
            self.block = hp.XYZ(training_data.block).to_array()
            self.action = training_data.action

    def __setattr__(self, name, value):
        if name in ["location", "direction", "block"]:
            self.__dict__[name] = hp.XYZ(value).to_array()

        self.__dict__[name] = value

    def __getattr__(self, name):
        if name in ["location", "direction", "block"]:
            return hp.XYZ(self.__dict__[name]).to_array()

        return self.__dict__[name]

    def is_place(self):
        return self.action == "place"

    def is_break(self):
        return self.action == "break"

    def is_execute(self):
        return not self.action == 0
