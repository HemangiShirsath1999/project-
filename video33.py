def sum():
    a = 10  # local variable cannot be accessed outside the function
    b = 20
    sum = a + b
    print(sum)


print(a)  # this gives an error