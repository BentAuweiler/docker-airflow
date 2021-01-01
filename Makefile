
launch_airflow:
	docker-compose -f docker-compose-LocalExecutor.yml up -d

kill_airflow:
	docker-compose -f docker-compose-LocalExecutor.yml down