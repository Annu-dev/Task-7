```
Write a Person class with an instance variable “age” and a constructor that takes an integer as a
parameter. The constructor must assign the integer value to the age variable after confirming the
argument passed is not negative; if a negative argument is passed then the constructor should set
age to 0 and print “Age is not valid, setting age to 0”.

```

class Person:

    def __init__(self,age):
        self.age = age
        if self.age < 0:
            self.age = 0
            print("Age is not valid, setting age to 0")
    
    def addAge(self, add_age):
        new_age_afteraddition = add_age + self.age
        print(new_age)

    def howOld(self):
        if self.age > 0 and self.age < 13:
            print("You are school young")
        elif self.age >= 13 and self.age <= 19:
            print("You are a teen")
        else:
            print("You are old enough")

for i in range(0,7):
    age = int(input("Please enter your age: "))
    person = Person(input_age)
    person.howOld()
add_age = int(input("Enter number to be added to your age: "))
person.addAge(add_age)
