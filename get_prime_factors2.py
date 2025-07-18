def get_prime_factors(number):
	factors = []
	div = number
	n = 2
	while n <= number:
		if div % n == 0:
			factors.append(n)
			div = div // n
		else:
			n = n + 1
	return factors

# Please, uncomment the line below to execute the code with the example given
# print(get_prime_factors(60))