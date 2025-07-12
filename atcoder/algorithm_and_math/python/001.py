# 001 - Print 5+N 

# 実行時間制限: 1 sec / メモリ制限: 1024 MiB

# 配点: 1000 点

# 問題文
# りんごが 5 個あり、みかんが N 個あります。

# 整数 N が与えられるので、りんごとみかんを合わせて何個あるかを出力するプログラムを作成してください。

def all(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    fixed_value = 5
    user_input = int(input())
    print(all(fixed_value, user_input))


# コード長	    実行時間	メモリ	
# 172 Byte		9 ms	 8616 KiB	