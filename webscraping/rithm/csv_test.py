from csv import reader


with open('article.csv', 'r') as file:
    csv_reader = reader(file)
    next(csv_reader)
    for row in csv_reader:
        print(row[0],row[1],row[2])