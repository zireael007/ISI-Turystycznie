#!/bin/bash

mkdir tmp
wget http:\/\/multikino.pl/pl/wszystkie-kina
cat wszystkie-kina | egrep '/pl/wszystkie-kina/[^/]*/o-kinie' | sed -e 's/" >[^>]*>//g' | sed -e 's/<a href="/\n/g' | egrep 'o-kinie' > linki.txt

$i = 3

for link in $(cat linki.txt)
do
    touch tmp/$i
    wget "$link" -O tmp/$i
    echo $link >> tmp/$i
    i=`expr $i + 1`
done

cd tmp
cat * | python ../WSMulti.py > ../informacje.xml

