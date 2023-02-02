
def fizzBuzz(n, fizz, buzz):
    # 1. If multiple of FizzBuzz
    if 0 == n % fizz == n % buzz:
      n = 'FizzBuzz'

    # 2. If multiple of fizz
    elif 0 == n % fizz:
      n = 'Fizz'

    # 3. If multiple of buzz
    elif 0 == n % buzz:
      n = 'Buzz'

    # 4. Not a multiple so do nothing
    else:
      n = str(n)

    return n


nums = [fizzBuzz(n, 3, 5) for n in range(1, 100+1)]
print(', '.join(nums))


