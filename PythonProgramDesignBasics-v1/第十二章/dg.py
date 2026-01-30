def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def range_sum(num_list, start, end):
    if start > end:
        return 0
    else:
        return num_list[start] + num_list(num_list, start + 1, end)


def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


def n_num(n):
    if n <= 0:
        return 0
    if n > 1:
        n_num(n - 1)
    print(n)


def max_list(ls):
    if len(ls) == 1:
        return ls[0]
    max_of_rest = max_list(ls[1:])
    if ls[0] > max_of_rest:
        return ls[0]
    else:
        return max_of_rest


def sum_list(ls):
    if len(ls) == 1:
        return ls[0]
    else:
        return ls[0] + sum_list(ls[1:])


def num_total(num):
    if num == 1:
        return 1
    else:
        return num + num_total(num - 1)


def num_xx(num1, xx):
    if xx == 0:
        return 1
    else:
        return num1 * num_xx(num1, xx - 1)


def num_and(num1, num2):
    if num2 == 1:
        return num1
    else:
        return num1 + num_and(num1, num2 - 1)


def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, n)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
