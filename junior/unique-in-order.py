'''
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
'''

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

print("---Beteer-Solution---")
'''
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
'''
