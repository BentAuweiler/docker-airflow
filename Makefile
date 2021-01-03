
launch:
	docker-compose -f docker-compose-LocalExecutor.yml up -d

kill:
	docker-compose -f docker-compose-LocalExecutor.yml down

build:
	docker build --rm -t auweiler/airflow-demo .