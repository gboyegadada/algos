
def fizzBuzz(m, fizz, buzz):
  for n in range(1, m+1):
    # 1. If multiple of FizzBuzz
    if 0 == n % fizz == n % buzz:
      print('FizzBuzz')

    # 2. If multiple of fizz
    elif 0 == n % fizz:
      print('Fizz')

    # 3. If multiple of buzz
    elif 0 == n % buzz:
      print('Buzz')

    # 4. Not a multiple
    else:
      print(n)


fizzBuzz(15, 3, 5)


