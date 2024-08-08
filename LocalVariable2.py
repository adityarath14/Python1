def fun1():
    print('Hello')
    def fun2():
        print('Hi')
        def fun3():
            print('Good')
        fun3()
    fun2()
print('Bye')
fun1()