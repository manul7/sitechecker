# Docker & Docker Compose
It's mandatory to have Docker installed and running on your machine. See [official documentation](https://docs.docker.com/get-docker/) for details.

# Kafka
It's mandatory to have Kafka installed and running. Two topics should be created.
Bootstrap URI must be known, `ca.pem`, `service.cert`, `service.key` files must be present. 

It would be better to use one of managed Kafka services, like [Confluent Cloud](https://www.confluent.io/confluent-cloud/) or [Aiven](https://aiven.io/kafka).

# PostgreSQL
It's mandatory to have PostgreSQL installed and running. Database and user must be created.
Connection URI must be known.

It would be better to use one of managed PostgreSQL services, like [AWS RDS](https://aws.amazon.com/rds/postgresql/) or [Aiven](https://aiven.io/postgresql).

# Setup
## Kafka
Valid files `ca.pem`, `service.cert`, `service.key` must be available in `access` directory.
Variable `KAFKA_SERVICE_URI` must be specified in `.env` file in project root directory.

## PostgreSQL
Variable `DATABASE_URI` must be specified in `.env` file in project root directory.
