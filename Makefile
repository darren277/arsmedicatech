run-flask:
	.\.venv\Scripts\activate
	set FLASK_APP=.\app.py
	flask run

run-react:
	cd src && npm start
