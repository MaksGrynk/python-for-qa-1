
import re


text = '''
Posting Date: June 25, 2008 [EBook #11]
Release Date: March, 1994
[Last updated: December 20, 2011]

Language: English
'''


numbers_regexp = re.compile('\d+')
print(re.findall(numbers_regexp, text))
# ['25', '2008', '11', '1994', '20', '2011']

language_regexp = re.compile('language: (\w+)', re.IGNORECASE)
match = re.search(language_regexp, text)
if match:
    print(match.group(1))
    # English



