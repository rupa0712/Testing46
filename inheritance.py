class parent:
    def display(self):
        print("This is parent method")

class child(parent):
    def display1(self):
        print("This is child method")

c=child()
c.display()
c.display1()


