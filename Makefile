# Define the Docker Compose file
COMPOSE_FILE = compose.yml

# Target to build and run the main Fibonacci service
run:
	docker-compose up --build fibonacci-service

# Target to run the tests
test:
	docker-compose up --build test
