from csv import reader

with open('quotes.csv', 'r', encoding='utf-8') as file:
    csv_reader = reader(file)
    next(csv_reader)
    stats = {}
    cleaner_stats = {}

    for row in csv_reader:
        if row[0] in stats:
            stats[row[0]] += 1
        else:
            stats[row[0]] = 1
        
    total = 0
    
    for author, num in stats.items():
        if num > 1:
            print(f'{num} quotes from {author}.')
        else:
            print(f'Only {num} quote from {author}.')
        total += num

        if num in cleaner_stats:
            cleaner_stats[num].append(author)
        else:
            cleaner_stats[num] = [author]
        
    print(total)
    for key, val in cleaner_stats.items():
        print(f'{key} quotes: {val}')

