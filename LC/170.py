class TwoSum:

# initialize data structure
def __init__(self):
    self.table = dict()

# @return nothing
def add(self, number):
    self.table[number] = self.table.get(number, 0) + 1;

# @param value, an integer
# @return true or false
def find(self, value):
    for i in self.table.keys():
        j = value - i
        if i == j and self.table.get(i) > 1 or i != j and self.table.get(j, 0) > 0:
            return True
    return False