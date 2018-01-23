class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
    @property.getter
    print(help(dir))
    def score(self):
        return self._score
if __name__ == "__main__":
    cls = Student()
    cls.score = 10
    
    print("current param : %s " % cls.score )
    print(help(property))
