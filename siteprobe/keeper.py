import argparse
import logging
from typing import List, Union

import psycopg2
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable

import config
import sql_scripts

logger = logging.getLogger("keeper")


def get_consumer(topic_name: str):
    """Create a Kafka consumer for the provided topic.
    :param topic_name: Name of the topic to consume messages from.
    :return: Kafka consumer.
    """
    try:
        consumer = KafkaConsumer(
            str(topic_name),
            client_id=config.KAFKA_AVAIL_CONSUMER_ID,
            bootstrap_servers=config.kafka_config["uri"],
            security_protocol=config.kafka_config["protocol"],
            ssl_cafile=config.kafka_config["ssl_cafile"],
            ssl_certfile=config.kafka_config["ssl_certfile"],
            ssl_keyfile=config.kafka_config["ssl_keyfile"],
        )
        return consumer
    except NoBrokersAvailable:
        logger.error("Unable to connect to the Kafka broker.")
        raise
    except FileNotFoundError:
        logger.exception("Unable to find SSL files. Please check configuration")
        raise


def execute_sql_script(conn, script: str, data: Union[List, None] = None):
    """Execute a SQL script.
    :param conn: Database connection.
    :param script: SQL script to execute.
    :param data: Data to insert.
    """
    with conn:
        with conn.cursor() as cursor:
            if data is None:
                cursor.execute(script)
            else:
                cursor.execute(script, data)
            conn.commit()


def process(conn, consumer, metric_type: str):
    """Process the messages from the Kafka topic and store them in the database.
    :param conn: Database connection.
    :param consumer: Kafka consumer.
    :param metric_type: Metric type.
    """
    try:
        while True:
            for message in consumer.poll().values():
                data = message[0].value.decode("utf-8").split(",")
                if metric_type == "availability":
                    logger.debug("Inserting availability data: %s", data)
                    execute_sql_script(conn, sql_scripts.insert_availability_row, data)
                else:
                    logger.debug("Inserting content data: %s", data)
                    execute_sql_script(conn, sql_scripts.insert_content_row, data)
    except KeyboardInterrupt:
        conn.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mtype", choices=[config.ARG_AVAIL, config.ARG_CONTENT], help="Metric type"
    )
    # Try to establish a connection to the database before moving to the next step.
    try:
        db_connection = psycopg2.connect(config.DATABASE_URI)
    except psycopg2.OperationalError as e:
        logger.error("Unable to connect to the database: %s", e)
        return

    args = parser.parse_args()
    if args.mtype == config.ARG_AVAIL:
        topic = config.TOPIC_AVAILABILITY
        table_script = sql_scripts.availability_table_script
    else:
        topic = config.TOPIC_CONTENT
        table_script = sql_scripts.content_table_script

    consumer = get_consumer(topic)
    logger.info("Connected to the Kafka broker.")
    execute_sql_script(db_connection, table_script)
    logger.info("Table for %s metrics set.", args.mtype)
    process(db_connection, consumer, args.mtype)


if __name__ == "__main__":
    main()
