'''
Code from Chris Beaumont's article Python Descriptor Demystified
https://nbviewer.jupyter.org/urls/gist.github.com/ChrisBeaumont/5758381/raw/descriptor_writeup.ipynb
'''


from weakref import WeakKeyDictionary

class NonNegative(object):
    """A descriptor that forbids negative values"""
    def __init__(self, default):
        self.default = default
        self.data = WeakKeyDictionary()
        
    def __get__(self, instance, owner):
        # we get here when someone calls x.d, and d is a NonNegative instance
        # instance = x
        # owner = type(x)
        return self.data.get(instance, self.default)
    
    def __set__(self, instance, value):
        # we get here when someone calls x.d = val, and d is a NonNegative instance
        # instance = x
        # value = val
        if value < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self.data[instance] = value

        
class Movie(object):
    
    #always put descriptors at the class-level  <=====
    rating = NonNegative(0)  
    runtime = NonNegative(0)
    budget = NonNegative(0)
    gross = NonNegative(0)
    
    def __init__(self, title, rating, runtime, budget, gross):
        self.title = title
        self.rating = rating
        self.runtime = runtime
        self.budget = budget
        self.gross = gross
    
    def profit(self):
        return self.gross - self.budget
    
    
m = Movie('Casablanca', 97, 102, 964000, 1300000)
print(m.budget)  # calls Movie.budget.__get__(m, Movie)   <====
print(m.__dict__)

m.rating = 100  # In concept calls Movie.rating.__set__(m, 100), not exactly

try:
    m.rating = -1   # calls Movie.rating.__set__(m, -1)
except ValueError:
    print ("Woops, negative value")

# del m.budget <=====   Movie.budget.__delete__(m)
