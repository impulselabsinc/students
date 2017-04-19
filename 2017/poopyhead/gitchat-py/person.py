class Person(object):
    def __init__(self, name="John Doe", eyecolor="brown"):
        self.name = name
        self.eyecolor = eyecolor

    def eyes(self, eyecolor):
        self.eyecolor = eyecolor

    def hair(self, haircolor="black"):
        self.haircolor = haircolor
