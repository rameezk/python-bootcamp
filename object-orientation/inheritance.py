class Animal():
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)

    def speak(self):
        print("Woof")

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)

    def speak(self):
        print("Meow")


dog = Dog()
cat = Cat()
generic = Animal()

def pet_speak(pet):
    print(type(pet))
    pet.speak()

for pet in [dog, cat, generic]:
    pet_speak(pet)

