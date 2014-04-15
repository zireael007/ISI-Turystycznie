# -*- coding: utf-8 -*-

import re
import sys
import operator

for a in sys.stdin:
    obiekt = re.search(r'<strong class="red">', a)
    if obiekt:
        print "<obiekt>"
        print "<nazwa>"
        nazwa = re.sub("<.*?>", "\n", a)
        print nazwa
        print "</nazwa> \n <kategoria>"
        print "Muzeum"
        print "</kategoria> \n"
        miasto = ""
        info = ""
        for a in sys.stdin:
            koniec = re.search(r'</tr>', a)
            if not(koniec):
                if re.search(r'.*kontakt:.*', a):
                    info = info + re.sub("<.*?>", "", a)
                    for a in sys.stdin:
                        miasto = re.sub("<.*?>", "", a)
                        info = info + miasto
                        break
                else:
                    info = info + re.sub("<.*?>", "", a)
            else:
                break
            
        print "<miasto>" + miasto + "</miasto> \n"
        print "<info>" + info + "</info>    s\n </obiekt>\n"




