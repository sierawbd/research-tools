#!/bin/env python

import os, sys
import requests
import xml.etree.ElementTree as ET

def query_author(author):
    url="http://ieeexplore.ieee.org/gateway/ipsSearch.jsp?au=%s&hc=1000&sortfield=ti&sortorder=asc"%(author)
    headers = {"accept": "application/xml"}
    r = requests.get(url, headers = headers)
    return r.text

author = sys.argv[1]
root = ET.fromstring(query_author(author))
for child in root:
    for doi in child.findall('doi'):
        print doi.text


