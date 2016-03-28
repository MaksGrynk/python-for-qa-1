

f = open('temp.txt', 'w')
lines = ['line {}\n'.format(i) for i in range(10)]
f.writelines(lines)
f.close()


f = open('temp.txt', 'r+')
f.seek(7)
line = f.readline()
print(line)

f.write('new line')
f.close()


f = open('temp.txt', 'r')
print(f.read())
f.close()




