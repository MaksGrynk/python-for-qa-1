
import random


application = random.choice(('PyCharm', 'Sublime Text 2', 'Sublime Text 3',
                             'Vim', 'Eclipse'))

if application.lower() == 'pycharm':
    print('Using IDE')
elif application.startswith('Sublime'):
    print('Using text editor')
elif application == 'Vim':
    print('Working from console')
else:
    print('Unknown application')
