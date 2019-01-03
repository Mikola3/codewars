'''
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
'''

def narcissistic(value):
    summa = 0
    numbers = [int(num) for num in str(value)]
    lenth = len(numbers)
    for i in numbers:
        summa += i ** lenth
    if summa == value:
        return True
    else:
        return False

print("---Beteer-Solution---")
'''
def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))
'''
