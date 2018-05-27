'''
Iterator
'''
class CountDown:
    def __init__(self, step):
        self.step = step
    def __next__(self):
        """Return the next element."""
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step
    def __iter__(self):
        """Return the iterator itself."""
        return self

'''
Generator
'''
def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

# How to use
fib = fibonacci()
next(fib)
next(fib)
[next(fib) for i in range(10)]

def power(values):
    for value in values:
        print('Supply %s.', value)
        yield value

def adder(values):
    for value in values:
        print('Add a value to %s', value)
        if value % 2 == 0:
            yield value + 3
        else:
            yield value + 2

# How to use
elements = [1, 4, 7, 9, 12, 19]
results = adder(power(elements))
next(results)
next(results)

def psychologist():
    print('What is your concern?')
    while True:
        answer = (yield)
        if answer is not None:
            if answer.endswith('?'):
                print("You should not ask for yourself.")
            elif 'good' in answer:
                print("Sounds good! Do it!")
            elif 'bad' in answer:
                print("Don't mind")

# How to use
free = psychologist
next(free)
free.send('I feel bad.')

'''
Generator expression
'''

iter = (x**2 for x in range(10) if x % 2 == 0)
for el in iter:
    print(el)

'''
Decorator
'''
def mydecorator(function):
    def wrapped(*args, **kwargs):
        # Write pre-processor
        result = function(*args, **kwargs)
        # Write post-processor
        return result
    return wrapped

class DecortorAsClass:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        # Write pre-processor
        result = self.function(*args, **kwargs)
        # Write post-processor
        return result

def repeat(number=3):
    """
    Repeat decorated function number times.
    :param number: number of repeat. default 3
    """
    def actual_decorator(function):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(number):
                result = function(*args, **kwargs)
            return result
        return wrapper
    return actual_decorator
