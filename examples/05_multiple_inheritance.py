class A:
    def method_a(self):
        print("I am A")

class B:
    def method_a(self):
        print("I am B's A")

    def method_b(self):
        print("I am B")

class C(A, B):
    def method_c(self):
        print("I am C")

c = C()
c.method_a()
c.method_b()
c.method_c()
