# Application packaging

# Context
Python application can be packaged in several ways - as Python Wheel, Python Egg (outdated), tarball, or Docker image.
Each way has its own pros and cons as well as purpose.

# Decision
Standard Python packaging is not used, because this app is not lib or CLI tool.
Two separate containers should be used for the app which produces metrics and the app which saves metrics.

# Status
accepted

# Consequences
It will be impossible to use PyPi for the app distribution.
Docker or similar containerization technology should be used for the app deployment.