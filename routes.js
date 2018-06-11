pyshell = require('python-shell');

module.exports = function(app) {
	app.get('/', (req, res) => {
		res.render('pages/index');
	});

	app.get('/about', (req, res) => {
		res.render('pages/about');
	});

	app.get('/memes', function(req, res) {
		var options = {
			mode: 'text',
			args: [ req.query.id || "empty" ]
		}

		pyshell.run('main.py', options, function(err) {
			if (err) throw err;
			console.log('finished execution pyshell');
			//res.sendFile(__dirname + "/public/meempie.png");
			res.render('pages/memes');
		})
	})

	app.get('/alv', function(req, res) {
		var options = {
			mode: 'text',
			args: [req.query.top || 'leden', req.query.bottom || 'dors op alw']
		}

		pyshell.run('hugo.py', options, function(err) {
			if (err) throw err;
			console.log('finished exection pyshell');
			res.sendFile(__dirname + "/public/hugo.png");
		})
	})

	app.get('/particles', function(req, res) {
		res.render('pages/particles');
	});
};
