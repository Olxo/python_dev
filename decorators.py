def timed(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        print('Run time: {0:.6f}s'.format(elapsed))
        return result
    return inner

def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-2) + calc_fib_recurse(n-1)

@timed   #fib = timed(fib)
def fib(n):
    return calc_fib_recurse(n)

print(fib(20))


# decorator with 2 parameters
def timed(fn, reps):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(reps):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += (end - start)

        avr_run_time = total_elapsed / reps
        print('Avg run time: {0:.6f}s ({1} reps)'.format(avr_run_time, reps))
        return result
    return inner

def fib(n):
    return calc_fib_recurse(n)

fib = timed(fib, 5)
print(fib(28))


# factory decorator
def dec_factory():
    print('running dec factory')

    def dec(fn):
        print('running dec')

        def inner(*args, **kwargs):
            print('running inner')
            return fn(*args, **kwargs)
        return  inner
    return dec

dec = dec_factory()
print(dec)

def my_func():
    print('running my_func')

my_func = dec(my_func)
print('my_func: ', my_func())

# OR
@dec
def my_func():
    print('running my_func')

# OR
def my_func():
    print('running my_func')

my_func = dec_factory()(my_func)


# OR
@dec_factory()
def my_func():
    print('running my_func')