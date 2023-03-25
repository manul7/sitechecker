# Kafka topics

# Context
Kafka provides a way to organize data in topics. Each topic is a category or feed name to which records are published. Topics in Kafka are always multi-subscriber; that is, a topic can have zero, one, or many consumers that subscribe to the data written to it.

# Decision
It would be better to use Kafka topics to organize data in the following way:
* `availability` - topic for availability check results
* `content` - topic for content checks

# Status
accepted

# Consequences
This will allow to try Kafka's topics feature and to organize data in a more structured way.
This complicates implementation of producer and consumer apps, but it is a good way to learn Kafka.
