from functools import wraps
import time

def timer(func):
    """
    Measure and print function execution time.
    
    Usage:
        @timer
        def slow_function():
            time.sleep(1)
    
    Output: "slow_function took 1.0023 seconds"
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def logger(func):
    """
    Log function calls with arguments and return value.
    
    Usage:
        @logger
        def add(a, b):
            return a + b
        
        add(2, 3)
    
    Output:
        "Calling add(2, 3)"
        "add returned 5"
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}{args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
    """
    Retry a function on failure.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Seconds to wait between retries
        exceptions: Tuple of exceptions to catch
    
    Usage:
        @retry(max_attempts=3, delay=0.5)
        def flaky_api_call():
            # might fail sometimes
            pass
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"Attempt {_ + 1} failed with error: {e}")
                    if _ < max_attempts - 1:
                        time.sleep(delay)

        return wrapper
    return decorator

def cache(max_size=128):
    """
    Cache function results.
    Similar to lru_cache but with visible cache inspection.
    
    Usage:
        @cache(max_size=100)
        def expensive_computation(x):
            return x ** 2
        
        expensive_computation(5)  # Computes
        expensive_computation(5)  # Returns cached
        
        # Inspect cache
        expensive_computation.cache_info()
        expensive_computation.cache_clear()
    """
    cache = {}
    cache_info = {
        'hits': 0, 
        'misses': 0, 
        'size': len(cache), 
        'max_size': max_size
    }
    def decorator(func):
        func.cache_info = lambda: cache_info
        func.cache_clear = lambda: cache.clear()
        @wraps(func)
        # change cache.keys() to tuple of args and kwargs to handle unhashable types
        def wrapper(*args, **kwargs):
            if (args, kwargs) not in cache.keys():
                result = func(*args, **kwargs)
                if len(cache) >= max_size:
                    cache.pop(next(iter(cache)))  # Remove oldest item
                cache[(args, kwargs)] = result
            else:
                wrapper.hits += 1
                return cache[(args, kwargs)]
            wrapper.misses += 1
            return result
        return wrapper
    return decorator

@timer
@logger
def add(a, b):
    return a + b

print(add(2, 3))

@retry(max_attempts=3, delay=0.5)
def flaky_api_call():
    # might fail sometimes
    pass

flaky_api_call()