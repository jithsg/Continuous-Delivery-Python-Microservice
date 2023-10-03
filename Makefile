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
	docker build -t my-fastapi-app:latest .
run:
	docker run -d --name my-fastapi-app -p 8080:8080 my-fastapi-app:latest
deploy:
	#deploy to AWS ECR
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 185183796631.dkr.ecr.us-east-1.amazonaws.com
	docker build -t fastapi-wiki .
	docker tag fastapi-wiki:latest 185183796631.dkr.ecr.us-east-1.amazonaws.com/fastapi-wiki:latest
	docker push 185183796631.dkr.ecr.us-east-1.amazonaws.com/fastapi-wiki:latest

all: install format lint test build deploy
