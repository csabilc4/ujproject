#!/usr/bin/env python
# coding=utf-8

# Problem 162
# hány olyan hexadecimális szám létezik, amelyik legfeljebb 16 hexa számjegyet tartalmaz
#
#
#

movies = [('a', 1987),
		  ('b', 1526),
		  ('c', 2019),
		  ('d', 1907),
		  ('e', 2437),
		  ('f', 1944),
		  ('g', 2037)]

gmovies = []
for title in movies:
    pass
    # print title
    # if year < 2000:
    #     pass
        # gmovies.append((title, year))
dmovies = {title: year for (title, year) in movies if year > 0 and title != ''}


print dmovies

# a, b = dmovies.items()

for c in dmovies.items():
    pass
    # print c, type(c)





exit()
# Problem 30
fact = 5
max_num = 200000
fsum = 0
for num in range(2, max_num + 1):
    num_string = str(num)

    sum = 0
    for s in num_string:
        sum = sum + int(s) ** fact
        if sum > num:
            break

    if sum == num:
        print num
        fsum = fsum + num

print "sum = %d" % fsum
    # mod_100 = num % 10
    # print num - mod_100, mod_100