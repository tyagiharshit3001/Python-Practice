"""
class Opps:

    def __init__(self):
        print('Hello penguin this is opps constructor')

    def func(self):
        print('This is oops function 1')


class Opps2(Opps):

    def __init__(self):
        print('Hello aliens, This is opps2 constructor')

    def func2(self):
        print('This is oops function 2')


class Opps3(Opps):

    def __init__(self):
        print('Hello aliens, This is opps3 constructor')

    def func3(self):
        print('This is oops function 3')


if __name__ == "__main__":
    obj = Opps3()
    obj2 = Opps2()

"""
import threading
import time

"""
class Opps:

    def __init__(self, data):
        print('Hello penguin this is opps constructor')
        # data = 0
        print(data)
        time.sleep(0.5)

    def func(self):
        for i in range(3):
            print('This is oops function 1')
            time.sleep(0.5)


class Opps2(Opps):

    def __init__(self, data):
        super().__init__(data)
        print('Hello aliens, This is opps2 constructor')
        time.sleep(0.3)

    def func2(self):
        for i in range(3):
            print('This is oops function 2')
            time.sleep(0.3)


class Opps3(Opps2):

    def __init__(self, data):
        super().__init__(data)
        print('Hello aliens, This is opps3 constructor')
        time.sleep(0.75)

    def func3(self):
        print('This is oops function 3')
        time.sleep(0.75)


if __name__ == "__main__":
    obj = Opps3(143)
    t = time.time()
    t1 = threading.Thread(target=obj.func())
    print("--------------------")
    t2 = threading.Thread(target=obj.func2())
    print("--------------------")
    t3 = threading.Thread(target=obj.func3())
    print("--------------------")
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()

    print(time.time() - t)
"""


class M:
    def __init__(self):
        self._data = 10

    def __fun(self):
        return print("Hello private world")


""" def func(self):
        self.__fun()
"""


class N(M):

    def __init__(self):
        super().__init__()
        print(self._data)



obj = N()

