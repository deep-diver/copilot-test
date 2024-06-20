# copilot-test

## Rate Limiting Module

This module provides a simple way to implement rate limiting for your applications. It uses a sliding window log algorithm to efficiently manage request rates over time.

### How to Use

To use the `RateLimiter` class, you need to initialize it with the maximum number of requests allowed within a given window size in seconds. Here is a basic example:

```python
from rate_limiter import RateLimiter

# Initialize the rate limiter to allow 100 requests per minute
rate_limiter = RateLimiter(max_requests=100, window_size=60)

# Check if a request is allowed
if rate_limiter.allow_request():
    print("Request allowed")
else:
    print("Request denied")
```

### Dependencies

This module requires Python 3.6 or later. No external libraries are needed.
