# ------------------ 1 -----------
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
# ------------------ 2 -----------

# if __name__ == '__main__':
#     n = int(input())
#     print(hash(tuple(map(int, input().split()))))