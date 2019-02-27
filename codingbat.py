#!/usr/bin/env python
# coding=utf-8

# has22
def has22(nums):

    has2 = False
    previ = 0
    for num in nums:
        if num == 2:
            has2 = True

            # print num, previ
            if previ == 2:
                return True
        else:
            has2 = False

        previ = num
    return False

print has22([1, 2, 2])

ff = ["átijlkd"]
print ff

exit()
# sum67
def sum67(nums):
    sum = 0
    previ = 0
    exist6 = False

    for i, num in enumerate(nums):
        if num == 6: exist6 = True

        if num != 6 and exist6 is False:
            sum += num

        if num == 7: exist6 = False

    return sum


exit()
# sum13
def sum13(nums):

    sum = 0
    previ = 0
    for i in nums:
        if i != 13 and previ != 13:
            sum += i
        previ = i
    return sum


exit()
# centered_average
def centered_average(nums):
    mins = min(nums)
    maxs = max(nums)

    nums.remove(mins)
    nums.remove(maxs)

    sum = 0
    for i in nums:
        sum += i
    ave = sum / len(nums)
    return ave

exit()
# big_diff
def big_diff(nums):

    return max(nums) - min(nums)

    pass

exit()
# count_evens
def count_evens(nums):

    evens = 0
    for num in nums:
        if num % 2 == 0:
            evens += 1

    return evens


exit()
# xyz_there
def xyz_there (str):

    num = str.count('xyz')
    if num == 0: return False

    newStr = str
    for i in range(num):
        # str.index('x')


        if newStr[newStr.find('xyz') - 1] != ".":
            return True

        newStr = newStr[newStr.find('xyz') + 3:]
        # print newStr

        # if str[str.find('xyz') - 1] != ".":
        #     return True

        # if str.find('xyz') > 1:
        # if str[str.find('xyz') - 1] != ".":
        #     return True



    return False


print xyz_there('abcxyz')
print xyz_there('abc.xyz')
print xyz_there('xyz.abc')

exit()
# end_other
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    # print a, b

    if len(a) > len(b):
        if (b in a) and a[-len(b)] == b[0]:
            return True
    else:
        if (a in b) and b[-len(a)] == a[0]:
            return True

    return False


print end_other('Hiabc', 'abc')
print end_other('AbC', 'HiaBc')
print end_other('abc', 'abXabc')

exit()
# count_code
def count_code(str):
    f = 'co'
    num = 0
    newStr = ''
    for i, string in enumerate(str):
        newStr += string
        if f in newStr:
            if i < len(str) - 2 and str[i + 2] == 'e':
                num += 1
                newStr = ''
    return num


print count_code('aaacodebbb')
print count_code('codexxcode')
print count_code('cozexxcope')
print count_code('co')
print count_code('codecos')

exit()
# cat_dog
def cat_dog(str):
    cat = 'cat'
    dog = 'dog'

    if str.count(cat) == str.count(dog):
        return True
    return False

print cat_dog('catdog')

exit()
# count_hi
def count_hi(str):
    f = 'hi'

    num = 0
    newStr = ''
    for string in (str):
        newStr += string
        if f in newStr:
            print newStr, num, f
            num += 1
            newStr = ''
    return num

print count_hi('abc hi ho')


exit()
# double_char
def double_char(str):
    newStr = ''
    for string in str:
        newStr += string * 2

    return newStr

print double_char('The')


exit()
# make_chocolate
def make_chocolate(small, big, goal):
    sum = 0
    for i in range(0, big + 1):
        if i * 5 <= goal:
            sum = i * 5
        # print 'i=' + str(i), sum

    if goal - sum > small:
        return -1

    return goal - sum


print make_chocolate(4, 1, 9)
print
print make_chocolate(4, 1, 5)
print
print make_chocolate(4, 1, 10)
print
print make_chocolate(1, 2, 7)
print
print make_chocolate(4, 1, 7)
print
print make_chocolate(6, 1, 10)
print
print make_chocolate(60, 100, 550)

exit()
# round_sum
def round_sum(a, b, c):
    sum = 0
    for num in [a, b, c]:
        if num % 10 < 5:
            sum += (num - (num % 10))
        else:
            sum += (num - (num % 10)) + 10

    return sum

print round_sum(6, 4, 4)

exit()
# no_teen_sum
def no_teen_sum(a, b, c):
    sum = 0
    for num in [a, b, c]:
        if 13 <= num <= 19 and (num != 15 and num != 16):
            pass
        else:
            sum = sum + num

    return sum

print no_teen_sum(2, 1, 15)

exit()
# lucky_sum
def lucky_sum(a, b, c):
    sum = 0
    for num in [a, b, c]:
        if num != 13:
            sum = sum  + num
        else:
            break

    return sum

print lucky_sum(1, 2, 3)