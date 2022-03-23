n = int(input("\nHow many inputs?\n"))

while n > 0:
    a = int(input())
    b = a
    c = a
    n = n-1
    while True:
        if c == int(str(b)[::-1]):
            print(f"Next palindrome for {a} is {b}.")
            break
        else:
            b = b+1
            c = c+1

