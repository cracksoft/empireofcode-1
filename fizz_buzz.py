def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    if number % 3 == 0:
        return "Fizz"
    return "Buzz" if number % 5 == 0 else str(number)
