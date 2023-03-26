import logging.config
import os


def is_file_exist(file_path: str):
    """Check if a file exists.
    :param file_path: Path to the file.
    :return: True if the file exists, False otherwise.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")


def is_empty_env_var(var_name: str):
    """Get the value of an environment variable.
    :param var_name: Name of the environment variable.
    :return: Value of the environment variable.
    """
    value = os.getenv(var_name)
    if not value:
        raise ValueError(f"Environment variable {var_name} is not set.")


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
            "level": logging.DEBUG,
        },
    },
    "loggers": {
        "keeper": {"handlers": ["console"], "level": logging.DEBUG, "propagate": False},
        "probe": {"handlers": ["console"], "level": logging.DEBUG, "propagate": False},
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

# It's worth to check if all the environment variables are set as it's human input.
for var in ["KAFKA_SERVICE_URI", "DATABASE_URI"]:
    is_empty_env_var(var)

for file in [
    kafka_config["ssl_cafile"],
    kafka_config["ssl_certfile"],
    kafka_config["ssl_keyfile"],
]:
    is_file_exist(file)
