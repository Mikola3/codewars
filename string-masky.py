'''
maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""
'''


def maskify(cc):
    array_new = list(cc)
    if len(array_new) < 4:
        return cc
    else:
        for i in range(len(array_new)-4):
            array_new[i]="#"
        return ''.join([str(x) for x in array_new])

print("---Best-Solution---")
'''
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]
'''
