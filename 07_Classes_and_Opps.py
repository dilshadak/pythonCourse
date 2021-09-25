# Why use classes
# Mimicing real world entity by associating
# methods, properties to it

# A simple class
class SmallestClass:
    pass

# ClassRoom object
smallest_class = SmallestClass()
print(type(smallest_class))
help(smallest_class)

# Class variable
class ClassVar():
    '''
    This class has class variable
    '''
    class_variable = 10

class_var = ClassVar()
class_var.class_variable = 20
print(class_var.class_variable)
print(class_var.__doc__)
help(class_var)

# Class methods
class ClassMethod:
    '''
    This class has class variable, and method
    '''
    class_variable = 10

    def method(self):
        self.method_varibale = 20

cm_object1 = ClassMethod()
cm_object1.class_variable = 'Hello'
print(cm_object1.class_variable)
# print(class_method.method_varibale)
cm_object1.method()
print(cm_object1.method_varibale)
cm_object1.method_varibale = 'Hi'
print(cm_object1.method_varibale)

cm_object2 = ClassMethod()
cm_object2.method()
print(cm_object2.class_variable)
print(cm_object2.method_varibale)

# Constructors and Magic Methods in Python
class Vector:
    '''
    Class of vectors for addition, subtraction and dot products
    between two vectors.
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mag = (x**2 + y**2)**0.5

    def __str__(self): # when printed
        return f'Vector ({self.x}, {self.y})'
    
    def __add__(self, other): # +
        return Vector(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other): # -
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other): # *
        return self.x * other.x + self.y * other.y
   
v1 = Vector(2, 10)
v2 = Vector(5, -2)
v3 = Vector(3, 7)

# print(v1)
# print(v1.mag)
# print(v1 + v2)
# print(v1 - v2)
# print(v1 + v2 + v3)
# print(v1*v2)

# Inheritance, Method Overriding
class Shape:
    shapes = []

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = length * width
        self.perimeter = 2*(length + width)
        Shape.shapes.append(self)

    def __add__(self, other):
        return Rectangle(self.length + other.length, self.width + other.width)

    def __str__(self):
        return f'Length: {self.length}, Width: {self.width}'

    def info(self):
        print(f'Rectangle with Area: {self.area}, and Perimeter: {self.perimeter}')    

class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
    
    def __str__(self):
        return f'Side: {self.length}'

    def info(self):
        print(f'Square with Area {self.area}, Perimeter {self.perimeter}')

rect = Rectangle(2, 3)
rect.info()

sqr = Square(8)
sqr.info()
print(isinstance(sqr, Square))
for shp in Shape().shapes:
    shp.info()
    print(shp)

new = rect + sqr
new.info()

# Multiple inheritance
class A:
    def __init__(self):
        print('A initialized')

class B:
    def __init__(self):
        print('B initialized')
        self.vb = 'b'
        # super().__init__()

    def x(self):
        print('method x of B is called')

class C:
    def __init__(self):
        print('C initialized')
        self.vc = 'c'
        # super().__init__()
    def c(self):
        print('method c of C is called')

    def x(self):
        print('method x of C is called')

# Method Resolution Order (MRO)
class D(B, C):
    def __init__(self):
        print('D initialized')
        B.__init__(self)
        C.__init__(self) # Does not override method

    def x(self):
        print('method x of D is called')

d = D()
d.c()
print(d.vb)
# print(d.vc)
d.x()