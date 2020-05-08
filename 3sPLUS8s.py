#Every natural number greater than 13 can be written as the sum of 3s and 8s
#this program does that

def main():
    while True:
        x = input('Enter a number greater than 13: ')
        x = int(x)
        if x < 14:
            print('Number must be greater than 13')
        else:
            break

    if isMultipleOf3(x):
        print('Is multiple of 3')
        decomp3(x)
    elif isMultipleOf8(x):
        print('Is multiple of 8')
        decomp8(x)
    else:
        print(x, 'is not multiple of 3 or 8')
        decomp(x)

    print()

def isMultipleOf3(x):
    r = x % 3
    isit = r == 0
    return isit

def isMultipleOf8(x):
    r = x % 8
    isit = r == 0
    return isit

def decomp3(x):
    i = 0
    while i != x:
        i += 3
        print('3', end = '')
        if i == x:
            break
        print('+', end = '')

def decomp8(x):
    i = 0
    while i != x:
        i += 8
        print('8', end = '')
        if i == x:
            break
        print('+', end = '')

def decomp(x):
    nums = []
    while listSum(nums)+8 <= x:
        nums.append(8)

    missing = x - listSum(nums)
    if isMultipleOf3(missing):
        decomp3(missing)
        printList(nums)
    else:
        nums[0] = 3
        i = 0
        while listSum(nums) != x:
            nums[0] += 3
            if listSum(nums) > x:
                nums.remove(8)
        decomp3(nums[0])
        printListFrom1(nums)

def listSum(l):
    i = 0
    j = 0
    lastI = len(l)-1
    while i < lastI:
        j += l[i]
        i += 1
    return j

def printList(l):
    i = 0
    lastI = len(l)-1
    while i < lastI:
        print('+', end = '')
        print(l[i], end = '')
        i += 1

def printListFrom1(l):
    i = 1
    lastI = len(l)-1
    while i < lastI:
        print('+', end = '')
        print(l[i], end = '')
        i += 1

main()
