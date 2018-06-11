var express = require('express');
var routes = require('./routes.js');
var port = 8000;

var app = express();

app.use(express.static('public'));
app.set('view engine', 'ejs');

routes(app);

app.listen(port, () => 
	console.log("Server listening on port " + port + "...")
);
