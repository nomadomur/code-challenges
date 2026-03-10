# Berilgan butun son, n, quyidagi shartli harakatlarni bajaring:

# Agar n toq bo'lsa, Weird chop eting
# Agar n juft bo'lsa va 2 dan 5 gacha (shu jumladan), Not Weird chop eting
# Agar n juft bo'lsa va 6 dan 20 gacha (shu jumladan), Weird chop eting
# Agar n juft bo'lsa va 20 dan katta bo'lsa, Not Weird chop eting

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

def check_weird(n):
    if n % 2 == 1:
        return "Weird"
    elif n % 2 == 0 and 2 <= n <= 5:
        return "Not Weird"
    elif n % 2 == 0 and 6 <= n <= 20:
        return "Weird"
    elif n % 2 == 0 and n > 20:
        return "Not Weird"

if __name__ == '__main__':
    n = int(input().strip())
    print(check_weird(n))