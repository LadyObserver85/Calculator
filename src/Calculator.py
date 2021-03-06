def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return 'Error: divisor b can not be zero'


def square_a_number(a):
    return a ** 2


def square_root_a_number(a):
    return a ** .5


class Calculator:

    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square_a_number(a)
        return self.result

    def square_root(self, a):
        self.result = square_root_a_number(a)
        return self.result
