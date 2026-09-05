import time
import functools
from typing import Callable, Any

def timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to measure execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"[{func.__name__}] executed in {duration:.6f}s")
        return result
    return wrapper
