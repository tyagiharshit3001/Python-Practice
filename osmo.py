"""

"""
"""products = {
    'Clothing': {
        'TSHIRT': [1000, 100],
        'JACKET': [2000, 100],
        'CAP': [500, 100]
    },
    'Stationary': {
        'NOTEBOOK': [200, 40],
        'PEN': [300, 30],
        'MARKERS': [500, 25]
    }
}
category = {
    'TSHIRT': 'Clothing',
    'JACKET': 'Clothing',
    'CAP': 'Clothing',
    'PEN': 'Stationary',
    'NOTEBOOK': 'Stationary',
    'MARKERS': 'Stationary'
}

items_list = {}
count_c = count_s = 0
total = 0
discount = 0
while True:
    n = input()
    if n == "PRINT_Bill":
        for i in items_list.keys():
            total += items_list[i] * products[category[i]][i][0]
            discount += items_list[i] * products[category[i]][i][1]
        total_copy = total
        if total_copy > 1000:
            total -= discount
        else:
            discount = 0
        if total_copy > 3000:
            total += 0.05 * total
            discount += 0.05 * total
        total += 0.1 * total
        print("TOTAL_DISCOUNT  {0:.2f}".format(discount))
        print("TOTAL_AMOUNT_TO_PAY  {0:.2f}".format(total))
        break
    n = n.split()
    opt = n[0]
    item = n[1]
    quant = int(n[2])
    if quant <= 2 and category[item] == 'Clothing':
        count_c += quant
        if item in items_list:
            items_list[item] += quant
        else:
            items_list[item] = quant
        print("ITEM_ADDED")
    elif quant <= 3 and category[item] == 'Stationary':
        count_s += quant
        if item in items_list:
            items_list[item] += quant
        else:
            items_list[item] = quant
        print("ITEM_ADDED")
    else:
        print("ERROR_QUANTITY_EXCEEDED")
"""

"""
def anglePrediction(mobileNumber):
    angle_numbers = [000, 111, 222, 333, 444, 555, 666, 777, 888, 999]
    mobileNumber = str(mobileNumber)
    angle_msg = {
        '000': "Message_of_000",
        '111': "Message_of_111",
        '222': "Message_of_222",
        '333': "Message_of_333",
        '444': "Message_of_444",
        '555': "Message_of_555",
        '666': "Message_of_666",
        '777': "Message_of_777",
        '888': "Message_of_888",
        '999': "Message_of_999"
    }
    for i in range(len(angle_numbers)):
        if str(angle_numbers[i]) in mobileNumber:
            return angle_msg[str(angle_numbers[i])]


mobileNumber = int(input())
print(anglePrediction(mobileNumber))
"""


def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def partition(arr, low, high):
    pivot_index = low
    pivot = arr[pivot_index]
    x = low + 1
    y = high - 1
    while x < y:
        while arr[x] < pivot and x < len(arr):
            x += 1
        while arr[y] > pivot:
            y -= 1
        if x < y:
            swap(arr, x, y)
        swap(arr, pivot_index, y)

    return y


def quick_sort(arr, low, high):
    if low < high:
        print(arr)
        k = partition(arr, low, high)
        quick_sort(arr, low, k - 1)
        quick_sort(arr, k + 1, high)


if __name__ == '__main__':
    arr = [7, 3, 5, 64, 9, 10, 0, 22, 6]
    low = 0
    high = len(arr)
    # quick_sort(arr, low, high)
