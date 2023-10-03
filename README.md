# Continuous-Delivery-Python-Microservice
FastAPI Wikipedia API

A simple FastAPI application that provides endpoints to fetch summaries and search results from Wikipedia.

Endpoints:
/: Welcome endpoint, returns a greeting message.
/wiki/{name}: Returns a summary from Wikipedia based on the given name.
/search/{name}: Returns a list of Wikipedia search results based on the given name.

Setup and Installation:
1. Install Dependencies:
   To install the required Python packages, run:
   make install

2. Run the Application:
   If you wish to run the app locally, execute:
   uvicorn main:app --reload
   The application will be available at http://localhost:8000.

Code Quality:
1. Format Code:
   We use black for code formatting. Run the following command to format your code:
   make format

2. Linting:
   Check for linting issues using pylint and flake8:
   make lint

3. Run Tests:
   Execute unit tests and view coverage:
   make test

Docker Commands:
1. Build Docker Image:
   make build

2. Run Docker Container:
   make run
   The Dockerized application will be available at http://localhost:8080.

3. Deploy to AWS ECR:
   Make sure you have configured your AWS credentials. Then, run:
   make deploy
   This will build the Docker image, tag it, and push it to the specified ECR repository.

Miscellaneous:
Run all the above commands (install, format, lint, test, build, deploy) sequentially with:
make all

