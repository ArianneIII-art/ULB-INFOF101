list, i = [], int(input())

while i != -1:
    list.append(i)
    i = int(input())

print(sum(list)/len(list))