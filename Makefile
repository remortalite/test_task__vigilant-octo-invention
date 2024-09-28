run-redis:
	docker run -d --name redis-for-funbox -p 6379:6379 -it redis/redis-stack:latest

stop-redis:
	docker stop redis-for-funbox

run:
	poetry run python funbox/main.py

test:
	poetry run python -m pytest funbox/tests.py