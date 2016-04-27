

import csv


def get_data(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        result = []
        for row in reader:
            result.append(row)
        return result


def calculate_duplicate_words_rate(str1, str2):
    if str1 == None:
        import ipdb; ipdb.set_trace()
        print('2')
    count = 0
    words = str1.split(' ')
    for word in words:
        if word in str2:
            count += 1

    if count == 0:
        rate = 0
    else:
        rate = int(count / len(words) * 100)

    return rate


def main():
    data = get_data('Python for QA - bugs list - Sheet1.csv')

    for i in range(len(data), 0, -1):  # reversed, range, enumerate
        index = i - 1
        bug = data[index]

        print('Processing bug {}'.format(bug['#']))

        if bug['Environment'] == 'staging':
            del data[index]
            continue

        for j in range(index - 1, 0, -1):
            rate = calculate_duplicate_words_rate(
                bug['Description'], data[j]['Description'])
            if rate >= 80:
                del data[j]
                break

    print(len(data))
    for bug in data:
        print(bug)
    print('Done')


def main2():
    data = get_data('Python for QA - bugs list - Sheet1.csv')
    priority_bugs = []

    for bug in data:
        if bug['Environment'] == 'staging':
            continue

        duplicate = False
        for priority_bug in priority_bugs:
            rate = calculate_duplicate_words_rate(
                bug['Description'], priority_bug['Description'])
            if rate >= 80:
                print('duplicates are: \'{}\' and \'{}\''.format(
                    bug['Description'], priority_bug['Description']))
                duplicate = True
                break

        if duplicate:
            continue

        priority_bugs.append(bug)

    print(len(priority_bugs))



if __name__ == '__main__':
    main2()
