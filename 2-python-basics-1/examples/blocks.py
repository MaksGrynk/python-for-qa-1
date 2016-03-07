
import random


application = random.choice(('PyCharm Community Edition - 5.01',
                             'PyCharm Professional - 5.05',
                             'PyCharm Community Edition - 5.03'))

if 'pycharm' in application.lower():
    print('working with IDE')

    version = application[(application.index('-') + 1):]
    print('IDE version is {}'.format(version))

    if 'professional' in application.lower():
        print('licensed version is used')
    else:
        print('free version is used')
