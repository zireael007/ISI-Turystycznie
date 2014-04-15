#!/bin/bash
mkdir tmp
wget http:\/\/www.kinastudyjne.pl\/kina\/letter\/a-Z.html
cat a-Z.html | grep 'kina/info' | sed 's/ *<a class="more" href="/http:\/\/www.kinastudyjne.pl\//'| sed 's/">.*//'  | tr -s ' '> linki.txt

$i = 3

for link in $(cat linki.txt)
do
    touch tmp/$i
    wget "$link" -O tmp/$i
    echo $link >> tmp/$i
    i=`expr $i + 1`
done

#wget -i linki.txt  
cd tmp
cat * | python ../WSKina.py | tr -s "\n" > ../informacje.xml


