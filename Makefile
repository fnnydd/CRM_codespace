postgres:
	docker-compose -f docker-compose.yml  up

bash:
	docker-compose -f docker-compose.yml exec postgres bash