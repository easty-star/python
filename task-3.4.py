def my_pow_func(x, y):
    try:
        ans = x ** y
    except TypeError:
        return 'Enter float'
    return ans


print(my_pow_func(10, -4))


# второй вариант
def my_pow_func(x, y):
    # y - целое отрицательное
    try:
        x, y = float(x), int(y)
        res = x
        for i in range(abs(y) - 1):
            res *= x  # res = res * x
        return 1 / res
    except ValueError:
        return 'Check value'