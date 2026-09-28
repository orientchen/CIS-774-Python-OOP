class Person:
    def __init__(self):
        self.A = "Alex"
        self.__B = "Bob"

    def print_name(self):
        print(self.A)
        print(self.__B)

p = Person()
print(p.A)
# print(p.__B)  # AttributeError
p.print_name()
