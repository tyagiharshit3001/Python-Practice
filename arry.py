def update_mark_list(mark_list, pos, new_element):
    mark_list.insert(pos, new_element)
    return mark_list


def find_mark(mark_list, pos1, pos2):
    a = mark_list[pos1]
    b = mark_list[pos2]
    return a, b


mark_list = [89, 78, 99, 76, 77, 72, 88, 99]
new_element = 69
pos = 2
pos1 = 5
pos2 = 8
print(update_mark_list(mark_list, pos, new_element))
print(find_mark(mark_list, pos1, pos2))



