
odd = [i for i in range(10) if i % 2]
print(odd)  # [1, 3, 5, 7, 9]

odd_squares = [i ** 2 for i in odd]
print(odd_squares)  # [1, 9, 25, 49, 81]


first_names = ['Bruce', 'James', 'Alfred']
last_names = ['Wayne', 'Gordon', 'Pennyworth']

heroes = ['{} {}'.format(f, l) for f, l in zip(first_names, last_names)]
print(heroes)  # ['Bruce Wayne', 'James Gordon', 'Alfred Pennyworth']
