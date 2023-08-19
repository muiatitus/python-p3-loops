#!/usr/bin/env python3

def happy_new_year():
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")

def square_integers(int_list):
    squared_list = [num ** 2 for num in int_list]
    return squared_list

def fizzbuzz():
    for num in range(1, 101):
        print(fizzbuzz_helper(num))

def fizzbuzz_helper(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
