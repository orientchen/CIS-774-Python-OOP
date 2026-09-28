class Animal:
    def name(self):
        pass

    def sleep(self):
        print("sleep")

    def make_noise(self):
        pass

class Dog(Animal):
    def name(self):
        print("I am a dog!")
    def make_noise(self):
        print("Woof!")

class Cat(Animal):
    def name(self):
        print("I am a cat!")
    def make_noise(self):
        print("Meow")

class Lion(Animal):
    def name(self):
        print("I am a lion!")
    def make_noise(self):
        print("Roar")

def test_animal(animal):
    animal.name()
    animal.sleep()
    animal.make_noise()

for animal in (Dog(), Cat(), Lion()):
    test_animal(animal)
