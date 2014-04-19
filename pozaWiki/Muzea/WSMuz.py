# -*- coding: utf-8 -*-

import re
import sys
import operator

for a in sys.stdin:
    obiekt = re.search(r'<strong class="red">', a)
    if obiekt:
        print "<item>"
        print "<title>"
        nazwa = re.sub("<.*?>", "\n", a)
        print nazwa
        print "</title> \n <category>"
        print "Muzeum"
        print "</category> \n"
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
            
        print "<city>" + miasto + "</city> \n"
        print "<content>" + info + "</content>    \n </item>\n"




