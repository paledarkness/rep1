n = int(input())
a = list(map(int, input().split(' ')))
b = (sorted(a))[:3]
for i in b:
    a.remove(i)
print(*(b + a))
