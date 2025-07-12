# 002 - Sum of 3 Integers 
# 実行時間制限: 1 sec / メモリ制限: 1024 MiB

# 配点: 1000 点

# 問題文
# 3 つの整数 A1 ,A2 ,A3 が与えられます。

# A1 +A2 +A3 を出力してください。

def sum_of_three(a: int, b: int, c: int) -> int:
    return a + b + c
if __name__ == "__main__":
    a, b, c = map(int, input().split())
    # numbers = input().split()
    # a1 = int(numbers[0])
    # a2 = int(numbers[1])
    # a3 = int(numbers[2])

    print(sum_of_three(a, b, c))

# コード長	    実行時間	メモリ
# 524 Byte		13 ms	8668 KiB