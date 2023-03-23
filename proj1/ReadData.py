with open("wartosci.txt", "r") as f:
    values = [[int(num) for num in line.split()] for line in f]

for row in values:
    print(row)