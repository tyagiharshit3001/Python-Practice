'cls'
a = bool(1)
print(a)
name = "cheeko_boyee"
f = " is the best!!"
b = name.upper()  # convert string to upper case
c = name.replace('boyee', 'Boy')  # replace string data
d = name.lower()  # covert string to lower case
e = len(name)  # fiind length of string
print(name[0:2])  # print sting from index 0 to 10
print(name[::2])  # print every second letter of string
print(name[1:12:2])  # print every second letter of string up to 12th index
print(name + f)  # add up two strings
print(3 * name)  # replicate string 3 times
h = name.find('Harshit')  # if string isnt found returns -1
g = name.find('ko')  # to find string
print(c)
print(g)
print(h)
print(name[-3])
print('1' + '2')
tuple = (10, 95.5, 25, 3.094, "disco_deewane", "hard rock", 'HV',
         ("pop", "western", (30, 1, 2)))  # decleration of nested tuple (immutable)
print(tuple[7][2][0])  # access to item od nested list
list = ["john", "michel", "roy", 7078179015, 1702, 30101]  # decleration of list (mutable)
print(list[2:5])  # slicing in list
print(list)
list.extend(["cheeko", "boyee", "disco_deewane"])  # add new item to list
print(list)
list.append([10, 20, 30, 40])  # add list inside the list
print(list)
del (list[3])  # delet the item of list
print(list)
print("hard rock".split())  # break up the string
print(list[1:])
setA = {'hockey', 'cricket', 'baseball', 'football'}  # decleration of set
print(setA)
setA.add("wrestling")  # adding element to set
print(setA)
setA.remove("cricket")  # remove element from set
print(setA)
print("cricket" in setA)  # check if element exist in set
print("hockey" in setA)  # check if element exist in set
dict = {"A": 1, 'B': 222, "C": 5221, 'D': 9502, 'E': 9055, "F": 9506}  # dictionary("key":value)
print(dict["C"])  # access to dict elements

l = 72
if (l < 70):
    print("You Got Avarage marks!!!")  # conditional
else:
    print("You Got Good marks!!")

for i in range(0, 5):  # for loop
    list[i] = "Oops!"
print(list)

i = 0
while (list[i] == "Oops!"):
    list[i] = "Harshit"  # while loop
    i = i + 1

print(list)
num_list = [15, 32, 0.22, 35, 41, 0, 8, 33.32564, 3.142857, 9.055, 299]
print(num_list)

sorted_list = sorted(num_list)  # sorting using sorted function
print(sorted_list)  # sorted() func. creates a new sorted list

num_list.sort()  # sorting using sort() function
print(num_list)  # sort function changed with in the old list


def add(x, y):
    """
    add two numbers
    """
    x = x + y
    return x


x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = add(x, y)
print("Result", z)

File1 = open("C:/Users/Prasant tyagi/Desktop/cheeko.txt", "a")
File1.write("\n This is a line A")
print(File1.closed)

File1 = open("C:/Users/Prasant tyagi/Desktop/cheeko.txt", "r")
file_stuff = File1.read()
print(file_stuff)
print(File1.closed)

with open("cheeko.txt", "r")as readfile:
    with open("boyee.txt", "w")as writefile:
        for line in readfile:
            writefile.write(line)

File2 = open("C:/Users/Prasant tyagi/Desktop/boyee.txt", "r")
file_stuff2 = File2.read()
print(file_stuff2)
print(File2.closed)
