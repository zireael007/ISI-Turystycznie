var bot = require('nodemw');
var fs = require('fs');
var _ = require('lodash');

var client = new bot({
	"server": "pl.wikivoyage.org",	//host name of MediaWIki
	"path": "/w",					//path to api.php
	"debug": false
});


var numberOfPages = 0;
var allLinks = [];

fs.writeFile('wikiVoyageLinks', '', function(){console.log('Zawartośc pliku links została usunieta')});

var writeToFile = function(dataName, data, cb) {
	//write links to file
	if (!_.isEmpty(data)) {
		data = _.filter(data, function(item) {
			return item.indexOf('Kategoria') == -1;
		});
		var oldLinks = _.clone(allLinks);
		allLinks = _.union(allLinks, data);
		var diff = _.difference(allLinks, oldLinks);
		if (!_.isEmpty(diff)) {
			fs.appendFile('wikiVoyageLinks', diff.join('\n') + '\n', function(err) {
	    		if(err) {
		        	console.log(err);
    			} else {
        			console.log(dataName + " gotowe!!!");
        			console.log('Liczba artykułów ' + (numberOfPages++) +'.');
        			console.log('Zapisano ' + (allLinks.length) +' linków.\n');
        			if (cb) {
        				cb();
        			}
    			}
			}); 
		}
	}
};

var getArticleLinks = function (articleName, deepStep) {
	client.getArticle(articleName, function(data){
		console.log('sciagam artykul ' + articleName);
	 	var links = data.match(reg);
	 	links.push(articleName);
	 	for (var link in links) {
	 		if (deepStep != 0) {
	 			getArticleLinks(links[link].slice(2).slice(0,-2).replace(/\s/g, "_"), deepStep - 1);
	 		}
	 		links[link] = 'http://pl.wikivoyage.org/wiki/' + links[link].slice(2).slice(0,-2).replace(/\s/g, "_");
	 	}
	 	links = _.uniq(links);
	 	writeToFile('akrtykuł:'+ articleName, links.sort(), function () {
	 		console.log(articleName + ' - ' + links.length);
	 	});
	});
};

var reg = /\[{2,2}(\w|[ąśłńęóÓżźćĄĘŃŻŹĆŁŚ]|\s)+\]{2,2}/g


//artykuly dla analizy
var articles = 
	[{
		article: 'Polska',
		deepStep: 3,
	}];

for (var elem in articles) {
	getArticleLinks(articles[elem].article.replace(/\s/g, "_"), articles[elem].deepStep);
}