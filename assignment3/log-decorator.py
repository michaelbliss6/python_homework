import logging
from functools import wraps

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {list(args) if args else 'none'}")
        logger.log(logging.INFO, f"keyword parameters: {kwargs if kwargs else 'none'}")
        logger.log(logging.INFO, f"return: {result}\n")
        return result

    return wrapper


@logger_decorator
def say_hello():
    print("Hello, World!")

@logger_decorator
def accept_positional(*args):
    return True

@logger_decorator
def accept_keywords(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    say_hello()
    accept_positional(1, 2, "three")
    accept_keywords(name="Ada", language="Python")