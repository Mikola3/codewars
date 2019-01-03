import math
def get_middle(s):
    arr = []
    new_arr = []
    for char in s:
        arr.append(char)
    if len(arr) % 2 == 0:
        middle = int(len(arr)/2)
        new_arr.extend((arr[middle-1], arr[middle]))
        return ''.join(new_arr)
    else:
        middle = len(s)/2
        middle_modify = int(math.ceil(middle))
        return str(arr[middle_modify-1])

print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))
print(get_middle("of"))
