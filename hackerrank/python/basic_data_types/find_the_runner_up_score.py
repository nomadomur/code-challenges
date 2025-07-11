if __name__ == '__main__':
    n = int(input())
    arr = sorted(set(map(int, input().split())))
    
    print(arr[-2])

    # sorted_arr = sorted(arr)
    # max_a = max(sorted_arr)
    # b = [i for i in sorted_arr if i != max_a]
    # print(max(b))
