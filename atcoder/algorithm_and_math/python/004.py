# 004 - Product of 3 Integers 
# Ishga tushirish vaqti cheklovi: 1 soniya / Xotira cheklovi: 1024 MiB

# Ball: 
# 1000 ball

# Muammo matni
# 3 ta butun son A1, A2, A3 beriladi.

# A1 A2 A3 ni chiqaruvchi dastur yarating.

def product_of_three(a: int, b: int, c: int) -> int:
    return a * b * c

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(product_of_three(a, b, c))
    
# Kod uzunligi	Ishga tushirish vaqti	Xotira
# 444 Byte		10 ms	8644 KiB	