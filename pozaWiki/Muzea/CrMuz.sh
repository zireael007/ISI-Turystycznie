#!/bin/bash
mkdir tmp
cd tmp
wget http:\/\/www.nimoz.pl\/pl\/bazy-danych\/wykaz-muzeow-w-polsce\/baza-muzeow-w-polsce
mkdir tmptmp
cd ..
cat tmp/baza-muzeow-w-polsce | grep 'page=' | sed 's/<a.*href="/http:\/\/www.nimoz.pl\//' | sed 's/".*>//' | tr -s '\t' | sort -u > linki.txt
cd tmp/tmptmp
cp ../../linki.txt linki.txt
wget -i linki.txt
cat * | grep 'baza-muzeow-w-polsce?' | sed 's/<a.*href="/http:\/\/www.nimoz.pl\//' | sed 's/".*>//' | tr -s '\t' | sort -u > ../../linki.txt
cd ..
wget -i ../linki.txt
rm tmptmp -r
rm baza-muzeow-w-polsce
cat * | python ../WSMuz.py | tr -s "\n" > ../informacje.xml
