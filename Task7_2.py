```
Define a class named Shape and its subclass Square. The Square class has an init function which
takes length as argument. Both classes have an area function which can print the area of the shape
where Shape’s area is 0 by default.
```

class Shape:

    def area(self):
        self.area_var = 0
        print("area of shape is: ",self.area_var)

class Square(Shape):
    def __init__(self,length):
        self.length = length
    
    def area(self):
        area = (self.length * self.length)
        print("Area of the square with length",self.length,"is:",area)

input_length = int(input("Enter the value of length: "))
sp = Shape()
sp.area()
sq = Square(value_length)
sq.area()