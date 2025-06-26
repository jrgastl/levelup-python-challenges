from random import randint

def is_prime(value):
    if value <= 1:
        return False
    for x in range(2, value):
        if value % x == 0:
            return False
    return True

def get_prime_factors(number):
    primeNumbers = [y for y in range(2, number) if is_prime(y)]
    primeFactors = []
    dividend = number
    if is_prime(number) == False and number > 1 and type(number) == int:
        while dividend > 1:       
            for n in primeNumbers:
                if dividend % n == 0:
                    primeFactors.append(n)
                    dividend /= n
            primeFactors.sort()          
    else:
        if number > 1 and type(number) == int:
            primeFactors.append(number)
        else:
            return "Number must be bigger than 1 and an integer"

    return primeFactors
    
def test_result(factors):
    result = 1
    for num in factors:
        result *= num
    return result
        
    
r = randint(2,10000)
result = get_prime_factors(r)
testedResult = test_result(result)
print(f'For the number {r} the prime factors are {result}')
if r == testedResult:
    print("Result is valid!")
else:
    print("Result is not valid!")