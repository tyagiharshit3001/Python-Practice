import math

"""
5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5

"""
"""
Pattern: p1
n=5

  *         
 ***        
*****       
@   @
@   @
@   @
@ * @
@***@
*****
"""


def p1():
    n = int(input('Enter odd number > 3: '))
    for i in range(math.ceil(n / 2)):
        for j in range(n // 2 - i):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        print()
    for i in range(math.ceil(n / 2)):
        print("@", end="")
        for j in range(n - 2):
            print(" ", end="")
        print("@")
    for i in range(math.floor(n / 2)):
        print("@", end="")
        for j in range(math.floor(n / 2) - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        for j in range(math.floor(n / 2) - i - 1):
            print(" ", end="")
        print("@")
    for i in range(n):
        print("*", end="")


"""
n = 4

@
@
@
@
@****
    ****
        ****
            ****@
                @
                @
                @
                @

"""


def p2():
    n = 3
    for i in range(n):
        print("@")
    print("@", end="")
    for k in range(n):
        for m in range(n * k):
            print(" ", end="")
        for l in range(n):
            print("*", end="")
        print() if k != n - 1 else print("", end="")
    print("@")
    for j in range(n):
        for k in range(n ** 2):
            print(" ", end="")
        print("@")


"""
Pattern p3:
n = 4

@****
@    ****
@        ****
@            ****@
@                @
                 @
                 @
                 @
"""


def p3():
    n = int(input("Enter number >=2: "))
    for i in range(n):
        print("@", end="")
        for j in range(n * i):
            print(" ", end="")
        for k in range(n):
            print("*", end="")
        print() if i != n - 1 else print("@")
    print("@", end="")
    for l in range(n):
        for _ in range(n ** 2):
            print(" ", end="")
        print(" @") if l != 0 else print("@")


"""
 Pattern p4:
 n = 7
 
          *         
         ***        
        *****
       *******  _    
       @--5--@  |
       @     @  |
       @     @  5
       @     @  |
       @     @  |
*******@--5--@*******|  
 *****----7----***** |
  ***-----9-----***  |
   *------11-----*   |
----------21---------|
 
 """


def p4():
    n = int(input("Enter odd number >=3: "))
    a = n
    for i in range(math.ceil(n / 2)):
        for _ in range(n + math.floor(n / 2) - i):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()

    for i in range(n - 2):
        for _ in range(n):
            print(" ", end="")
        print("@", end="")
        for k in range(n - 2):
            print(" ", end="")
        print("@")

    for i in range(n):
        print("*", end="")
    print("@", end="")
    for k in range(n - 2):
        print(" ", end="")
    print("@", end="")
    for i in range(n):
        print("*", end="")
    # ----------------------
    print()
    for i in range(math.ceil(n - 2)):
        for k in range(i + 1):
            print(" ", end="")
        for j in range(n - 2 - 2 * i):
            print("*", end="")
        for l in range(a + 2):
            print(" ", end="")
        for j in range(n - 2 - 2 * i):
            print("*", end="")
        a += 2
        print()


"""
Pattern p5:
n=6

@
@
@
@******
@     ******
@          ******               @
@               ******          @
                     ******     @
                          ******@
                                @
                                @
                                @

"""


def p5():
    pass


"""
**********
****  ****
***    ***
**      **
*        *
**      **
***    ***
****  ****
**********
"""


def p6():
    n = int(input("Enter number: "))
    for i in range(n):
        for k in range(n - i, 0, -1):
            print("*", end="")
        for j in range(0, 2 * i, 2):
            print(" ", end="")
        for j in range(0, 2 * i, 2):
            print(" ", end="")
        for k in range(n - i, 0, -1):
            print("*", end="")
        print()

    for i in range(1, n):
        for j in range(0, i + 1):
            print("*", end="")
        for j in range(2, 2*(n - i), 2):
            print(" ", end="")
        for j in range(2, 2*(n - i), 2):
            print(" ", end="")
        for j in range(0, i + 1):
            print("*", end="")
        print()


if __name__ == "__main__":
    p6()
