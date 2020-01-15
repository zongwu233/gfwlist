#! /usr/bin/python
# -*- coding: UTF-8 -*-
import base64
import os


rawfile = "rawcontent.txt"
encodefile = "gfwlist.txt"
with open(rawfile) as f:
    content = f.read()
    encode = base64.b64encode(content)
    os.remove(encodefile)

    with open(encodefile,"w") as wf:
    	wf.write(encode)
    print('update success!')

os.system('git commit -a -m "update"')
os.system('git push')



