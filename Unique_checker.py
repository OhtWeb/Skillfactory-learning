def create_unique_checker(*args):
	seen_element = set()
	def checker(*args):
		if args in seen_element:
			return False
		else:
			seen_element.add(args)
			return True
	return checker