#! /usr/bin/python
# -*- coding: UTF-8 -*-
import base64

with open('gfwlist.txt') as f:
	content = f.read()
	raw = base64.b64decode(content)
	print(raw)
