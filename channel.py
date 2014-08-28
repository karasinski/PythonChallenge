# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 12:23:18 2013

@author: Johnny
"""

import re, zipfile
 
inFile = zipfile.ZipFile('channel.zip')
num= '90052'
end = '.txt'
cmt = ''
while True:
    try:
        text = inFile.read(num + end).decode('utf-8')
    except:
        break
    comment = inFile.getinfo(num + end).comment
    cmt += comment.decode('utf-8')
    num = ''.join(re.findall('nothing is ([0-9]*)', text))
 
print (cmt)