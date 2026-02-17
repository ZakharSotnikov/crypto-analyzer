import time


def retry(max_attempts, delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts <= max_attempts:
                attempts += 1
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempts == max_attempts:
                        print(f"Попытка {attempts}")
                        print(f"Подключиться не удалось. Произошла ошибка {e}")
                        print()
                        raise
                    print(f"Попытка {attempts}")
                    print(f"Пробую снова через {delay} секунд")
                    print()
                    time.sleep(delay)
        return wrapper
    return decorator
