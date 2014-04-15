skrypt CrKina.sh:
 - zasysa indeks (a-Z.html)
 - z indeksu zasysa listę stron do ściągnięcia (linki.txt)
 - ściąga strony kin i zapisuje je do plików tmp/i, i = 1,2,3.., wraz z adresem, z którego były zassane
 - a następnie odpala pajtonowego WSKina.py, który scrapuje wszystkie pliki i zapisuje w formacie xmlowym do pliku informacje.xml:
    <item>
        <title></title>
        <category></category>
        <city></city>
        <content></content>
        <url></url>
    </item>

np. 
<item>
<title>
Forum
</title> 
 <category>
Kino lokalne
</category> 
 <city>
 Bolesławiec
</city>
<content>
ul. Piłsudskiego 1c
59-700 Bolesławiec
                                            
Osoba do kontaktu: 
Iwona Bojko
                                            
Telefon:
(75) 644 55 93
                                            
Email: 
impresariat@bok.boleslawiec.pl
                                            
Strona WWW: 
www.kino.boleslawiec.pl 

                    
Data przystąpienia: 
2007-03-19

                    
Kino cyfrowe: 
Tak

                                            
Kategoria: 
A
                    
Programy edukacyjne: 
Tak



</content> 
 <url>
http://www.kinastudyjne.pl/kina/info/3945/forum.html
</url>
</item>
