# Precision of metrics

# Context
It's not mention how precise metrics should be collected.
For example,`response_time` could be collected in seconds, milliseconds, microseconds, etc.
Also it's not clear how many digits in fractional part should be collected.

# Decision
Time will be collected in seconds.
Fractional part will be rounded to 6 digits, but implemented as configurable parameter.

# Status
accepted

# Consequences
This decision will allow to collect metrics with high precision, but not to waste a lot of disk space.