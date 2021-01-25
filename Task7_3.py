class FindThreeElements:
    def __init__(self,values):
        self.values = values

    def elements(self):
        lt = len(self.values)
        result_set = []
        sol = 0
        for first in range(0, lt):
            for second in range(first+1, lt):
                for third in range(second+1, lt):
                    if self.values[first] + self.values[second] + self.values[third] == sol:
                        result.append([self.values[first],self.values[second],self.values[third]])
        print(result)

list_numbers = [9,2,-3,-6,9,0,8]
sum = FindThreeElements(list_numbers)
sum.elements()