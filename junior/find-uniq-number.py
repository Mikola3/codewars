'''
findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
'''

def find_uniq(arr):
    for x,y,z in zip(arr, arr[1:], arr[2:]):
        if x != y and y == z and x != z:
            return x
        elif x != y and y != z and x == z:
            return y
        elif x == y and y != z and x != z:
            return z

#print(find_uniq([ 1, 1, 1, 1, 0, 1 ]))
