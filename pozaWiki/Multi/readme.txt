skrypt CrMulti.sh:
 - zasysa indeks (wszystkie-kina)
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
