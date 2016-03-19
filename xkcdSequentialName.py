#!/usr/bin/env python3

import requests,sys,re
from bs4 import BeautifulSoup
import time
from datetime import datetime
from urllib.request import urlopen
now = time.time()
import string

print('downloading xkcd comics ..')
print("time started: ",datetime.now())

for i in range(1,1658):
    # 404: not found and 1525 is not an image
    if i in [404,1525]:
        continue
    else:
        res = requests.get('http://xkcd.com/'+str(i)+'/')
    soup = BeautifulSoup(res.text)
    imageToken = soup.find_all('img')

    """
    name = (imageToken[1].get('alt'))
    if name==None:
        name = ''.join(['dude',str(i)])
    """
    raw = imageToken[1].get('src')
    raw = raw.strip('/')
    extension = raw.split('.')
    extension = extension[-1]

    """
    if 'style' in name:
        pat = re.compile(r'>(.*)</span>(.*)')
        sp = list(pat.search(name).groups())
        
    else:
        if '/' in name:
            sp = name.split('/')
        else:
            sp = name.split()

    name = "".join(str(x) for x in sp if x not in string.punctuation)
    """
    
    filename = ''.join(['comic',str(i),'.',extension])
    
 
    pic_url ='http://'+raw
    pic = requests.get(pic_url,stream=True)

    with open(filename, 'wb') as fd:
        for chunk in pic.iter_content(1024):
            fd.write(chunk)
            
    #with open(filename, "wb" ) as f:
    #    f.write(pic)

    print(''.join(['download completed ','xkcd comics ',str(i)]))

then = time.time()
print("time finished: ",datetime.now())
print("total time taken: ",then-now)
