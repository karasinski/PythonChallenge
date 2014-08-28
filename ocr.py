# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 00:27:37 2013

@author: Johnny
"""

# Let's grab the source of the page.
import urllib.request
def get_challenge(s):
    return urllib.request.urlopen('http://www.pythonchallenge.com/pc/' + s).read()

mess = get_challenge('def/ocr.html')

# Let's properly encode it and grab the part we care about.
m = str( mess, encoding='utf8' )
s1 = m.split('<!--')
s2 = s1[2].split('-->')
mess = s2[0]

# Let's find rare characters
dict = {}
for ch in mess:
    dict[ch] = dict.get(ch, 0) + 1

# Let's print rare characters
print ("".join(ch for ch in mess if dict[ch] == 1))
