# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 18:51:22 2018

@author: adity
"""

N = int(input())
final = list()
for i in range(N):
    lst = list()
    name = str(input())
    marks = float(input())
    lst.append(name)
    lst.append(marks)
    final.append(lst)
a = len(final)
#print (final)
#print (a)
k = list()
for i in range(len(final)):
    k.append(final[i][1])
#print (k)

x = min(k)
k1 = list()
for i in range(len(k)):
	if x != k[i]:
		k1.append(k[i])
y = min(k1)
#print (x)

student = list()
for i in range(len(final)):
    if y == final[i][1]:
        student.append(final[i][0])
student.sort()

for i in range(len(student)):
    print (student[i])