# -*- coding: utf-8 -*-

import re
import sys
import operator

i = 0

for a in sys.stdin:
    print "<item>"
    print "<title>"
    for a in  sys.stdin:
        PreNazwa = re.search(r'.*<header>', a)
        if PreNazwa:
            for a in sys.stdin:
                nazwa = re.search(r'<h2>.+</h2>', a)
                if nazwa:  
                    nazwaa = re.search(r'>.*<', nazwa.group())
                    nazwa = re.search(r'[^>].*[^<]', nazwaa.group())
                    print nazwa.group()
                    break
            break

    print "</title> \n <category>"
    for a in  sys.stdin:
        kat = re.search(r'<p class="subheading">.*</p>', a)
        if kat:
            """        print nazwa.group()"""
            katt = re.search(r'>.*<', kat.group())
            katt = re.search(r'[^>].*[^<]', katt.group())
            print katt.group()
            break

    print "</category> \n <city>"
    """znalezienie adresu"""
    adres = ""
    miastozkodem = ""
    
    for a in  sys.stdin:
        kat = re.search(r'<dl class="entry-meta">', a)
        if kat:
            for a in sys.stdin:
                katt = re.search(r'>.*<', a)
                adres = re.search(r'[^>].*[^<]', katt.group())
                break
            break
    
    for a in  sys.stdin:
        miast = re.search(r'<dt>[0-9]{2}\-[0-9]{3}.*', a)
        if miast:
            miastoo = re.search(r'>.*<', miast.group())
            miastozkodem = re.sub(">", "", miastoo.group())
            miastozkodem = re.sub("<", "", miastozkodem)
            miasto = re.search(r'[^>0-9-].*[^<]', miastoo.group())
            if miasto:
                print miasto.group()
            break
    
    print "</city>\n<content>"
    if adres:
        print adres.group()
    print miastozkodem
    """
    for a in  sys.stdin:
        info = re.search(r'<dl class="entry-meta info"', a)
        if info:
            for a in sys.stdin:
                if re.search(r'</dl>',a):
                    break
                else:
                    linia = re.findall(r'[^<>]+', a)
                    znacznik = re.compile("[^<>]*span|[^<>]*href[^<>]*|/?dt|/?a")
                    for i in linia:
                        if not(znacznik.match(i)):
                            print i
            break
    """
    for a in  sys.stdin:
        poczatek = re.search(r'<dl class="entry-meta info"', a)
        if poczatek:
            for a in  sys.stdin:
                koniec = re.search(r'</dl.*', a)
                if not(koniec):
                    if re.search(r'\w*', a):
                        a = re.sub("<.*?>", "\n", a)
                        print a + "\n"
                else:
                    break
            break

    print "</content> \n <url>"

    for a in  sys.stdin:
        adres = re.search(r'</html>.*', a)
        if adres:
            print re.sub("</html>", "", adres.group())
            break
    print "</url>"

    print "\n</item>"
