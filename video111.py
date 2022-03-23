name = hemangi shirsath
lst = []
print("How many items you want")
i = int(input())
for i in range(0,i):
    print("Enter the items")
    items = int(input())
    lst.append(items)
    if items>10:
        lst.remove(items)
        lst.append(items+1)
print(lst)