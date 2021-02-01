def exp_op(x, y):
    return x ** y


def exp_without_op(x, y):
    x = 1 / x
    res = x
    for i in range(y * -1 - 1):
        res *= x
    return res


a = 9
b = -5

print(exp_op(a, b))
print(exp_without_op(a, b))
