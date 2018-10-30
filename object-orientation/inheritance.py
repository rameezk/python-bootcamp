class Animal():
    def __init__(self):
        print("Creating animal")

    def speak(self):
        print("Generic sound")

    def what_am_i(self):
        print("I am an animal")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)

    def speak(self):
        print("Woof")

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)

dog = Dog()
dog.what_am_i()
dog.speak()

cat = Cat()
cat.what_am_i()
cat.speak()

for pet in [dog, cat]:
    pet.speak()

