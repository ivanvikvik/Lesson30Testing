class Human:
    def __init__(self, name="no name"):
        self.name = name

    def __str__(self):
        return self.name

    def hello(self):
        return f"Hello! I'm {self.name}."

    def work(self):
        pass
