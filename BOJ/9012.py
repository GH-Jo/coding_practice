Cases = int(input())
for _ in range(Cases):
    ps = input()
    stack = []
    try:
        for p in ps:
            if p=='(':
                stack.append('1')
            else:
                stack.pop()        
    except IndexError:
        print("NO")
        continue
    print("YES") if len(stack)==0 else print("NO")