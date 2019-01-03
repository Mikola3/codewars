def getCount(inputStr):
    num_vowels = 0
    vowels = ["a", "e", "i", "o", "u"]
    for letter in inputStr:
        if letter in vowels:
            num_vowels += 1
    return num_vowels

'''
print(getCount("abracadabra"))
print(getCount("kkk3"))
5
0
'''

print("---Beteer-Solution---")
'''
def getCount(inputStr):
    return sum(1 for letter in inputStr if letter in "aeiou")
'''
