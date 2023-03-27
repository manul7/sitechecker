import logging.config
import os

logger_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": logging.INFO,
        },
    },
    "loggers": {
        "keeper": {"handlers": ["console"], "level": logging.INFO, "propagate": False},
        "probe": {"handlers": ["console"], "level": logging.INFO, "propagate": False},
    },
}

# Configure the logger using the dictionary configuration
logging.config.dictConfig(logger_config)

# Kafka topics
# Availability checks
TOPIC_AVAILABILITY = "site_availability"
# Content checks
TOPIC_CONTENT = "site_content"

# Kafka connection configuration
kafka_config = {
    # Kafka connection URI
    "uri": os.getenv("KAFKA_SERVICE_URI"),
    # Default protocol is SSL
    "protocol": os.getenv("KAFKA_SECURITY_PROTOCOL", "SSL"),
    # Path to CA file
    "ssl_cafile": os.getenv("KAFKA_SSL_CA", "access/ca.pem"),
    # Path to SSL certificate file
    "ssl_certfile": os.getenv("KAFKA_SSL_CERT", "access/service.cert"),
    # Path to SSL key file
    "ssl_keyfile": os.getenv("KAFKA_SSL_KEY", "access/service.key"),
}

KAFKA_AVAIL_CONSUMER_ID = os.getenv("KAFKA_AVAIL_CONSUMER_ID", "AvailabilityConsumer")
KAFKA_CONTENT_CONSUMER_ID = os.getenv("KAFKA_CONTENT_CONSUMER_ID", "ContentConsumer")

# Postgres connection URI
DATABASE_URI = os.getenv("DATABASE_URI")

# Global checks interval in seconds
CHECK_INTERVAL = os.getenv("CHECK_INTERVAL", 10)

# List of targets
TARGETS = [{"url": "https://example.com", "regex pattern": "Example Domain"}]
