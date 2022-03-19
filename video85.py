def function1():

    print("subcrides now")

    fun2 = function1
    del fun2
    function1()