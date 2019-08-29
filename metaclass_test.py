'''
The example below is from Marty Alchin's Pro Django book Page 13
It shows how metaclass works. __qualname__ see PEP 3155
'''


class MetaClass(type):
    def __init__(cls, name, bases, attrs):
        print('Defining %s' % cls)
        print('Name: %s' % name)
        print('Bases: %s' % (bases, ))
        print('Attributes:')
        for (name, value) in attrs.items():
            print('    %s: %r' % (name, value))
            
            
class RealClass(metaclass=MetaClass):
    spam = 'egg'
    def f(self):
        return 0
    
    
class SubClass(RealClass):
    foo = 'bar'
    def s(self):
        return 1
        
print('')
print('RealClass.__dict__ is {}'.format(RealClass.__dict__))
print('')
print('SubClass.__dict__ is {}'.format(SubClass.__dict__))


'''
Results:

george@desktop:~/Desktop/desktop/git-repo/PythonDescriptor$ python metaclass_test.py 
Defining <class '__main__.RealClass'>
Name: RealClass
Bases: ()
Attributes:
    __module__: '__main__'
    __qualname__: 'RealClass'
    spam: 'egg'
    f: <function RealClass.f at 0x7ff6d68eff28>
Defining <class '__main__.SubClass'>
Name: SubClass
Bases: (<class '__main__.RealClass'>,)
Attributes:
    __module__: '__main__'
    __qualname__: 'SubClass'
    foo: 'bar'
    s: <function SubClass.s at 0x7ff6d685a048>

RealClass.__dict__ is {'__module__': '__main__', 'spam': 'egg', 'f': <function RealClass.f at 0x7ff6d68eff28>, '__dict__': <attribute '__dict__' of 'RealClass' objects>, '__weakref__': <attribute '__weakref__' of 'RealClass' objects>, '__doc__': None}

SubClass.__dict__ is {'__module__': '__main__', 'foo': 'bar', 's': <function SubClass.s at 0x7ff6d685a048>, '__doc__': None}



'''
