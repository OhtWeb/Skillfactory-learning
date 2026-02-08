multipl = 1
for i in range(10):
    if i % 2 == 0:
        continue
    multipl *= i
print(multipl)