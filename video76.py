def myfunc():
    print("Code With Harry")
    while True:
        value = (yield)
        print(value)

coroutine =myfunc()
next(coroutine)
coroutine.send("Python")
coroutine.send(" Tutorial ")
coroutine.close()