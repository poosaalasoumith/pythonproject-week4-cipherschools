class Phone:
          def __init__(self,brand,model,price):
                    self.brand=brand
                    self.model=model
                    self.price=price
          def phone_name(self):
                    return f"{self.brand} {self.model} "
          def __repr__(self):
                    return f"phone({self.brand} {self.model} and price is {self.price}) "
          def __str__(self):
                    return f"phone({self.brand} {self.model} and price is {self.price}) "
          def __len__(self):
                    return len(self.phone_name())
          def __mul__(self,other):
                    return self.price * other.price
l=[1,2,3,4,4]
print(l)
my_phone=Phone("nokia","1100",1100)
my_phone2=Phone("nokia","1600",1200)
print(my_phone*my_phone2 )
print(my_phone.phone_name())
print(repr(my_phone))
print(len(my_phone))



class Smartphone(Phone):
          def __init__(self,brand,model,price,camera):
                    super().__init__(brand,model,price)
                    self.camera=camera
          def phone_name(self):
                    return f"{self.brand}"
my_phone=Phone("nokia","1100",1100)
my_phone2=Phone("nokia","1600",1200)
my_smartphone=Smartphone("oneplus","5T",33000,"16MP")
print(my_phone2.phone_name())
































