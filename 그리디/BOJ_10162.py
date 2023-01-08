t = int(input())
buttons = [300,60,10]
ans = []


ans.append(t//buttons[0])
t = t % buttons[0]
ans.append(t//buttons[1])
t = t % buttons[1]
ans.append(t//buttons[2])
t = t % buttons[2]
if t > 0:
    print(-1)
else:
    for i in range(3):
        print(ans[i],end=' ')
