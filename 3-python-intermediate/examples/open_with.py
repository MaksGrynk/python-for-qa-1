

try:
    f = open('integers.txt', 'r')
    s = f.readline()
    i = int(s.strip())
    print(i)
except ValueError:
    print('No valid integer in line.')
finally:
    f.close()


with open('integers.txt', 'r') as f:
    try:
        s = f.readline()
        i = int(s.strip())
        print(i)
    except ValueError:
        print('No valid integer in line.')
