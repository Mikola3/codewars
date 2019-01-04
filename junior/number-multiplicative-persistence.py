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
