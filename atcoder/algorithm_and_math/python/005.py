# 005 - Modulo 100 
# 実行時間制限: 1 sec / メモリ制限: 1024 MiB

# 配点: 1000 点

# 問題文
# N 個の整数 a1 ,a2 ,⋯,aN が与えられます。

# (a1 +a2 +⋯+aN )mod100 の値を出力してください。

def modulo(numbers: list) -> int:
    return sum(numbers) % 100

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    print(modulo(numbers))
    
# コード長	    実行時間	メモリ
# 432 Byte		9 ms	8632 KiB