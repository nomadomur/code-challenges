# 005 - Modulo 100 
# Ishga tushirish vaqti cheklovi: 1 soniya / Xotira cheklovi: 1024 MiB

# Ball: 1000 ball

# Muammo matni
# N ta butun son a1, a2, ⋯, aN beriladi.

# (a1 +a2 +⋯+aN )mod100 qiymatini chiqaring.

def modulo(numbers: list) -> int:
    return sum(numbers) % 100

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    print(modulo(numbers))
    
# Kod uzunligi	Ishga tushirish vaqti	Xotira
# 432 Byte		9 ms	8632 KiB