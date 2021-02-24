for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        print("FizzBuzzBang")
        
    elif i % 3 == 0 and i % 7 == 0:
        print("FizzBang")
        
    elif i % 5 == 0 and i % 7 == 0:
        print("BuzzBang")
       
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        
    elif i % 3 == 0:
        print("Fizz")
        
    elif i % 5 == 0:
        print("Buzz")
        
    elif i % 7 == 0:
        print("Bang")
    else: 
        print(i)
