n = int(input())

stack = []

for _ in range(n):
    command = input().split()
    if command[0] == '1':
        stack.append(int(command[1]))
    elif command[0] == '2':
        if len(stack) > 0:
            stack.pop()
    elif command[0] == '3':
        
        if stack:
            print(max(stack))
    elif command[0] == "4":
        if stack:
            print(min(stack))

stack.reverse()
print(", ".join(map(str, stack)))