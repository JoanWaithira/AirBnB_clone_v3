class Test:
    def __init__(self, name):
        self.name = name


obj = Test('cup')
setattr(obj, 'name', 'spoon')
print(obj.__dict__)
