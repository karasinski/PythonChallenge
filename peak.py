# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 01:10:53 2013

@author: Johnny
"""

# Let's grab the source of the page.
import urllib.request
def get_challenge(s):
    return urllib.request.urlopen('http://www.pythonchallenge.com/pc/' + s).read()

mess = get_challenge('def/banner.p')

import pickle
data = pickle.loads(mess)
print ('\n'.join([''.join([p[0] * p[1] for p in row]) for row in data]))
