"""
y = int(input("Enter year: "))
if y % 4 == 0:
    if y % 400 and y % 100:
        print(y, "is a leap year.")

else:
    print(y, "is not a leap year.")
"""

"""
x = int(input("Enter number: "))
s = 0
n = x
while x > 0:
    a = x % 10
    s = s *10 + a
    x = x // 10

if s == n:
    print(n, " is a palindrome")
else:
    print(n, " is not a palindrome number.")
"""

"""
def sel():
    print("For Fahrenheit to Celsius - - - - -> [1]")
    print("For Celsius to Fahrenheit - - - - -> [2]")
    o = int(input("Enter option: "))
    if o == 1:
        cel()
    elif o == 2:
        farn()
    else:
        print("Invalid option!!!")


def farn():
    a = int(input("Enter temperature: "))
    print(((9 * a) / 5) + 32, " C")


def cel():
    b = int(input("Enter temperature: "))
    print(((b - 32) * 5) / 9, " F")


sel()
"""

# Linked list
"""
def fun():
    print("\n Following are the operations in Linked List...")
    print("Press [1]-------> To create linked List")
    print("Press [2]-------> To insert data in Beginning.")
    print("Press [3]-------> To insert data from end.")
    print("Press [4]-------> To find out the length of Linked List.")
    print("Press [5]-------> To insert at position.")
    print("Press [6]-------> To delete at position.")
    print("Press [7]-------> To insert by value")
    print("Press [8]-------> To delete value.")
    p = int(input("Enter option: "))
    return p


class Node:
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beg(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        i = self.head
        while i.nxt:
            i = i.nxt
        i.nxt = Node(data, None)

    def length2(self):
        count = 0
        i = self.head
        while i:
            count += 1
            i = i.nxt
        return count

    def insert_pos(self, pos, data):
        r = ll.length2()
        if pos < 0 or pos >= r:
            print("Position dosn't exist in Linked List.")
            return
        count = 1
        i = self.head
        while i:
            count += 1
            i = i.nxt
            if count is pos - 1:
                node = Node(data, i.nxt)
                i.nxt = node

    def remove_at(self, pos):
        ll.display()
        if pos == 1:
            i = self.head
            i = i.nxt
            return
        if pos <= 0 or pos >= ll.length2():
            raise Exception("Invalid Position!!!")
        i = self.head
        count1 = 0
        while i:
            i = i.nxt
            count1 += 1
            if count1 == pos - 1:
                i.nxt = i.nxt.nxt
                break

    def insert_by_val(self, by_value, data):
        i = self.head
        if i is None:
            return
        if i.data == by_value:
            node = Node(data, i.nxt)
            i.nxt = node
            return
        while i:
            i = i.nxt
            if i.data == by_value:
                node = Node(data, i.nxt)
                i.nxt = node

    def remove_by_val(self, data1):
        i = self.head
        if i is None:
            return
        if i.data == data1:
            i = i.nxt
            return
        i = self.head
        while i:
            if i.data == data1:
                i.nxt = i.nxt.nxt
            i = i.nxt

    def display(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        i = self.head
        llstr = ''
        while i:
            llstr += str(i.data) + '------>'
            i = i.nxt

        print(llstr)


if __name__ == "__main__":
    o = 1
    loop = True
    ll = LinkedList()
    while loop:
        q = fun()
        if q == 1:
            print("Implement linked lis by entering  data...")
            while o:
                ll.insert_beg(int(input("\n Enter data: ")))
                o = int(input("Do you again wants to enter data [1/0] : "))
            ll.display()
        elif q == 2:
            while o:
                ll.insert_beg(int(input("\n Enter data: ")))
                o = int(input("Do you again wants to enter data [1/0] : "))
            ll.display()
        elif q == 3:
            while o:
                ll.insert_end(int(input("\n Enter data: ")))
                o = int(input("Do you again wants to enter data [1/0] : "))
            ll.display()
        elif q == 4:
            length1 = ll.length2()
            print(length1)
            ll.display()
        elif q == 5:
            length1 = ll.length2()
            ll.display()
            ll.insert_pos(int(input("Enter Position: ")), int(input("Enter data item: ")))
            ll.display()
        elif q == 6:
            length1 = ll.length2()
            ll.display()
            ll.remove_at(int(input("\n Enter Position: ")))
            ll.display()
        elif q == 7:
            length1 = ll.length2()
            ll.display()
            ll.insert_by_val(int(input("\n Enter value at position: ")), int(input("\n Enter data: ")))
            ll.display()
        elif q == 8:
            length1 = ll.length2()
            ll.display()
            ll.remove_by_val(int(input("\n Enter value at position: ")))
            ll.display()
        else:
            loop = False
"""

# stack implementation

"""
class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def tos(self):
        return self.stack[-1]

    def length(self):
        return len(self.stack)

    def display(self):
        return self.stack


def fun():
    print("\n Following are the operations in Stack...")
    print("Press [1]-------> To create Stack")
    print("Press [2]-------> To Push data item.")
    print("Press [3]-------> To Pop data item.")
    print("Press [4]-------> To find out Top of the Stack Element.")
    print("Press [5]-------> To get length of stack.")
    print("Press [6]-------> To display stack.")
    p = int(input("Enter option: "))
    return p


if __name__ == "__main__":
    ss = Stack()
    loop = True
    while loop:
        o = 1
        choice = fun()
        if choice == 1:
            print("Implement Stack by entering  data...")
            while o:
                ss.push(int(input("\n Enter data: ")))
                o = int(input("Push data again or not [1/0] : "))
            print(ss.display(), "<----TOS")
        elif choice == 2:
            while o:
                ss.push(int(input("\n Enter data: ")))
                o = int(input("Push data again or not [1/0] : "))
            print(ss.display(), "<----TOS")
        elif choice == 3:
            while o:
                print(ss.pop(), " is popped from Stack")
                o = int(input("Pop again or not [1/0] : "))
            print(ss.display(), "<----TOS")
        elif choice == 4:
            print("Top of Stack is: ", ss.tos())
            print(ss.display(), "<----TOS")
        elif choice == 5:
            print("Length of Stack is: ", ss.length())
            print(ss.display(), "<----TOS")
        elif choice == 6:
            print(ss.display(), "<----TOS")
        else:
            loop = False
"""

# Assignment 1                              Merge list      Done

"""
def merge_list(list1, list2):
    merged_data = ""
    s = ""
    for i in range(len(list1)):
        if list1[i] is None:
            list1.pop(i)
            list1.insert(i, "")

    for i in range(len(list2)):
        if list2[i] is None:
            list2.pop(i)
            list2.insert(i, "")

    # write your logic here
    list2.reverse()
    for i in range(len(list1)):
        s = s + str(list1[i])
        s = s + str(list2[i])
        s = s + " "
    resultant_data = s
    return resultant_data


# Provide different values for the variables and test your program
list1 = ['A', 'app', 'a', 'd', 'ke', 'th', 'doc', 'awa']
list2 = ['y', 'tor', 'e', 'eps', 'ay', None, 'le', 'n']
merged_data = merge_list(list1, list2)
print(merged_data)
"""

# Assignment 2                              Car List        Done

"""
class Car:
    def __init__(self, model, year, registration_number):
        self.__model = model
        self.__year = year
        self.__registration_number = registration_number

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_registration_number(self):
        return self.__registration_number

    def __str__(self):
        return self.__model + " " + self.__registration_number + " " + str(self.__year)


# Implement Service class here

class Service:
    def __init__(self, car_list):
        self._car_list = car_list

    def find_cars_by_year(self, year):
        for i in self._car_list:
            if i.get_year() == year:
                print(i.get_model(), " ", i.get_year())

    def add_cars(self, new_car_list):
        # self._car_list.sort(key=lambda x: x.get_year(), reverse=False)
        for i in range(len(new_car_list)):
            self._car_list.append(new_car_list[i])

        for car in self._car_list:
            print(car.get_model(), "\t", car.get_year())

    def remove_cars_from_karnataka(self):
        for car in car_list:
            regno = str(car.get_registration_number())
            if regno[0:2] == "KA":
                self._car_list.remove(car)
        for car in self._car_list:
            print(car.get_model(), "\t", car.get_year(), "\t", car.get_registration_number())


car1 = Car("WagonR", 2010, "KA09 3056")
car2 = Car("Beat", 2011, "MH10 6776")
car3 = Car("Ritz", 2013, "KA12 9098")
car4 = Car("Polo", 2013, "GJ01 7854")
car5 = Car("Amaze", 2014, "KL07 4332")
car6 = Car("Breeza", 2019, "KL20 4332")
car7 = Car("Verna", 2020, "KA31 4332")
# Add different values to the list and test the program
car_list = [car1, car2, car3, car4, car5]
# Create object of Service class, invoke the methods and test your program
ss = Service(car_list)

ss.find_cars_by_year(2013)
ss.add_cars([car6, car7])
ss.remove_cars_from_karnataka()
"""

# Assignment 3                              check Doubles   Done

"""
def check_double(list1, list2):
    new_list = []
    # write your logic here
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] * 2 == list2[j]:
                new_list.append(list1[i])
    return new_list


# Provide different values for the variables and test your program
list1 = [11, 8, 23, 7, 25, 15]
list2 = [6, 33, 50, 31, 46, 78, 16, 34]
print(check_double(list1, list2))
"""

# Assignment 4                             Cricket Players  Done

"""
class Player:
    def __init__(self, name, experience):
        self.__name = name
        self.__experience = experience

    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def __str__(self):
        return self.__name + " " + str(self.__experience)


# Implement Game class here

class Game:
    def __init__(self, player_list):
        self.__player_list = player_list

    def sort_players_based_on_experience(self):
        return self.__player_list.sort(key=lambda x: x.get_experience(), reverse=True)

    def shift_player_to_new_position(self, old_index, new_index):
        plyer = self.__player_list.pop(old_index)
        self.__player_list.insert(new_index, plyer)

    def display(self):
        for i in self.__player_list:
            print(i)


player1 = Player("Dhoni", 15)
player2 = Player("Virat", 10)
player3 = Player("Rohit", 12)
player4 = Player("Raina", 11)
player5 = Player("Jadeja", 13)
player6 = Player("Ishant", 9)
player7 = Player("Shikhar", 8)
player8 = Player("Axar", 7.5)
player9 = Player("Ashwin", 6)
player10 = Player("Stuart", 7)
player11 = Player("Bhuvneshwar", 5)
# Add different values to the list and test the program
players_list = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11]
# Create object of Game class, invoke the methods and test your program
gg = Game(players_list)
gg.display()
print("\n")
print(gg.sort_players_based_on_experience())
gg.shift_player_to_new_position(7, 3)
gg.display()
"""

# Sentence problem linked list (remove * or /)              Done

"""
# lex_auth_0127438603766333441613

class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if data_before is None:
            new_node.set_next(self.__head)
            self.__head = new_node
            if new_node.get_next() is None:
                self.__tail = new_node

        else:
            node_before = self.find_node(data_before)
            if node_before is not None:
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if new_node.get_next() is None:
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        node = self.find_node(data)
        if node is not None:
            if node == self.__head:
                if self.__head == self.__tail:
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while temp is not None:
                    if temp.get_next() == node:
                        temp.set_next(node.get_next())
                        if node == self.__tail:
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print(data, "is not present in Linked list")

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = "".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


def create_new_sentence(word_list):
    new_sentence = ""
    # Write your logic here

    d = " "
    list1 = []
    i = word_list.get_head()
    while i:
        if i.get_data() == "*" or i.get_data() == "/":
            i.set_data(d)
        list1.append((i.get_data()))
        i = i.get_next()
    return word_list


word_list = LinkedList()
word_list.add("T")
word_list.add("h")
word_list.add("e")
word_list.add("/")
word_list.add("*")
word_list.add("s")
word_list.add("k")
word_list.add("y")
word_list.add("*")
word_list.add("i")
word_list.add("s")
word_list.add("/")
word_list.add("/")
word_list.add("b")
word_list.add("l")
word_list.add("u")
word_list.add("e")
result = create_new_sentence(word_list)
print(result)
"""

# Sum at odd places in linked list problem                  Done

"""
# lex_auth_012742477906173952821
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if data_before is None:
            new_node.set_next(self.__head)
            self.__head = new_node
            if new_node.get_next() is None:
                self.__tail = new_node

        else:
            node_before = self.find_node(data_before)
            if node_before is not None:
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if new_node.get_next() is None:
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if data == temp.get_data():
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        node = self.find_node(data)
        if node is not None:
            if node == self.__head:
                if self.__head == self.__tail:
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while temp is not None:
                    if temp.get_next() == node:
                        temp.set_next(node.get_next())
                        if node == self.__tail:
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print(data, "is not present in Linked list")

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


def find_sum(number_list):
    sum1 = 0
    # Write your logic here
    count = 0
    i = number_list.get_head()
    while i:
        count += 1
        print(i.get_data())

        if count % 2 != 0:
            sum1 = sum1 + i.get_data()
        i = i.get_next()
    return sum1


number_list = LinkedList()
number_list.add(10)
number_list.add(20)
number_list.add(30)
number_list.add(40)
number_list.add(50)
number_list.add(60)
number_list.add(70)
number_list.add(80)
number_list.add(90)
number_list.add(100)
number_list.add(110)

print(find_sum(number_list))

"""

# Max number replacement linked list problem                Done

"""
# lex_auth_012742480559513600853
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if data_before is None:
            new_node.set_next(self.__head)
            self.__head = new_node
            if new_node.get_next() is None:
                self.__tail = new_node

        else:
            node_before = self.find_node(data_before)
            if node_before is not None:
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if new_node.get_next() is None:
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        node = self.find_node(data)
        if node is not None:
            if node == self.__head:
                if self.__head == self.__tail:
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while temp is not None:
                    if temp.get_next() == node:
                        temp.set_next(node.get_next())
                        if node == self.__tail:
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print(data, "is not present in Linked list")

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


def replace_maximum(number_list, new_value):
    i = number_list.get_head()
    list1 = []
    while i:
        list1.append(i.get_data())
        i = i.get_next()
    m = max(list1)
    i = number_list.get_head()
    while i:

        if i.get_data() == m:
            i.set_data(new_value)
        i = i.get_next()

    return number_list


# Add different values to the linked list and test your program
number_list = LinkedList()
number_list.add(12)
number_list.add(95)
number_list.add(140)
number_list.add(110)
number_list.add(40)

new_value = 100
number_list = replace_maximum(number_list, new_value)
number_list.display()
"""

# Add new circle problem
"""
# lex_auth_012742507648933888867
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def set_head(self, head):
        self.__head = head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if (self.__head is None):
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if (data_before == None):
            new_node.set_next(self.__head)
            self.__head = new_node
            if (new_node.get_next() == None):
                self.__tail = new_node

        else:
            node_before = self.find_node(data_before)
            if (node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if (new_node.get_next() is None):
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while (temp is not None):
            if (temp.get_data() == data):
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        node = self.find_node(data)
        if (node is not None):
            if (node == self.__head):
                if (self.__head == self.__tail):
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while (temp is not None):
                    if (temp.get_next() == node):
                        temp.set_next(node.get_next())
                        if (node == self.__tail):
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print(data, "is not present in Linked list")

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp = self.__head
        msg = []
        while (temp is not None):
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


class Circle:
    def __init__(self, color, radius):
        self.__color = color
        self.__radius = radius

    def __str__(self):
        return (self.__color + " " + str(self.__radius))

    def get_color(self):
        return self.__color

    def get_radius(self):
        return self.__radius


class Shape:
    def __init__(self, circle_list):
        self.__circle_list = circle_list

        # Write your logic here

    def get_circle_list(self):
        circle_list.display()

    def insert_circle(self, new_circle):
        i = circle_list.get_head()
        
        node = Node(new_circle)
        circle_list.set_head(node)


circle1 = Circle("Red", 4)
circle2 = Circle("Green", 5)
circle3 = Circle("Purple", 3.5)
new_circle = Circle("Blue", 6)

circle_list = LinkedList()
circle_list.add(circle1)
circle_list.add(circle2)
circle_list.add(circle3)

shape = Shape(circle_list)
shape.insert_circle(new_circle)
shape.get_circle_list()
"""


# The Montessari Public School  Cultural event              Partially done
"""
# lex_auth_0127438667235000321614

class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if (self.__head is None):
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if (data_before == None):
            new_node.set_next(self.__head)
            self.__head = new_node
            if (new_node.get_next() == None):
                self.__tail = new_node

        else:
            node_before = self.find_node(data_before)
            if (node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if (new_node.get_next() is None):
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while (temp is not None):
            if (temp.get_data() == data):
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        node = self.find_node(data)
        if (node is not None):
            if (node == self.__head):
                if (self.__head == self.__tail):
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while (temp is not None):
                    if (temp.get_next() == node):
                        temp.set_next(node.get_next())
                        if (node == self.__tail):
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print(data, "is not present in Linked list")

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp = self.__head
        msg = []
        while (temp is not None):
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


class Child:
    def __init__(self, name, item_to_perform):
        self.__name = name
        self.__item_to_perform = item_to_perform

    def __str__(self):
        return (self.__name + " " + self.__item_to_perform)

    def get_name(self):
        return self.__name

    def get_item_to_perform(self):
        return self.__item_to_perform


# Implement Performance class here
class Performance:
    def __init__(self, children_list):
        self.__children_list = children_list

    def get_children_list(self):
        i = children_list.get_head()
        while i:
            print(i.get_data().get_name(), "\t", i.get_data().get_item_to_perform())
            i = i.get_next()

    def change_position(self, child):
        temp = self.__children_list.get_head()
        temp1 = self.__children_list.get_head()

        while temp.get_next():
            temp1 = temp1.get_next()
            if temp.get_next().get_next():
                temp = temp.get_next().get_next()
        self.__children_list.delete(child)
        self.__children_list.insert(child, temp1.get_data())
        # display
        i = children_list.get_head()
        while i:
            print(i.get_data().get_name(), "\t", i.get_data().get_item_to_perform())
            i = i.get_next()
    

    def add_new_child(self, child):
        children_list.add(child)


child1 = Child("Rahul", "solo song")
child2 = Child("Sheema", "Dance")
child3 = Child("Gitu", "Plays Flute")
child4 = Child("Tarun", "Gymnastics")
child5 = Child("Tom", "MIME")

# Add different values to the list and test the program
children_list = LinkedList()
children_list.add(child1)
children_list.add(child2)
children_list.add(child3)
children_list.add(child4)
children_list.add(child5)
performance = Performance(children_list)
print("The order in which the children would perform:")
performance.get_children_list()
print()
print("After Rahul's performance, the schedule would change to:")
performance.change_position(child1)
print()
child6 = Child("Swetha", "Vote of Thanks")
print("After Swetha has joined, the schedule is:")
performance.add_new_child(child6)
performance.get_children_list()

            orignal_list = []
            event_list = []
            i = children_list.get_head()
            while i:
                orignal_list.append(i.get_data().get_name())
                event_list.append(i.get_data().get_item_to_perform())
                i = i.get_next()
    
            i = children_list.get_head()
            count = 0
            while i:
                count += 1
                i = i.get_next()
    
            rep1 = orignal_list[count // 2]
            rep2 = event_list[count // 2]
            orignal_list[count // 2] = orignal_list[0]
            event_list[count // 2] = event_list[0]
            orignal_list[0] = rep1
            event_list[0] = rep2
            
"""

# Removing Duplicate number                             if condition error
"""
# lex_auth_0127438760987525121618

class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if data_before is None:
            new_node.set_next(self.__head)
            self.__head = new_node
            if new_node.get_next() is None:
                self.__tail = new_node

        else:
            node_before = self.find_node(data_before)
            if node_before is not None:
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if new_node.get_next() is None:
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        node = self.find_node(data)
        if node is not None:
            if node == self.__head:
                if self.__head == self.__tail:
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while temp is not None:
                    if temp.get_next() == node:
                        temp.set_next(node.get_next())
                        if node == self.__tail:
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print(data, "is not present in Linked list")

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg

    def remove_duplicates(self, duplicate_list):
        # write your logic here
        data_list = []

        i = self.__head
        while i:
            print(i.get_data(),"\t", i.get_next().get_data())
            print()
            if i.get_data() == i.get_next().get_data():
                duplicate_list.delete(i.get_next().get_data())
            i = i.get_next()

        return duplicate_list


# Add different values to the linked list and test your program
duplicate_list = LinkedList()
duplicate_list.add(30)
duplicate_list.add(40)
duplicate_list.add(40)
duplicate_list.add(40)
duplicate_list.add(40)

print(duplicate_list.remove_duplicates(duplicate_list))
"""

# BakeHouse Caff Problem
"""
# lex_auth_0127438800232038401622


class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if data_before is None:
            new_node.set_next(self.__head)
            self.__head = new_node
            if new_node.get_next() is None:
                self.__tail = new_node

        else:
            node_before = self.find_node(data_before)
            if node_before is not None:
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if new_node.get_next() is None:
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        node = self.find_node(data)
        if node is not None:
            if node == self.__head:
                if self.__head == self.__tail:
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while temp is not None:
                    if temp.get_next() == node:
                        temp.set_next(node.get_next())
                        if node == self.__tail:
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print(data, "is not present in Linked list")

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


table = 0


class BakeHouse:
    def __init__(self):
        self.__occupied_table_list = LinkedList()

    # Implement other methods here

    def get_occupied_table_list(self):
        i = self.__occupied_table_list.get_head()
        if i.get_next() is None:
            print("No Table allocated")
            return

        while i:
            print(i.get_data())
            i = i.get_next()

    def allocate_table(self):
        pass

    def deallocate_table(self, table_number):
        pass


bakehouse = BakeHouse()
bakehouse.get_occupied_table_list()
# Invoke the methods of BakeHouse class and test the program
"""
