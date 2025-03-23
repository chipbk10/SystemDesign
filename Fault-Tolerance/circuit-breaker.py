import time
from enum import Enum
from functools import wraps

class State(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"

class CircuitBreaker:

    # failure_threshold - number of limited requests is allowed in `HALF_OPEN` mode
    # reset_timeout - amount of time for our api to be recovered
    # failure_count - number of failures since the last successful response
    # last_failure_time - the first time we fail the request after the last successful response
    def __init__(self, failure_threshold=5, reset_timeout=60):
        self.state = State.CLOSED
        self.failure_count = 0
        self.failure_threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self.last_failure_time = None

    def call(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.state == State.OPEN:
                if time.time() - self.last_failure_time > self.reset_timeout:
                    print("Attempting to recover: moving to HALF_OPEN")
                    self.state = State.HALF_OPEN
                else:
                    raise Exception("Circuit is OPEN. Service unavailable.")
            
            try:
                result = func(*args, **kwargs)
                if self.state == State.HALF_OPEN:
                    print("Service recovered: moving to CLOSED")
                    self.state = State.CLOSED
                    self.failure_count = 0
                return result
            except Exception as e:
                self.failure_count += 1
                print(f"Failure detected. Count: {self.failure_count}")
                
                if self.failure_count >= self.failure_threshold:
                    print("Threshold exceeded: moving to OPEN")
                    self.state = State.OPEN
                    self.last_failure_time = time.time()
                raise e
        return wrapper

# Example usage in a server
breaker = CircuitBreaker(failure_threshold=3, reset_timeout=10)

@breaker.call
def unreliable_service():
    # Simulate a service that fails intermittently
    import random
    if random.random() > 0.7:
        raise Exception("Service failed!")
    return "Service worked!"

# Test the circuit breaker
def test_circuit_breaker():
    for _ in range(10):
        try:
            result = unreliable_service()
            print(f"Success: {result}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1)

if __name__ == "__main__":
    test_circuit_breaker()
