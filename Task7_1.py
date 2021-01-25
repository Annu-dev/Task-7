# Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]

import math as "mt"

C = 5
H = 3

class SquareRoot:
    def __init__(self,values):
        self.values = values
    def calculate(self):
        self.values = self.values.split(',')
        convset = map(int,self.values)
        result = []
        for D in convset:
            Q= mt.sqrt((2*C*D)/H)
            result.append(Q)
        return result

values = input("enter D with comma seperation ")
sq = SquareRoot(values)
print(sq.calculate())
