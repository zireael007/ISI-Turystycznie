skrypt CrMuz.sh:
 - zasysa wszystkie zalinkowane strony ze spisem zabytków, a potem wszystkie w nich zalinkowane strony ze spisem zabytków - do linki.txt
 - ściąga strony
 - a następnie odpala pajtonowego WSKina.py, który scrapuje wszystkie pliki i zapisuje w formacie xmlowym do pliku informacje.xml:
    <item>
        <title></title>
        <category></category>
        <city></city>
        <content></content>
        #brak wysysania urla
    </item>
