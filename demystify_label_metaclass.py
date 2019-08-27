'''
Code from Chris Beaumont's article Python Descriptor Demystified
https://nbviewer.jupyter.org/urls/gist.github.com/ChrisBeaumont/5758381/raw/descriptor_writeup.ipynb
modified to handle python 3 metaclasses
'''


class Descriptor(object):
    def __init__(self):
        #notice we aren't setting the label here
        self.label = None
        
    def __get__(self, instance, owner):
        print('__get__. Label = %s' % self.label)
        return instance.__dict__.get(self.label, None)
    
    def __set__(self, instance, value):
        print('__set__')
        instance.__dict__[self.label] = value

        
class DescriptorOwner(type):
    def __new__(cls, name, bases, attrs):
        # find all descriptors, auto-set their labels
        for n, v in attrs.items():  # in the example below n is 'x', v is Descriptor()
            if isinstance(v, Descriptor):
                v.label = n
        return super().__new__(cls, name, bases, attrs)

        
class Foo(metaclass=DescriptorOwner):
    x = Descriptor()
    
f = Foo()
f.x = 10
print(f.x)
