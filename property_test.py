'''
code example from this webpage
https://www.machinelearningplus.com/python/python-property/
It is a nice example on how to write property
'''

class Person():

    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    @property    
    def fullname(self):
        return self.first + ' '+ self.last

    @fullname.setter
    def fullname(self, name):
        firstname, lastname = name.split()
        self.first = firstname
        self.last = lastname

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None   
        
    # note all three methods are called 'fullname'

    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)


person = Person('George', 'Harrison')
print(person.fullname)  
print(person.first)  
print(person.last)  

# Setting fullname 
person.fullname = 'John Lennon'

# Print the changed values of `first` and `last`
print(person.fullname) 
print(person.first)  
print(person.last)  

del person.fullname
#print(person.fullname) # raise exception 
print(person.first)  
print(person.last)


