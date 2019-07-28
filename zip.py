midterm = [80, 91 ,78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

#output {'dan': 98, 'ang': 91, 'kate': 78}

list1 = list(zip(midterm, finals))

list2 = [max(tup) for tup in list1]

print(dict(zip(students, list2)))


