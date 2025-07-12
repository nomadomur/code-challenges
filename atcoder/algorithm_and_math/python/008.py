# 008 - Brute Force 1 
# 実行時間制限: 2 sec / メモリ制限: 1024 MiB

# 配点: 1000 点

# 問題文
# 赤・青のカードが各 1 枚ずつあり、あなたはそれぞれのカードに 1 以上 N 以下の整数を 1 つ書き込みます。

# カードに書かれた整数の合計が S 以下となる書き方は、いくつありますか？

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
    
# コード長	    実行時間	メモリ
# 678 Byte		48 ms	8708 KiB	