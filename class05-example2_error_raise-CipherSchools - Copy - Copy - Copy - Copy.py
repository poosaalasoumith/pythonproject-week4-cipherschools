class mobile:
          def __init__(self,name):
                    self.name=name

class mobilestore:
          def __init__(self):
                    self.mobiles=[]
          def add_mobile(self,new_mobile):
                    if isinstance(new_mobile,mobile):
                              self.mobiles.append(new_mobile)
oneplus=mobile("Oneplus 6")
samsung="samsung galaxy s8"
mobostore=mobilestore()
mobostore.add_mobile(samsung)
print(mobostore.mobiles)