if __name__ == '__main__':
    
    N = int(input())
    lst = []

    for _ in range(N):
        command = input().split()
        
        if command[0] == 'insert':
            lst.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(lst)
        elif command[0] == 'remove':
            lst.remove(int(command[1]))
        elif command[0] == 'append':
            lst.append(int(command[1]))
        elif command[0] == 'sort':
            lst.sort()
        elif command[0] == 'pop':
            lst.pop()
        elif command[0] == 'reverse':
            lst.reverse()

# --------------- 2 -----------

# if __name__ == '__main__':
#     N = int(input())
#     lst = []

#     commands = {
#         'insert': lambda args: lst.insert(int(args[0]), int(args[1])),
#         'print': lambda args: print(lst),
#         'remove': lambda args: lst.remove(int(args[0])),
#         'append': lambda args: lst.append(int(args[0])),
#         'sort': lambda args: lst.sort(),
#         'pop': lambda args: lst.pop(),
#         'reverse': lambda args: lst.reverse()
#     }

#     for _ in range(N):
#         command, *args = input().split()
#         commands[command](args)
