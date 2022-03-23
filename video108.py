st = [int(input("Enter the list Element:\n")) for i in range(3)]
print(f"Your list is {lst}")
while True:
    choice1 = int(input("Enter 1(Traditional Method),2(Slicing Method) or 3(Swaping Method) for reverse the List:\n"))
    if choice1 == 1:
        lst1 = lst[:]
        lst1.reverse()
        print("The Answer of First Method is :",lst1)
    elif choice1 == 2:
        lst2 = lst[::-1]
        print("The Answer of Second Method is :", lst2)
    elif choice1 == 3:
        for i in range(len(lst)//2):
            lst[i], lst[len(lst)-i-1] = lst[len(lst)-i-1], lst[i]
        print("The Answer of Third Method is :", lst)
    choice2 = input("C for Continue and Q for Quit:\n")
    if choice2.capitalize() == 'Q':
        break
    if choice2.capitalize() == 'C':
        continue
print("Thank You.")
