def swap_case(s):
    
    nstring = ""
    for i in s:
        if i.isupper():
            nstring += i.lower()
        else:
            nstring += i.upper()
            
    return nstring
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# -------- 2 --------
# def swap_case(s):
#     return s.swapcase()

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)
