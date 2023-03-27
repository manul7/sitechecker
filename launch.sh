#!/usr/bin/env bash
# Check for access files
for f in access/ca.pem access/service.key access/service.cert; do
    if [ ! -f "$f" ]; then
        echo "$f not found. Please get $f from your cluster and put it in $f"
        exit 1
    fi
done

if [ ! -f ".env" ]; then
  echo -e "
  .evn not found. Please create .env file with the following content:\n
      KAFKA_SERVICE_URI=<Kafka connection string>
      DATABASE_URI=<PostgreSQL connection string>
  "
fi


# Build images
docker build -f keeper.Dockerfile -t keeper:1 .
docker build -f checker.Dockerfile -t checker:1 .

# Run containers
docker compose up