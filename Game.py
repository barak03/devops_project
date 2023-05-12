class Game:
    def __int__(self):
        pass

    def __init__(self, difficulty_level_number):
        self._difficulty_level_number = difficulty_level_number

    def play(self):
        raise NotImplementedError()
