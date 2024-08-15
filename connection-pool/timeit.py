import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()
        total_time = end_time - start_time
        print(f"The function '{func.__name__}' took {total_time:.2f} seconds to complete.")
        return result

    return wrapper
