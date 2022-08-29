
def fizzbuzz(number):
    three = number % 3
    five = number % 5
    match (three, five):
        case (0, 0):
            return "FIZZBUZZ"
        case (0, _):
            return "FIZZ"
        case (_, 0):
            return "BUZZ"
        case _:
            return number


for i in range(1, 100):
    print(fizzbuzz(i))
