import heapq
import math
from itertools import permutations
from bisect import bisect, insort
from functools import reduce
import nltk
from nltk.corpus import wordnet


# Reverse the array
def reverse_arry(arr):
    l = 0
    h = len(arr) - 1
    while l < h:
        arr[l], arr[h] = arr[h], arr[l]
        l += 1
        h -= 1
    return arr


# Find the maximum and minimum element in an array
def swp(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


# Move all negative integer to one side
def move_all_negative(lst):
    l = 0
    h = len(lst) - 1
    while l < h:
        if lst[l] < 0:
            l += 1
        elif lst[h] > 0:
            h -= 1
        else:
            lst[l], lst[h] = lst[h], lst[l]
    return lst


# max sum sub array (Kadanes's Algorithm)
def kadane(lis):
    max_sum = 0
    curr_sum = 0
    for i in lis:
        curr_sum += i
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return max_sum


def min_height_diff(arr, k):
    for i in range(0, len(arr)):
        if (arr[i] - k) > k:
            arr[i] -= k
        else:
            arr[i] += k
    print(arr)
    return max(arr) - min(arr)


def min_jumps(arr):
    k = arr[0]
    pos = 0
    jumps = 1
    while pos < len(arr):
        if arr[pos] != 0:
            pos = k
            k = pos + arr[pos]
            jumps += 1
            if k >= len(arr) - 1:
                return jumps
        else:
            return -1


def find_duplicate(nums):
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    for i in freq.keys():
        if freq[i] > 1:
            return i

    print(freq)


def merge_sorted_arr(arr1, arr2):
    arr1.extend(arr2)
    arr1.sort()
    return arr1


"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""


def merge_overlaps(intervals):
    intervals.sort()
    disc = [intervals[0]]
    if len(intervals) > 1:
        for i in range(1, len(intervals)):
            if intervals[i][0] <= disc[-1][1]:
                disc[-1] = disc.append([min(disc[-1][1], intervals[i][0]), max(disc[-1][1], intervals[i][1])])
            else:
                disc.append(intervals[i])
    return disc


def merge_overlaps2(intervals):  # Editor Bug
    intervals.sort()
    disc = []
    n = len(intervals)
    for i in range(0, n):
        if len(disc) == 0:
            disc.append(intervals[i])
        else:
            if intervals[i][0] <= disc[-1][1]:
                disc[-1][1] = max(disc[-1][1], intervals[i][1])
            else:
                disc.append(intervals[i])
    return disc


A = [1, 5, 10, 20, 40, 80]
B = [6, 7, 20, 80, 100]
C = [3, 4, 15, 20, 30, 70, 80, 120]


def common_elements(n1, n2, n3):
    arr = set(n1 + n2 + n3)
    result = []
    for i in arr:
        if i in n1 and i in n2 and i in n3:
            result.append(i)
    return sorted(result)


def count_sum_pairs(arr, k):
    count = 0
    arr = list(permutations(arr, 2))
    print(arr)
    for i in arr:
        if sum(i) == k:
            print(i)
            count += 1
    return count // 2


def alt_neg_pos(arr):
    neg = []
    pos = []
    for i in arr:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)
    print(neg)
    print(pos)
    arr = []
    i = -1
    for i in range(min(len(pos), len(neg))):
        arr.append(pos[i])
        arr.append(neg[i])
    arr.extend(neg[i + 1:])
    arr.extend(pos[i + 1:])
    return arr


def leader(arr):
    leaders = []
    for i in range(len(arr) - 1):
        if arr[i] == heapq.nlargest(1, arr[i:])[0]:
            leaders.append(arr[i])
    leaders.append(arr[-1])
    return leaders


def facto(N):
    N = math.factorial(N)
    N = [N]
    while N[-1] > 0:
        N.insert(0, N[-1] % 10)
        N[-1] = N[-1] // 10
    N.pop()
    return N


def colors(arr):
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for i in arr:
        if i == 0:
            count_0 += 1
        elif i == 1:
            count_1 += 1
        else:
            count_2 += 1

    arr = [0] * count_0 + [1] * count_1 + [2] * count_2
    return arr


def next_permutation(nums):
    temp = nums
    nums = list(permutations(nums))
    nums.sort()
    for i in range(len(nums)):
        nums[i] = list(nums[i])
    for j in range(len(nums) - 2):
        if nums[j] == temp:
            nums = nums[j + 1]
            break


def count_inversion():  # TLE
    arr = [468, 335, 1, 170, 225, 479, 359, 463, 465, 206, 146, 282, 328, 462, 492, 496, 443, 328, 437, 392, 105, 403,
           154, 293, 383, 422, 217, 219, 396, 448, 227, 272, 39, 370, 413, 168, 300, 36, 395, 204, 312, 323]
    count = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count


def count_inversion_opti(arr):  # TLE
    a = enumerate(arr)
    sort_list = []
    result = 0
    for i, j in a:
        heapq.heappush(sort_list, (j, i))
    x = []
    while sort_list:
        j, i = heapq.heappop(sort_list)

        y = bisect(x, i)

        result += i - y

        insort(x, i)

    return result


def stocks(lis):
    lis = list(list)
    if lis == sorted(lis).reverse():
        return 0
    i = lis.index(min(lis))
    j = lis.index(max(lis))
    while i > j:
        if j > 0:
            lis.remove(lis[j])
        i = lis.index(min(lis))
        j = lis.index(max(lis))
        print(i, " ", j, " ", lis)
    return (max(lis) - min(lis)) if len(lis) > 1 else 0


def sieve(n):
    lis = [True] * n
    lis[0], lis[1] = False, False

    for i in range(2, n // 2):
        for j in range(i + 1, n):
            if j % i == 0:
                lis[j] = False
    for i in range(n):
        if lis[i]:
            print(i)


def pascal_triangle(n):
    for i in range(n):
        for j in range(n - i):
            print(" ", end="")
        a = 11 ** i
        while a:
            print(a % 10, end=" ")
            a //= 10
        print()


def triplet_sum(lis, x):
    triplets = list(permutations(lis, 3))
    print(triplets)
    flag = False
    for i in triplets:
        print(i)
        if sum(i) == x:
            flag = True
            break

    print(flag)


def synonyms(string):
    syn = []
    for synset in wordnet.synsets(string):
        for lemma in synset.lemmas():
            syn.append(lemma.name())
    return str(syn)


def bubble_sort(lis):
    for i in range(len(lis) - 1):
        swapped = False
        for j in range(len(lis) - 1 - i):
            if lis[j] > lis[j + 1]:
                lis[j] = lis[j] ^ lis[j + 1]
                lis[j + 1] = lis[j] ^ lis[j + 1]
                lis[j] = lis[j] ^ lis[j + 1]
                swapped = True
        if swapped is False:
            break
    return lis


def lucky_num():
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    c = 0
    for i in range(len(a)):
        if a[i] % 4 != 0:
            s = s + a[i]
            c = c + 1
    if s % 4 == 0:
        print(c // 2)
    else:
        print(-1)


def merge(a, b):
    len_a = len(a)
    len_b = len(b)
    s_list = []
    i = j = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            s_list.append(a[i])
            i += 1
        else:
            s_list.append(b[j])
            j += 1
    if i < len_a:
        s_list.extend(a[i:])
    else:
        s_list.extend(b[j:])
    return s_list


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


def partition(arr, low, high):
    pivot = arr[low]
    pivot_index = low
    while low < high:
        while low < len(arr) and arr[low] <= pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low < high:
            swap(low, high, arr)
    swap(high, pivot_index, arr)
    return high


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


if __name__ == "__main__":
    pass

"""s = input()
    st = set(s)
    freq = {}
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for i in st:
        if freq[i] > 1:
            print(i)
"""
"""
    n = int(input())
    lis = list(map(int, input().split()))
    def zero_one(lis):
        for i in range(1,n):
            if lis[i-1] != lis[i]:
                continue
            else:
                return "NO"

        return "YES"

    zero_one(lis)
"""

""" lis = list(map(int, input().split()))
    a = lis[0]
    b = lis[1]
    c = lis[2]
    if max(a,b,c)== a:
        if b+c>= a:
            print("YES")
        else:
            print("NO")
    elif max(a,b,c) == b:
        if a+c >= b:
            print("YES")
        else:
            print("NO")
    else:
        if a+b>= c:
            print("YES")
        else:
            print("NO")
"""

"""n = int(input())
    x = []
    y = []
    v = 0
    d = 0
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    for i in range(0, n):
        if x[i] != y[i]:
            d += 1
        elif i == 0:
            pass
        else:
            if x[i] == y[i]:
                v += 1

    if d != 0:
        print(0)
    else:
        print(v)
"""
