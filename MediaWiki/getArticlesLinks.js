var bot = require('nodemw');
var fs = require('fs');
var _ = require('lodash');

var client = new bot({
	"server": "pl.wikipedia.org",	//host name of MediaWIki
	"path": "/w",					//path to api.php
	"debug": false
});

var writeToFile = function(file, data) {
	//write links to file
	fs.writeFile(file, data, function(err) {
    	if(err) {
	        console.log(err);
    	} else {
        	console.log(file + " done!!!");
    	}
	}); 

};

var getLinks = function (articleName, fileName) {
	client.getArticle(articleName, function(data){
	 	var links = data.match(reg);
	 	links.push(articleName);
	 	for (var link in links) {
	 		links[link] = 'http://pl.wikipedia.org/wiki/' + links[link].slice(2).slice(0,-2).replace(/\s/g, "_");
	 	}
	 	links = _.uniq(links);
	 	writeToFile(fileName, links.sort().join('\n'));
	});
};

var reg = /\[{2,2}(\w|[ąśłńęóÓżźćĄĘŃŻŹĆŁŚ]|\s)+\]{2,2}/g


//artykuly dla analizy
var articles = [ 
	{
		article: 'Miasta w Polsce',
		fileName: 'miasta_polski'
	}, 
	{
		article: 'Lista uzdrowisk w Polsce',
		fileName: 'uzdrowiska_polski'
	}];

for (var elem in articles) {
	getLinks(articles[elem].article, articles[elem].fileName);
}