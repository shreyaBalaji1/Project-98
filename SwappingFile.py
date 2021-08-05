file1 = "textSample1.txt"
file2 = "textSample2.txt"

with open(file1, 'r') as a:
    data_a = a.read()

with open(file2, 'r') as b:
    data_b = b.read()

with open(file1, 'w') as y:
    y.write(data_b)

with open(file2, 'w') as z:
    z.write(data_a)