FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"
THOUSAND = "thousand"

def help(number):
    if number == 0:
        return ""
    if number < 10:
        return FIRST_TEN[number-1] + ' '
    if number < 20:
        return SECOND_TEN[number-10] + ' '
    if number < 100:
        return OTHER_TENS[(number//10)-2] + ' ' + help(number%10)
    if number < 1000:
        return help(number//100) + 'hundred ' + help(number%100)
    return help(number//1000) + 'thousand ' + help(number%1000)

def tell_number(number):
    if number == 0:
        return 'zero'
    return ('minus ' if number < 0 else '') + help(abs(number)).strip()
