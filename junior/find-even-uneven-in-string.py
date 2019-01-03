def even(numbers, bit):
    array = numbers.split()
    for i in range(len(array)):
        if int(array[i]) % 2 == bit:
            return i+1

def iq_test(numbers):
    a = 0
    array = numbers.split()
    for i in array[:3]:
        if int(i) % 2 == 1:
            a += 1
    if a > 1:
        return even(numbers, 0)
    else:
        return even(numbers, 1)

'''
Find position uneven (even) item in the even (uneven) string
print(iq_test("4 6 2 4 6 2 9")) == 7
print(iq_test("1 3 4 5 7")) == 3
'''
