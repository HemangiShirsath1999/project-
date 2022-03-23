n = int(input("Enter the number of Apples given to Harry:"))
min = int(input("Enter the minimum number of students:"))
max = int(input("Enter the maximum number of students:"))

for i in range(min,max+1):
    if n % i == 0:
        print(i,"is divisior of", n)
    else:
        print(i, "is not divisor of", n)
