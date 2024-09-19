import time


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f'[*] Время выполнения: {(end - start) * 1000:.3f} мс')
        return return_value

    return wrapper


def benchmark_iter(iters):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            total = 0
            return_value = None
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total += (end - start)
            print(f'[*] Общее время выполнения  : {total * 1000:.3f} мс')
            print(f'[*] Среднее время выполнения: {total / iters * 1000:.3f} мс')
            return return_value

        return wrapper

    return actual_decorator
