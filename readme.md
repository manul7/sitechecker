# Simple Site Monitoring app
This is sample application, which purpose is to probe Kafka and PostgreSQL services as building blocks for a simple site monitoring application.

# Overall goal
Try Kafka and ProstgreSQL services to implement a simple site monitoring application using them and Python.

# High level architecture
The application consists of the following components:
1. Website checker
2. Database writer
3. Kafka as a message bus
4. PostgreSQL database

## Website checker
The website checker is a Python program that periodically checks the target websites (could be many) and sends the check results to a Kafka topics.
This app should perform the checks _periodically_ and collect the _HTTP response time_, _status code returned_, as well as **optionally** _checking the returned page contents for a regexp pattern_ that is expected to be found on the page.

## Database writer
The database writer is a Python program that reads the check results from the Kafka topics and writes them to a PostgreSQL database.
This app records the check results into one or more database tables and could handle a reasonable amount of checks performed over a longer period of time.
This app will not be based on ORM libraries, but rather on the Python DB API compliant library and raw SQL queries.

# Documentation
* Prerequisites are described in the [prerequisites](docs/prerequisites.md) file.
* All architecture decisions can be found in the [docs](docs) directory.

# Launch
To launch the application, run the following command:
```bash
bash launch.sh
```