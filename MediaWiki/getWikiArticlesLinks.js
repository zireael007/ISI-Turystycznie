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
var allExternalLinks = [];
var wikiLinksFile = 'wikiLinks';
var wikiExternalLinksFile = 'wikiExternalLinks';

var clearFile = function (fileName) {
	fs.writeFile(fileName, '', function(){console.log('Zawartośc pliku' + fileName +  'została usunieta')});
};

clearFile(wikiLinksFile);
clearFile(wikiExternalLinksFile);

var appendToFile = function(fileName, dataName, data, cb) {
	fs.appendFile(fileName, data.join('\n') + '\n', function(err) {
		if(err) {
		  	console.log(err);
    	} else {
        	console.log(dataName + " gotowe!!!");
        	console.log('Liczba artykułów ' + (numberOfPages++) +'.');
       		console.log('Zapisano ' + (allLinks.length) +' linków.\n');
       		console.log('Zapisano ' + (allExternalLinks.length) +' zewnętrznych linków.\n');
       		if (cb) {
    			cb();
    		}        			
    	}
	});
};

var prepareExternalToWrite = function (dataName, data) {
	console.log('prepareExternalToWrite' + data);
	if(!_.isEmpty(data)) {
		var oldExternalLinks = _.clone(allExternalLinks);
		allExternalLinks = _.union(allExternalLinks, data);
		var diff = _.difference(allExternalLinks, oldExternalLinks);
		if(!_.isEmpty(diff)) {
			appendToFile(wikiExternalLinksFile, dataName, diff);
		}
	}
};

var prepareToWrite = function(dataName, data, cb) {
	//write links to file
	if (!_.isEmpty(data)) {
		data = _.filter(data, function(item) {
			return item.indexOf('Kategoria') == -1;
		});
		var oldLinks = _.clone(allLinks);
		allLinks = _.union(allLinks, data);
		var diff = _.difference(allLinks, oldLinks);
		if (!_.isEmpty(diff)) {
			appendToFile(wikiLinksFile, dataName, diff, cb);
		}
	}
};

var getExternalLinks = function (articleName) {
	console.log('Sciagamy linki zewnetrzne - ', articleName);
	client.getExternalLinks(articleName, function(data) {
		data = _.flatten(data, '*');
		if (!_.isEmpty(data)) {
			console.log(data);
			prepareExternalToWrite(articleName, data);	
		}
	});
};

var getArticleLinks = function (articleName, deepStep) {
	client.getArticle(articleName, function(data){
		console.log('sciagam artykul ' + articleName);
	 	var links = data.match(reg);
	 	links.push(articleName);
	 	for (var link in links) {
	 		if (deepStep != 0) {
	 			getArticleLinks(links[link].slice(2).slice(0,-2).replace(/\s/g, "_"), deepStep - 1);
	 			getExternalLinks(links[link].slice(2).slice(0,-2).replace(/\s/g, "_"));
	 		}
	 		links[link] = 'http://pl.wikipedia.org/wiki/' + links[link].slice(2).slice(0,-2).replace(/\s/g, "_");
	 	}
	 	links = _.uniq(links);
	 	prepareToWrite('akrtykuł:'+ articleName, links.sort(), function () {
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
		_.forEach(data, function (item) {
			getExternalLinks(item);
		});
		data = _.map(data, function (elem) {
			return 'http://pl.wikipedia.org/wiki/' + elem.replace(/\s/g, "_");
		});
		if (data.length != 0) {
			prepareToWrite('kategoria:' + categoryName, data, function() {
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