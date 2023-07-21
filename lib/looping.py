#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while(counter > 0):
        print(counter)
        counter -= 1
    print("Happy New Year!")

def square_integers(int_list):
    def squareNumber(num):
        return num*num
    result = map(squareNumber, int_list)
    return list(result)
        
# def fizzbuzz_printer():
#     for num in range(1, 100):
#         print(fizzbuzz(num))

def fizzbuzz():
    for num in range(1, 101):
        if(num % 3 == 0 and num % 5 == 0):
            print("FizzBuzz")
        elif(num % 3 == 0):
            print("Fizz")
        elif(num % 5 == 0):
            print("Buzz")
        else:
            print(num)

# /* 
#   Write a method `fizzbuzz_printer` that prints the numbers from 1 to 100. For
#   multiples of three, print "Fizz" instead of the number and for the multiples
#   of five print "Buzz". For numbers which are multiples of both three and five,
#   print "FizzBuzz".
# */
# function fizzbuzzPrinter() {
#   for (let num = 1; num <= 100; num++) {
#     console.log(fizzbuzz(num));
#   }
# }

# function fizzbuzz(num) {
#   if (num % 3 === 0 && num % 5 === 0) {
#     return "FizzBuzz";
#   } else if (num % 3 === 0) {
#     return "Fizz";
#   } else if (num % 5 === 0) {
#     return "Buzz";
#   } else {
#     return num;
#   }
# }

# /*
#   Write a method `reverse_string` that takes one argument, a string, and reverses
#   it. Don't use the built-in `.reverse` method. Instead, loop through the
#   characters in the input string and reverse it.
# */
# function reverseString(str) {
#   let reversedStr = "";
#   for (let i = 0; i < str.length; i++) {
#     reversedStr = str[i] + reversedStr;
#   }
#   return reversedStr;
# }

