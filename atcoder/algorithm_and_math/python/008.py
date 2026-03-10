# 008 - Brute Force 1 
# Ishga tushirish vaqti cheklovi: 2 soniya / Xotira cheklovi: 1024 MiB

# Ball: 1000 ball

# Muammo matni
# Qizil va ko'k kartalar har biri 1 tadan bor, siz har bir kartaga 1 dan N gacha butun son yozasiz.

# Kartalarga yozilgan butun sonlarning yig'indisi S dan kam yoki teng bo'lgan yozish usullari nechta？

def c_card_comb(n: int, s: int) -> int:
    count = 0
    for red in range(1, n + 1):
        for blue in range(1, n + 1):
            if red + blue <= s:
                count += 1
    return count

if __name__ == "__main__":
    n, s = map(int, input().split())
    print(c_card_comb(n, s))
    
# Kod uzunligi	Ishga tushirish vaqti	Xotira
# 678 Byte		48 ms	8708 KiB	