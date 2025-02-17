from functools import wraps
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException

def handle_selenium_exceptions():
    """Decorator to handle Selenium exceptions with retries."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException) as e:
                print(f"Exception during selenium execution: {e}")
        return wrapper
    return decorator