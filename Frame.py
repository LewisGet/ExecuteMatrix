import Helper as hp


class Entity:
    def __init__(self, training_data={}):
        if type(training_data).__name__ == 'dict':
            self.location = hp.XYZ(training_data['location']).toArray()
            self.direction = hp.XYZ(training_data['direction']).toArray()
            self.block = hp.XYZ(training_data['blockLocation']).toArray()
            self.action = training_data['block']
        else:
            self.location = training_data.location
            self.direction = training_data.direction
            self.block = training_data.block
            self.action = training_data.action

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __getattr__(self, name):
        self.__dict__[name]

    def is_place(self):
        return self.action == "place"

    def is_break(self):
        return self.action == "break"

    def is_execute(self):
        return not self.block == 0
