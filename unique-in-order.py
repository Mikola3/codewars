def unique_in_order(iterable):
    array = []
    new_array = []
    for i in iterable:
        array.append(i)
    new_array.append(array[0])
    for x, y in zip(array, array[1:]):
        if x != y:
            new_array.append(y)
    return new_array

print(unique_in_order('AAAABBBCCDAABBB'))
#print(unique_in_order([1,2,2,3,3]))
