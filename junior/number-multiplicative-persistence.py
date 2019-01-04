'''
persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.
 '''
 
def get_digits(num):
    digits = [int(n) for n in str(num)]
    return digits

#print(get_digits(39)) == [3, 9]

def multiply_all(digits):
    multiplier = 1
    for i in digits:
        multiplier *= i
    return multiplier

#print(multiply_all([3, 9])) == 27

def persistence(num):
    count = 0
    while num >= 10:
        num = multiply_all(get_digits(num))
        count += 1
    return count

#print(persistence(39)) == 3


print("----Better-Solusion------")
'''
def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count
'''
'''
import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i
#print(operator.mul(3,9)) == 27
#reduce (function, iterable [, initializer])
#functools.reduce(operator.mul, [1, 2, 3], 1) == 6
#functools.reduce(operator.mul, [], 1) == 1
'''
'''
def persistence(n):
    nums = [int(x) for x in str(n)]
    sist = 0
    while len(nums) > 1:
        newNum = reduce(lambda x, y: x * y, nums)
        nums = [int(x) for x in str(newNum)]
        sist = sist + 1
    return sist
'''
