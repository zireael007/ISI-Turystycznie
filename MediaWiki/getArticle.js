var bot = require('nodemw');
var fs = require('fs');
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

var reg = /\[{2,2}(\w|[ąśłńęóÓżźćĄĘŃŻŹĆŁŚ]|\s)+\]{2,2}/g

var cities = [];
//sciągamy strony z miastami Polski
client.getArticle('Miasta w Polsce', function(data){
 	cities = data.match(reg);
 	for (var city in cities) {
 		cities[city] = 'http://pl.wikipedia.org/wiki/' + cities[city].slice(2).slice(0,-2);
 	}
 	writeToFile('miasta_polski', cities.sort().join('\n'));
});
