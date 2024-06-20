# copilot-test

## Rate Limiting Module

This module provides a simple way to implement rate limiting for your applications. It uses a sliding window log algorithm to efficiently manage request rates over time.

### How to Use

To use the `RateLimiter` class, you need to initialize it with the maximum number of requests allowed within a given window size in seconds, and the number of concurrent workers. Here is a basic example:

```python
from rate_limiter import RateLimiter

# Initialize the rate limiter to allow 100 requests per minute for 5 workers
rate_limiter = RateLimiter(max_requests=100, window_size=60, worker_count=5)

# Check if a request is allowed
if rate_limiter.allow_request():
    print("Request allowed")
else:
    print("Request denied")
```

### Understanding the Worker Count Parameter

The `worker_count` parameter is crucial for applications that operate with multiple concurrent workers or threads. It allows the `RateLimiter` to adjust the rate limiting logic proportionally, ensuring that the overall rate limit is maintained across all workers. This means that the effective rate limit per worker is the total `max_requests` divided by the `worker_count`. This adjustment ensures fair access and prevents any single worker from monopolizing the request quota.

### Dependencies

This module requires Python 3.6 or later. No external libraries are needed.
