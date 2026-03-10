# 002 - Sum of 3 Integers 
# Ishga tushirish vaqti cheklovi: 1 soniya / Xotira cheklovi: 1024 MiB

# Ball: 1000 ball

# Muammo matni
# 3 ta butun son A1, A2, A3 beriladi.

# A1 + A2 + A3 ni chiqaring.

def sum_of_three(a: int, b: int, c: int) -> int:
    return a + b + c
if __name__ == "__main__":
    a, b, c = map(int, input().split())
    # numbers = input().split()
    # a1 = int(numbers[0])
    # a2 = int(numbers[1])
    # a3 = int(numbers[2])

    print(sum_of_three(a, b, c))

# Kod uzunligi	Ishga tushirish vaqti	Xotira
# 524 Byte		13 ms	8668 KiB