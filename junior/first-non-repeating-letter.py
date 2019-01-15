'''
'stress' - 't'
'sTreSS' - 'T'
'''

from collections import Counter
def first_non_repeating_letter(string):
    new_string = string.lower()
    cnt = Counter(new_string)
    for letter in new_string:
        if cnt[letter] == 1:
            for i in [i for i,x in enumerate(new_string) if x == letter]: # i is a position non-repeating letter in the new string
                return string[i] # non-repeating letter in the initial string
    return ''

print("---Beteer-Solution---")
'''
def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]
            
    return ""
'''
'''
from collections import Counter
def first_non_repeating_letter(string):
    cnt = Counter(string.lower())
    for letter in string:
        if cnt[letter.lower()] == 1:
            return letter
    return ''
'''
