'''
Code from Chris Beaumont's article Python Descriptor Demystified
https://nbviewer.jupyter.org/urls/gist.github.com/ChrisBeaumont/5758381/raw/descriptor_writeup.ipynb
'''


class Descriptor(object):
    
    def __init__(self, label):
        self.label = label
        
    def __get__(self, instance, owner):
        print('__get__', instance, owner)
        return instance.__dict__.get(self.label)
    
    def __set__(self, instance, value):
        print('__set__')
        instance.__dict__[self.label] = value
        

class Foo(list):
    x = Descriptor('x')
    y = Descriptor('y')
    
f = Foo()
f.x = 5        # <===== Foo.Descriptor.__set__(f, 5) in concept
print(f.x)
