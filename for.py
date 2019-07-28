
# ========= print a diamond =============
# for x in range(1,11):
#     print("x" * ((x - 11) * -1) + " " * x * 2 + "x" * ((x - 11) * -1))

# for y in range (1,11):
#     print("x" * y  + " " * ((y - 11) * -1) * 2 + "x" * y)

# ========= print a pyramid =============

count = 0
for x in range(1,21,2):
    if x != 1:
        count += 1
    print("-" * (((x - 21) * -1) + count) + "v" * x  + "-" * (((x - 21) * -1) +count))


