
import csv


USERS = {
    'qa1': 'real name1',
    'qa2': 'real name2',
    'qa3': 'real name3'}



def get_data(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        result = []
        for row in reader:
            result.append(row)
    return result

def calculate_duplicates_words_rate(str1, str2):
    count = 0
    words = str1.split(' ')
    print(words)
    print(str2)
    for word in words:
        print(word, str2, (word in str2))
        if word in str2:
            count += 1

    return int(float(count) / len(words) * 100)


def main():
    data = get_data('bugs.csv')
    priority_issues = []
    for bug in data:
        if bug['Environment'] == 'staging':
            continue

        duplicate = False
        for priority_bug in priority_issues:
            rate = calculate_duplicates_words_rate(
                bug['Description'], priority_bug['Description'])
            if rate >= 80:
                print('duplicates are: \'{}\' and \'{}\''.format(
                    bug['Description'], priority_bug['Description']))
                duplicate = True
                break

        if duplicate:
            continue

        priority_issues.append(bug)

    for bug in priority_issues:
        if bug['Priority'] in ('critical', 'high'):
            print(bug)

    count = {}
    for bug in priority_issues:
        if bug['Owner'] not in count:
            count[bug['Owner']] = 0
        count[bug['Owner']] += 1

    print(count)

    for bug in priority_issues:
        bug['Owner'] = USERS.get(bug['Owner'])
        print(bug)

    print(max(count))

if __name__ == '__main__':
    main()
