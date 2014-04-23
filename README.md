ISI-Turystycznie
================

Wyszukiwarka turystyczna

Web interface is available at http://54.186.183.152:8080/.

##Download links from Wikipedia and Wikivoyage

###Requirements:
 * nodejs

###Dependencies:
 * [lodash](https://github.com/lodash/lodash)
 * [nodemw](https://github.com/macbre/nodemw)

###Instalation

To install nodejs:
```bash  
  sudo apt-get install nodejs
```

To install nodemw and lodash:
```bash
  cd MediaWiki
  npm install nodemw
  nom install lodash
```
###How to use:

To download the links from wikipedia:
```bash
  node getWikiArticlesLinks.js
```

To download the links from wikivoyage:
```bash
  node getWikiVoyageArticlesLinks.js
```
