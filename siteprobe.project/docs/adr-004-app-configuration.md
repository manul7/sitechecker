# Applications configuration

# Context
There are several ways to configure applications:
* Environment variables
* Configuration files
* Command line arguments
* Hardcoded values

Each approach has its own pros and cons. For example, environment variables are easy to use in Docker containers, but it's not easy to use them in development environment. 
Configuration files are easy to use in development environment, but it's not easy to use them in Docker containers.
Command line arguments are easy to use in development environment and in Docker containers, but it's not easy to use them in production environment. 
Hardcoded values are easy to use in development environment, but it's not easy to change them and in most cases create security issues.

# Decision
This app is supposed to be running as a Docker container, so it's better to use environment variables for configuration.
Exception - target websites list and checks configuration. It's better to use configuration file for this, but it's not mandatory and this will be hardcoded in `config.py` file.

# Status
accepted

# Consequences
It will not be possible to re-target this app to other sites without container image rebuild, but it's not a goal of this app.
This enhancement can be easily implemented in the future.
