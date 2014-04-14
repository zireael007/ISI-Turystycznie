var bot = require('nodemw');
var fs = require('fs');
var _ = require('lodash');

var client = new bot({
	"server": "pl.wikipedia.org",	//host name of MediaWIki
	"path": "/w",					//path to api.php
	"debug": false
});

var numberOfPages = 0;
var allLinks = [];

fs.writeFile('wikiLinks', '', function(){console.log('Zawartośc pliku links została usunieta')});

var writeToFile = function(dataName, data, cb) {
	//write links to file
	if (!_.isEmpty(data)) {
		data = _.filter(data, function(item) {
			return item.itemndexOf('Kategoria') == -1;
		});
		var oldLinks = _.clone(allLinks);
		allLinks = _.union(allLinks, data);
		var diff = _.difference(allLinks, oldLinks);
		if (!_.isEmpty(diff)) {
			fs.appendFile('wikiLinks', diff.join('\n') + '\n', function(err) {
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
	 		links[link] = 'http://pl.wikipedia.org/wiki/' + links[link].slice(2).slice(0,-2).replace(/\s/g, "_");
	 	}
	 	links = _.uniq(links);
	 	writeToFile('akrtykuł:'+ articleName, links.sort(), function () {
	 		console.log(articleName + ' - ' + links.length);
	 	});
	});
};

var getCategoryLinks = function (categoryName, deepStep) {
	client.getPagesInCategory(categoryName, function(data) {
		console.log('sciągam kategorie ' + categoryName);
		data = _.pluck(data, 'title');
		if (deepStep != 0) {
			_.each(data, function(val){
				if (val.match(/kategoria/gi)) {
					getCategoryLinks(val.replace(/\s/g, "_").slice(10), deepStep - 1);
				}	
			});
		}
		data = _.map(data, function (elem) {
			return 'http://pl.wikipedia.org/wiki/' + elem.replace(/\s/g, "_");
		});
		if (data.length != 0) {
				writeToFile('kategoria:' + categoryName, data, function() {
				console.log(categoryName + ' - ' + data.length);
			});
		}
	});	
};

var reg = /\[{2,2}(\w|[ąśłńęóÓżźćĄĘŃŻŹĆŁŚ]|\s)+\]{2,2}/g


//artykuly dla analizy
var articles = 
	[{
		article: 'Miasta_w_Polsce',
		deepStep: 1,
	},{
		article: 'Organizacje_turystyczne_w_Polsce',
		deepStep: 0
	},{
		article: 'Multikino',
		deepStep: 0
	},{
		article: 'Silver_Screen',
		deepStep: 0
	},{
		article: 'Cinema City',
		deepStep: 0
	}];

for (var elem in articles) {
	getArticleLinks(articles[elem].article.replace(/\s/g, "_"), articles[elem].deepStep);
}

var categories = ['Turystyka w Polsce', 'Kina w Polsce', 'Teatry w Polsce', 'Obiekty_sportowe_w_Polsce', 'Pomniki_według_roku_odsłonięcia', 'Pomniki historii'];

for (var category in categories) {
	getCategoryLinks(categories[category].replace(/\s/g, "_"), 3);
}