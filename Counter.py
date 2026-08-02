def create_counter(param):
	count = param
	def counter():
		nonlocal count
		count += 1
		return count
	return counter

counter = create_counter(0)
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())