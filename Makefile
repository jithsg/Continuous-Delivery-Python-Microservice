install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	black *.py
lint:
	pylint --disable=R,C,W1203,W1202 main.py mylib/*.py
test:
	pytest -vv --cov=main tests/*.py
deploy:
   #deploy
all: install format lint test deploy
