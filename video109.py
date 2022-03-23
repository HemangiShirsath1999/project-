a = sorted(list(map(int,input().split())))
print(a[::-1])
print(list(reversed(a)))
for i in range(len(a)//2):
	a[i],a[-(i+1)] = a[-(i+1)], a[i]
print(a)