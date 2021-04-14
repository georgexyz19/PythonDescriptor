'''
Code example on this webpage
https://www.blog.pythonlibrary.org/2016/06/10/python-201-what-are-descriptors/

Revised to show d.desc on 4/14/2021
'''


class MyDescriptor():
    def __init__(self, initial_value=None, name='my_var'):
        self.var_name = name
        self.value = initial_value
 
    def __get__(self, obj, objtype):
        print('Getting', self.var_name)
        return self.value
 
    def __set__(self, obj, value):
        msg = 'Setting {name} to {value}'
        print(msg.format(name=self.var_name, value=value))
        self.value = value
 

class MyClass():
    desc = MyDescriptor(initial_value='Mike', name='desc')
    normal = 10
 

if __name__ == '__main__':
    c = MyClass()
    print('c.desc is ', c.desc)
    d = MyClass()               # added for testing
    print('c.normal is ', c.normal)
    print('d.desc is ', d.desc)

    print('Setting c.desc to 100')
    c.desc = 100
    print('c.desc is ', c.desc)
    print('d.desc is ', d.desc)  # this is 100

