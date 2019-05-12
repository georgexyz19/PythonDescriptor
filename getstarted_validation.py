from weakref import WeakKeyDictionary

'''
A weak reference to an object is not enough to keep the object alive: when the only remaining 
references to a referent are weak references, garbage collection is free to destroy the referent 
and reuse its memory for something else. However, until the object is actually destroyed the weak 
reference may return the object even if there are no strong references to it.

Once again, we create a descriptor class. In this case, we use Python’s weakref library’s 
WeakKeyDictionary, which is a neat class that creates a dictionary that maps keys weakly. 
What this means is that when there are no strong references to a key in the dictionary, 
that key and its value will be discarded. We are using that in this example to prevent our 
Person instances from hanging around indefinitely. 

'''


class Drinker:
    def __init__(self):
        self.req_age = 21
        self.age = WeakKeyDictionary()
 
    def __get__(self, instance_obj, objtype):  # objtype still not used here
        return self.age.get(instance_obj, self.req_age)
 
    def __set__(self, instance, new_age):  # What is this instance ? a Person instance
        if new_age < 21:
            msg = '{name} is too young to legally imbibe'
            raise Exception(msg.format(name=instance.name))
        self.age[instance] = new_age
        print('{name} can legally drink in the USA'.format(
            name=instance.name))
 
    def __delete__(self, instance):
        del self.age[instance]
 
 
class Person:
    drinker_age = Drinker()   # class level descriptor
 
    def __init__(self, name, age):
        self.name = name
        self.drinker_age = age
 
if __name__ == '__main__' :
    p_Miguel = Person('Miguel', 30)
    print('Miguel\'s age is {}'.format(p_Miguel.drinker_age))
    p_Miguel.drinker_age = 32	# call Person.drinker_age.__set__(p_Miguel, 32)
    p_Niki = Person('Niki', 13)
