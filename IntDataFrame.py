class IntDataFrame:
    def __init__(self, numbers):
        self.column = [int(x) for x in numbers]

    def count(self):
        return len([x for x in self.column if x != 0])

    def unique(self):
        return len(set(self.column))

df = IntDataFrame([4.7, 4, 3, 0, 2.4, 0.3, 4])

print(df.column)
    # [4, 4, 3, 0, 2, 0, 4]

print(df.count())
    # 5

print(df.unique())
    # 4
