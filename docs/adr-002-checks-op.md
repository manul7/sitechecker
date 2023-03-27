# Checks operation

# Context
Original requirements:
> The website checker should perform the checks periodically ...

It would be better to perform checks periodically, but with individual interval for each check. 
This would allow to increase performance and make check independent from each other, moreover this could open the road to more robust and fault tolerant application.

However, implementation of this feature would require more complex architecture and more complex code (async programming, queues, etc.).

# Decision
Stay in the scope of the original requirements and user global interval for all checks.

# Status
accepted

# Consequences
Python apps will remain simple and easy to understand.