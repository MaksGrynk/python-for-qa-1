
print('1')

def debug(fn):
    print('2')
    def wrapper(*args, **kwargs):
        print('3')
        return fn(*args, **kwargs)
    return wrapper

print('4')

@debug
def test(value):
    print('5')


test(11)
