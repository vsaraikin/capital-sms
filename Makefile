run:
	 docker-compose down && docker-compose up --build

format:
	black .

lint:
	 ruff check .