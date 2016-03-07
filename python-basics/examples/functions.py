

def add_to_cache(cache, key, value=''):
    """Adds value to cache if key is new."""
    if key in cache:
        return False
    cache[key] = value
    return True


cache = {}
result = add_to_cache(cache, 'key1', 'value1')
print(result)
add_to_cache(cache, 'key2', 'value2')
print(add_to_cache(cache, 'key2', 'value3'))
print(add_to_cache(cache, 'key3'))
print(cache)

# Result:
# True
# False
# True
# {'key3': '', 'key2': 'value2', 'key1': 'value1'}
