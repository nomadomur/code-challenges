# The provided code stub reads an integer, n, from STDIN. For all non-negative integers i < n, print i^2.

# ----------- 1 ----------

def sqr_n(n):
    for i in range(n):
        print(i * i)

if __name__ == '__main__':
    n = int(input())
    sqr_n(n)

# ----------- 2 ----------

# def sqr_n(n):
#     list(map(lambda i: print(i * i), range(n)))

# if __name__ == '__main__':
#     n = int(input())
#     sqr_n(n)