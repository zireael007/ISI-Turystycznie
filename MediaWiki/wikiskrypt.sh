#!/bin/bash

mkdir htmls
cd htmls

aria2c -i ../wikilinks -j5

#$i=1
#for link in $(head -n100 ../wikilinks)
#do
#    wget "$link" -O $i
#    echo $link >> $i
#    i=`expr $i + 1`
#done

cd ..
mkdir xmls
cd xmls
cat ../htmls/* | python ../wikiscrap.py | tr -s "\n" > wiki.xml
