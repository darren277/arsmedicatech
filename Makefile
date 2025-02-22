include .env

# To initialize `.venv`: `python3 -m venv .venv`.

run-flask:
	.\.venv\Scripts\activate
	set FLASK_APP=.\app.py
	flask run --host=$(HOST) --port=$(PORT)

run-flask-linux:
	. .venv/bin/activate
	export FLASK_APP=./app.py
	flask run --host=$(HOST) --port=$(PORT)


run-react-dev:
	npm start


run-react-prod:
	npm run build
	npx http-server ./dist -p $(REACT_PORT)
