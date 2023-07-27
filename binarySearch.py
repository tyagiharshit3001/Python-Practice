import time


# decorator
def time_it(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        fun(*args, **kwargs)
        end = time.time()
        print(fun.__name__ + " took " + str((end - start) * 1000) + " mil sec")

    return wrapper


# generator
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def drive_fib(n):
    for f in fib():
        if f > n:
            break
        print(f, end=" ")


# @time_it
def binarySearch(lis, low, high, data):
    lis.sort()
    mid = (low + high) // 2
    if high >= low:
        if data == lis[mid]:
            print(f"{data} exist at index = {mid}.")
            return
        elif data < lis[mid]:
            high = mid - 1
            binarySearch(lis, low, high, data)
        else:
            low = mid + 1
            binarySearch(lis, low, high, data)
    else:
        print(f"{data} doesn't exist in list.")


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    binarySearch(arr, 0, len(arr), 4)
