# 1094
x = int(input())
sticks = [64]
while sum(sticks) > x:
    new = sticks[0]/2
    sticks.pop(0)
    if sum(sticks)+new >= x:
        sticks.insert(0, new)
    else:
        sticks.insert(0, new)
        sticks.insert(0, new)
print(len(sticks))
