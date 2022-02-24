class Skill:

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def set_level(self, level):
        self.level = level
