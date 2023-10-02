install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	black *.py
lint:
	pylint --disable=R,C,W1203,W1202 main.py mylib/*.py
	flake8 --ignore=E501 main.py mylib/*.py
test:
	pytest -vv --cov=mylib test_*.py
build:
	#build container
deploy:
   #deploy
all: install format lint test build deploy
