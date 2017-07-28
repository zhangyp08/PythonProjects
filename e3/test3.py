#!/usr/bin/python
# encoding:utf-8


def test3():
    l=[]
    for i in range(10):
        if i%2 == 0:
            for j in range(5):
                if j%2 == 0:
                    l.append((i*2, j))
    return l

l=test3()
print l