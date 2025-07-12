# 003 - Sum of N Integers 
# 実行時間制限: 1 sec / メモリ制限: 1024 MiB

# 配点: 1000 点

# 問題文
# 整数 N と 
# N 個の整数 A1 ,A2 ,⋯,AN が与えられます。（入力の形式は「入力」セクションを参照）

# A1 +A2 +⋯+AN を出力してください。

# --------------- 1 ---------------

def sum_of_n(n: int, numbers: list) -> int:
    return sum(numbers)

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    print(sum_of_n(n, numbers))
    
# コード長	    実行時間	メモリ
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