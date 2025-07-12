# 006 - Print 2N+3 
# 実行時間制限: 1 sec / メモリ制限: 1024 MiB

# 配点: 1000 点

# 問題文
# 整数 N が与えられます。
# 2N+3 の値を出力してください。

def calc(n: int) -> int:
    return 2 * n + 3

if __name__ == "__main__":
    n = int(input())
    print(calc(n))
    
# コード長	    実行時間	メモリ
# 317 Byte		10 ms	8620 KiB