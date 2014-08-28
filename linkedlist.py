# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 01:10:53 2013

@author: Johnny
"""

# Let's grab the source of the page.
import urllib.request
def get_challenge(s):
    return urllib.request.urlopen('http://www.pythonchallenge.com/pc/' + s).read()

mess = get_challenge('def/linkedlist.php')

num = 12345
count = 0
for x in range(1, 400):
    oldnum = num
    mess = get_challenge('def/linkedlist.php?nothing=' + str(num))
    m = str( mess, encoding='utf8' )
    num = [int(s) for s in m.split() if s.isdigit()]
    if len(num) >= 1:
        num = num[0]
    elif (count == 0):
        num = oldnum/2
        count = count + 1
    else:
        print (mess)
        break
    
    print (x, num)
