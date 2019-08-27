'''
Code example on this webpage
https://www.blog.pythonlibrary.org/2016/06/10/python-201-what-are-descriptors/
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
    print(c.desc)
    print(c.normal)
    c.desc = 100
    print(c.desc)
