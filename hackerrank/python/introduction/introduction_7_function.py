# The included code stub will read an integer, n , from STDIN.

# Without using any string methods, try to print the following:

# ----------- 1 ----------

def nmb(n):
    for i in range(n):
        print(i + 1, end="")

if __name__ == '__main__':
    n = int(input())
    nmb(n)

# ----------- 2 ----------

# def print_numbers(n):
#     print(*range(1, n + 1), sep='')
# if __name__ == '__main__':
#     n = int(input())
#     print_numbers(n)
    
# ----------- 3 ----------

# def print_numbers(n):
#     print(''.join(str(i) for i in range(1, n + 1)))
# if __name__ == '__main__':
#     n = int(input())
#     print_numbers(n)

