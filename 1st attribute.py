# creating attributes in python 
class Customer:
    def set_name(self,new_name):
        self.name = new_name
#self is a stand in for a particular object used in a class definition
cust = Customer()
cust.set_name("Akoto Boadi")
print(cust.name)