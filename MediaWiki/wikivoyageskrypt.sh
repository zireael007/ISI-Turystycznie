#!/bin/bash

rm -R htmls
mkdir htmls
cd htmls

aria2c -i ../wikiVoyageLinks -j5

$i=1
for link in $(head -n2499 ../wikiVoyageLinks)
do
   wget "$link" -O $i
   echo $link >> $i
   i=`expr $i + 1`
done

cd ..
rm -R xmls
mkdir xmls
cd xmls
cat ../htmls/* | python ../wikiscrap.py | tr -s "\n" > wiki.xml
