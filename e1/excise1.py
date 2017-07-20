#!/usr/bin/python
# encoding:utf-8

'''
Created on 2017/7/1
@author: Yuping
'''

def feb(n):  # simple feblaci function
    f=[1]*n
    if (n>1):
        f[1] = 1
        for i in range(2,n,1):
            f[i]=f[i-1] + f[i-2]
    else:
        print "The number is smaller than 1."

    print f


def feb_tri(l,n):           # Gengerate feb list
    l_new=[1]*n
    l.append(l_new)
    middle_num=n/2                   #middle_num
    for i in range(0,middle_num,1):
        l[n-1][i+1]=l[n-2][i]+l[n-2][i+1] #中间以前的部分为上面的数字之和

    a=n-1
    b=0
    while a>middle_num:         #中间以后的数字等于对应前面的数值
        l[n-1][a]=l[n-1][b]
        a=a-1
        b=b+1
    mod=n%2
    if (mod!=1):
        l[n-1][middle_num]=l[n-2][middle_num-1]+l[n-2][middle_num] # 如果为基数，中间还需要再做一次



def print_triangle(l,n): #print function
    mod=n%2
    middle_num=n/2
    max_length=0
    if mod==0:                      #Get the largest number size
        #print "n is even number"
        max_length=len(str(l[n-1][middle_num]))
        #print "Large length is: ", length
    else:
        #print "n is odd number"
        max_length = len(str(l[n-1][middle_num+1]))
        #print "Large length is: ", length

    j = n
    i=0
    for i in range(n):                      #print, 如果最大的数值的长度为5，那么不足5位的会用空格代替
        if j > 0:
            print "*" * j* (max_length-1),
            for m in range(0, i + 1, 1):
                num_len=len(str(l[i][m]))
                space_before=(max_length-num_len)/2
                print "*"*space_before,
                print l[i][m],
                space_after=max_length-num_len-space_before
                print "*"*space_after,
            print ""
        j = j - 1




