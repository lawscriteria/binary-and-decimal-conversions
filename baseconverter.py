import numpy as np

print("Input a number you want converted. Note that if there is ambiguity, meaning if your number can be both binary and decimal, you should indicate with an indicator (a letter at the end of your number, either d or b, specifying whether your number is a 'd'ecimal or 'b'inary). If there is no indicator at the end of the string provided, the number is assumed to be in binary.")

dig = [f'{d}' for d in range(10)]
def ambchecker(num_str, range_start):
    for j in num_str:
        if j in [
            f'{f}' for f in dig[
                (range_start):
                ]
        ]: return 0

    return 1

def baseconverter(num):
    indic = num[-1]
    if indic not in ['b', 'd'] and ambchecker(num, 2) or indic == 'b':
        return two2ten(num)
    
    return ten2two(num)
    

def ten2two(n):
    if n[-1] not in dig:
        n = n[:-1]

    for i in n:
        if i not in dig: return TypeError, "The number provided couldn't be recognized. Please try again."

    nint = int(n)
    if nint == 0:
        return 0
    
    l = int(np.log2(nint))
    b = [0]*(l+1)

    bint = 0
    for i in range(l+1):
        if nint < 1: break

        p = int(np.log2(nint))
        nint -= 2**p
        j = -p-1

        b[j] = 1
        bint += sign(n)*(10**p)*b[j]
    
    return bint


def two2ten(n):
    if n[-1] not in dig:
        n = n[:-1]

    for j in n:
        if j not in dig[:2]: return TypeError, "The number provided couldn't be recognized. Please try again."

    if n == '0':
        return 0

    l = len(n)
    bint = 0
    for i in range(l):
        bint += sign(n)*int(n[i])*(2**(l-(i+1)))

    return bint

def sign(arg):
    s = 1
    if arg[0] == '-':
        arg = arg[1:]
        s = -1
    return s
    
while True:
    userinput = input("What's your number? ")

    print(baseconverter(userinput))