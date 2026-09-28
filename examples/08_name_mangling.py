class C:
    def accessible(self):
        print("you can see me")

    def __inaccessible(self):
        print("you cannot see me")

c = C()
c.accessible()
# c.__inaccessible()      # AttributeError
c._C__inaccessible()      # name-mangled access
