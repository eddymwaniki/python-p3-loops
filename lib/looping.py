#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter > 0 :
        print(counter)
        counter -= 1
        print("Happy New Year!")
    pass

def square_integers(int_list):
   return [squares ** 2 for squares in int_list]
   pass

def fizzbuzz():
    for num in range(1, 101) :
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")   
        elif  num % 3 == 0 :
           print("Fizz")  
        else :
            print(num)

    pass
