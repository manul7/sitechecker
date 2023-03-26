import logging
import time
from kafka import KafkaProducer
import config
from checks import check_site

logger = logging.getLogger("probe")


def main():
    producer = KafkaProducer(
        bootstrap_servers=config.kafka_config["uri"],
        security_protocol=config.kafka_config["protocol"],
        ssl_cafile=config.kafka_config["ssl_cafile"],
        ssl_certfile=config.kafka_config["ssl_certfile"],
        ssl_keyfile=config.kafka_config["ssl_keyfile"],
    )

    logger.info("Kafka producer connected to %s", config.kafka_config["uri"])

    try:
        while True:
            for target in config.TARGETS:
                logger.info("Checking %s", target["url"])
                if target["regex pattern"]:
                    pattern = target["regex pattern"]
                else:
                    pattern = None
                # Perform check
                response_time, status_code, match = check_site(target["url"], pattern)
                # Send metrics about availability
                message = f"{target['url']},{response_time},{status_code}"
                producer.send(config.TOPIC_AVAILABILITY, message.encode("utf-8"))
                logger.debug("Availability message: %s", message)
                # Send metrics about content
                if target["regex pattern"]:
                    message = f"{target['url']},{match}"
                    producer.send(config.TOPIC_CONTENT, message.encode("utf-8"))
                    logger.debug("Content message: %s", message)
            # Wait before next check
            time.sleep(config.CHECK_INTERVAL)
    # TODO: Replace with a more specific exception
    except KeyboardInterrupt:
        producer.close()


if __name__ == "__main__":
    main()
