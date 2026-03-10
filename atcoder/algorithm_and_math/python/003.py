# 003 - Sum of N Integers 
# Ishga tushirish vaqti cheklovi: 1 soniya / Xotira cheklovi: 1024 MiB

# Ball: 1000 ball

# Muammo matni
# Butun son N va N ta butun son A1, A2, ⋯, AN beriladi. (Kirish shakli uchun "Kirish" bo'limiga qarang)

# A1 + A2 + ⋯ + AN ni chiqaring.

# --------------- 1 ---------------

def sum_of_n(n: int, numbers: list) -> int:
    return sum(numbers)

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    print(sum_of_n(n, numbers))
    
# Kod uzunligi	Ishga tushirish vaqti	Xotira
# 561 Byte		10 ms	8548 KiB

# --------------- 2 ---------------
# def  sum_of_n(n: int, numbers: list) -> int:
#     result = 0
#     for i in range(n):
#         result += numbers[i]
#     return result

# if __name__ == "__main__":
#     n = int(input())
#     numbers = list(map(int, input().split()))
#     print(sum_of_n(n, numbers))

# コード長	    実行時間	メモリ
# 267 Byte		10 ms	8644 KiB