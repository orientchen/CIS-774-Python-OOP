class Person:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

p = Person("Alex")
print(p.name)
p.print_name()
