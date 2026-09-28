class Person:
    def speak(self):
        print("I can speak")

class Man(Person):
    def wear(self):
        print("I wear shirt")

class Woman(Person):
    def wear(self):
        print("I wear skirt")

man = Man()
man.wear()
man.speak()
