for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        print("FizzBuzzBang")
        continue
    if i % 3 == 0 and i % 7 == 0:
        print("FizzBang")
        continue
    if i % 5 == 0 and i % 7 == 0:
        print("BuzzBang")
        continue
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    elif i % 7 == 0:
        print("Bang")
        continue
    print(i)
