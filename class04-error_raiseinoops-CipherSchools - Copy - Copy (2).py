class Animal:
          def __init__(self,name):
                    self.name=name
          def sound(self):
                    # return "this is animal sound"
                    raise NotImplementedError("you have to implement in the subclasses")
class Dog(Animal):
          def __init__(self, name,breed):
                  super().__init__(name)
                  self.breed=breed
          def sound(self):
                    return "bow bow"


class Cat(Animal):
          def __init__(self,name,breed):
                    super().__init__(name)
                    self.breed = breed
          def sound(self):
                  return "meow meow"
doggy=Dog("boomy","bug")
print(doggy.sound())
messy=Cat("country","bumchik")
print(messy.sound())