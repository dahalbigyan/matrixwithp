class LineCounter:
    def __init__(self, filename):
        self.file=open(filename, 'r')
        self.lines=[]
    def read(self):
        self.lines = [line for line in self.file]
    def count(self):
        return len(self.lines)
lc = LineCounter('example_file.txt')
# print(lc.lines) # prints 0
# print(lc.count()) #prints 0
# lc.read();
# print(lc.lines)
# print(lc.count())
#Global variable
A = 5
def impure_sum(b):
    return b + A

def pure_sum(a,b):
    return b+a

# print(impure_sum(6))
# print(pure_sum(5,6))

# using function to count the same lines
def read_and_print(filename):
    with open(filename) as f:
        data = [line for line in f]
    for line in data:
        print(line)

# read_and_print('example_file.txt')

# lambda expression
sum_withlambda = lambda a, b: a+b

# map function
values = [1,2,3,4,5]
add_10 = map(lambda x: x+10, values)
print(add_10)
