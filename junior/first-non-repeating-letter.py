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
