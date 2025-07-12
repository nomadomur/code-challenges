# 007 - Number of Multiples 1 
# 実行時間制限: 1 sec / メモリ制限: 1024 MiB

# 配点: 1000 点

# 問題文
# N 以下の正の整数の中で、
# X の倍数または Y の倍数であるものの個数はいくつありますか？

def multiples_count(n: int, x: int, y: int) -> int:
    count = 0
    for i in range(1, n + 1):
        if i % x == 0 or i % y == 0:
            count += 1
    return count

if __name__ == "__main__":
    n, x, y = map(int, input().split())
    print(multiples_count(n, x, y))
    
# コード長	    実行時間	メモリ
# 593 Byte		64 ms	8740 KiB