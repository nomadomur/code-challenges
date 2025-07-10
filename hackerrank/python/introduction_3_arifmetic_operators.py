# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

# ----- 1 ----------
def calculate(a, b):
    print(a + b)
    print(a - b)
    print(a * b)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    calculate(a, b)
# ----- 2 ----------

# if __name__ == '__main__':
#     a, b = int(input()), int(input())
#     for rlt in (a + b, a - b, a * b):
#         print(rlt)
        
# ----- 3 ----------

# if __name__ == '__main__':
#     a, b = map(int, [input(), input()])
#     print(a + b, a - b, a * b, sep='\n')