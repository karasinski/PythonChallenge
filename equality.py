# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 01:10:53 2013

@author: Johnny
"""

# Let's grab the source of the page.
import urllib.request
def get_challenge(s):
    return urllib.request.urlopen('http://www.pythonchallenge.com/pc/' + s).read()

mess = get_challenge('def/equality.html')

# Let's properly encode it and grab the part we care about.
m = str( mess, encoding='utf8' )
s1 = m.split('<!--')
s2 = s1[1].split('-->')
mess = s2[0].replace("\n","")

import re
print (''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', mess)))
