
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by zero')
    else:
        print('result is {}'.format(result))
    finally:
        print('divide function was run with x={}, y={}'.format(x, y))


divide(5, 2)  # result is 2, divide function was run with x=5, y=2
divide(10, 0)  # division by zero, divide function was run with x=10, y=0
