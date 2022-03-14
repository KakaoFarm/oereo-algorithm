from pprint import pprint

case = int(input())

for i in range(case):
    N = int(input())
    category_book = dict()
    result = 1
    for j in range(N):
        categories = list(map(str, input().split()))
        category = categories[1]
        item = categories[0]
        if category not in category_book:
            category_book[category] = [item]
        else:
            category_book[category].append(item)

    for key, item in category_book.items():
        result *= (len(category_book[key]) + 1)

    print(result - 1)
