import json
import csv

booksData = []
result = []

with open('user.json', 'r') as file:
    jsonData = json.load(file)

with open('books.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)
    for row in csvreader:
        booksData.append(row)


split = lambda lst, n: [lst[i::n] for i in range(n)]
books = split(booksData, len(jsonData))

for item, bookArr in zip(jsonData, books):
    refference = {"name": None, "gender": None, "address": None, "age": None, "books": None}
    refference['name'] = item['name']
    refference['gender'] = item['gender']
    refference['address'] = item['address']

    booksRefs = []
    for b in bookArr:
        book = {"title": None, "author": None, "pages": None, "genre": None}
        book['title'] = b[0]
        book['author'] = b[1]
        book['pages'] = b[3]
        book['genre'] = b[2]
        booksRefs.append(book)

    refference['books'] = booksRefs
    result.append(refference)

json_object = json.dumps(result)

with open("reference.json", "w") as outfile:
    outfile.write(json_object)
