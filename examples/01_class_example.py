class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is", self.name)

    def __del__(self):
        print(f"{self.name} says bye.")

A = Person("Alex")
