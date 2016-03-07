
from __future__ import print_function

print(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(range(5, 12))  # [5, 6, 7, 8, 9, 10, 11]
print(range(20, 0, -2))  # [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
for i in range(10):
    print(i, end=', ')

print()
# P, y, C, h, a, r, m,
app = 'PyCharm'
for i in app:
    print(i, end=', ')

print()
envs = {'local': 1,
        'staging': 2,
        'production': 3}

for k, v in envs.items():
    print('Key: {}, value: {}'.format(k, v))
