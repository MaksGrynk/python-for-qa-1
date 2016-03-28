
import os
import tempfile


temp = tempfile.NamedTemporaryFile()
print(temp.name)
print(os.path.isfile(temp.name))

temp.write('Some data')
temp.flush()


with open(temp.name, 'r') as f:
    print(f.read())

temp.close()
print(os.path.isfile(temp.name))

# /var/folders/gh/50_jfxjn6kq1_kv456t57b840000gn/T/tmpv79kEu
# True
# Some data
# False



