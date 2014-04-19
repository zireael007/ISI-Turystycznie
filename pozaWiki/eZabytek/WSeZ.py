# -*- coding: utf-8 -*-

import re
import sys
import operator

i = 0

for a in sys.stdin:
    print "<item>"
    print "<title>"
    for a in  sys.stdin:
        nazwa = re.search(r'og:title" content=".*"', a)
        if nazwa:  
            nazwaa = re.search(r'=".*"', nazwa.group())
            nazwa = re.search(r'[^="].*[^"]', nazwaa.group())
            print nazwa.group()
            break

    print "</title> \n <category> Zabytek </category> \n <city>"
    miastooo = re.search(r'.*-', nazwa.group())    
    if miastooo:
        miasto = re.search(r'.*[^-]', miastooo.group())
        print miasto.group()
    else:
        miasto = nazwa.group()
        print miasto
    """    for a in  sys.stdin:
        adres = re.search(r'.*, woj\. .*', a)
        if adres:
            miasto = re.search(r'"[^"]*, woj\.', adres.group())
            miasto = re.search(r'[^"].*,', miasto.group())
            miasto = re.search(r'.*[^,]', miasto.group())
            print miasto.group()
            break"""
    
    print "</city>\n<content>"

    """for a in  sys.stdin:
        if re.search(r'Opis zabytku', a):
            for a in sys.stdin:
                koniec = re.search(r'</body>', a)
                if not(koniec):
                    print re.sub("<.*?>", "", a)
                else:
                    print "</content>  \n <url>"
                    break
            break"""
    """krotkie info"""
    for a in  sys.stdin:
        if re.search(r'<dl class="ls7">', a):
            for a in sys.stdin:
                koniec = re.search(r'Lokalizacja', a)
                if not(koniec):
                    print re.sub("<.*?>", "", a)
                else:
                    break
            break

    """opis"""
    for a in  sys.stdin:
        if re.search(r'<section>', a):
            for a in sys.stdin:
                koniecopisu = re.search(r'</section>', a)
                if not(koniecopisu):
                    print re.sub("<.*?>", "", a)
                else:
                    print "</content>\n"
                    break
            break
    print "<url>"
    for a in  sys.stdin:
        url = re.search(r'.*</html>http://e-zabytek.*', a)
        if url:
            print re.sub("<.*?>", "", a)
            print "</url> \n </item>"
            break
