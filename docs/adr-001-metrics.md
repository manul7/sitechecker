# Website metrics

# Context
Original requirements:
> The website checker should perform the checks periodically and collect the HTTP response time, status code returned,
> as well as optionally checking the returned page contents for a regexp pattern that is expected to be found on 
> the page.

However, this requirements are not enough to make adequate decisions about target web site state. To make this metrics more useful, it's necessary to collect more data, for example time when the request was sent, original regex pattern, etc.

# Decision
Stay in the scope of the original requirements and not to implement collection of any other parameters.

# Status
accepted

# Consequences
Application will not be very useful, but it will be a good example of how to use Kafka and PostgreSQL.
Python apps will remain simple and easy to understand.
