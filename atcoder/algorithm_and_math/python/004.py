# 004 - Product of 3 Integers 
# 実行時間制限: 1 sec / メモリ制限: 1024 MiB

# 配点: 
# 1000 点

# 問題文
# 3 つの整数 A1 ,A2 ,A3 が与えられます。

# A1 A2 A3 を出力するプログラムを作成してください。

def product_of_three(a: int, b: int, c: int) -> int:
    return a * b * c

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(product_of_three(a, b, c))
    
# コード長	    実行時間	メモリ
# 444 Byte		10 ms	8644 KiB	