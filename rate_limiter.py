import time

class RateLimiter:
    def __init__(self, max_requests, window_size):
        """
        Initializes a RateLimiter object with a maximum number of requests
        allowed within a given window size in seconds.
        
        :param max_requests: Maximum number of requests allowed
        :param window_size: Window size in seconds
        """
        self.max_requests = max_requests
        self.window_size = window_size
        self.request_timestamps = []

    def allow_request(self):
        """
        Determines if a new request is allowed under the current rate limit.
        
        :return: True if the request is allowed, False otherwise
        """
        current_time = time.time()
        # Clean up old timestamps that are outside the rate limit window
        self.request_timestamps = [timestamp for timestamp in self.request_timestamps if current_time - timestamp < self.window_size]
        
        if len(self.request_timestamps) < self.max_requests:
            self.request_timestamps.append(current_time)
            return True
        else:
            return False
