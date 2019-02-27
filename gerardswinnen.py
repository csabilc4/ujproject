#!/usr/bin/env python
# coding=utf-8





exit()

#10.37.
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

t2 = []

for i, month in enumerate(t1):
    t2.append(str(t1[i]))

print ", ".join(t2)

cities = ["Albuquerque", "Anaheim", "Anchorage", "Arlington", "Atlanta"]
crime_rates = [749, 371, 828, 503, 1379]
cities_slice = cities[1:4]
cr_slice = crime_rates[-2:]

print cities_slice
print cr_slice


exit()
#10.36.
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Január', 'Február', 'Március', 'Április', 'Május', 'Június', 
        'Július', 'Augusztus', 'Szeptember', 'Október', 'November', 'December']

t3 = []
# t3.append('0')

for i, month in enumerate(t1):
    t3.append(t2[i])
    t3.append(str(t1[i]))

print ", ".join(t3)

exit()