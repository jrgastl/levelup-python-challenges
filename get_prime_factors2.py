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

print(get_prime_factors(60))