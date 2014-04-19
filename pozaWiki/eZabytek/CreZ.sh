#!/bin/bash
mkdir tmp
cd tmp

for i in `seq 1 300`            #poki co jest zabytkow do 209, wiec wystarczy seq 1 300. mozna sprobowac zautomatyzowac - np. na glownej odwoluja sie do ostatnio dodanych - wystarczy wyciagnac najwieksze n tze wystepuje Zabytek/szczegoly.php?ID=$n
do
    wget -t inf "http://e-zabytek.nid.pl/Zabytek/szczegoly.php?ID=$i" -O zabytek$i
    if cat zabytek$i | egrep '"og:title" content=".+"'; then
        echo "http://e-zabytek.nid.pl/Zabytek/szczegoly.php?ID=$i" >> zabytek$i
        cp  "zabytek$i" "zabytek$i"
    else 
        rm "zabytek$i"
    fi
done


cat * | python ../WSeZ.py | tr -s "\n" > ../informacje.xml
