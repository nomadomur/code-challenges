# 007 - Number of Multiples 1 
# Ishga tushirish vaqti cheklovi: 1 soniya / Xotira cheklovi: 1024 MiB

# Ball: 1000 ball

# Muammo matni
# N dan kichik yoki teng musbat butun sonlar orasida、
# X ning karralisi yoki Y ning karralisi bo'lganlarning soni nechta？

def multiples_count(n: int, x: int, y: int) -> int:
    count = 0
    for i in range(1, n + 1):
        if i % x == 0 or i % y == 0:
            count += 1
    return count

if __name__ == "__main__":
    n, x, y = map(int, input().split())
    print(multiples_count(n, x, y))
    
# Kod uzunligi	Ishga tushirish vaqti	Xotira
# 593 Byte		64 ms	8740 KiB