# -*- coding: utf-8 -*-

import re
import sys
import operator

i = 0

for a in sys.stdin:
    print "<item>"
    print "<title>"
    for a in  sys.stdin:
        nazwa = re.search(r'<h2>.*</h2>', a)
        if nazwa:  
            nazwaa = re.search(r'>.*<', nazwa.group())
            nazwa = re.search(r'[^>].*[^<]', nazwaa.group())
            print "Multikino " + nazwa.group()
            break

    print "</title> \n <category> Multikino </category> \n <city>"
    """znalezienie adresu"""
    
    for a in  sys.stdin:
        adres = re.search(r'.*[0-9]{2}-[0-9]{3}.*', a)
        if adres:
            miasto = re.search(r'[0-9] [^<]*', adres.group())
            miasto = re.search(r'[^0-9 ].*', miasto.group())
            print miasto.group() + "\n"
            break
    
    print "</city>\n<content>"
    if adres:
        print re.sub("<.*?>", "", adres.group())

    for a in  sys.stdin:
        koniec = re.search(r'<script.*', a)
        if not(koniec):
            if re.search(r'\w*', a):
                a = re.sub("<.*?>", "", a)
                print a
        else:
            break

    print "</content>  \n <url>"

    for a in  sys.stdin:
        adres = re.search(r'</html>', a)
        if adres:
            for a in sys.stdin:
                print a
                break
            break
    print "</url> \n </item>"
