array = [1,3,4,2,9]


def differ(a, b):
    if a >= b:
        a = a - b
    else:
        a = b - a
    return a


def evaluate(arr):
    even = 1
    odd = 0
    for i in arr:

        if i % 2 == 0:
            even *= i
        else:
            odd += i

    return differ(even, odd)


x = evaluate(array)


print(x)