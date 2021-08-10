### Part 1

Write a class that given a number (with arbitrary number of digits), converts it into LCD style numbers using the following format:
```
   _  _     _  _  _  _  _  
 | _| _||_||_ |_   ||_||_|  
 ||_  _|  | _||_|  ||_| _|  
````
(each digit is 3 lines high)


### Part 2

Change your program to support variable width or height of the digits.
For example for width = 3 and height = 2 the digit 2 will be:

```
 ___
    |
    |
 ___
|
|
 ___
```

### Run your code
In `number_to_lcd.py` there is a an empty class that you can use to implement the logic to print the numbers.
In `number_to_lcd.py` there are several tests that you can use to confirm to make sure your program is working.

I recommend comment out all but 1 test and try to get one test passing at a time.

You can run the tests by using the following command.
```
python test_number_to_lcd.py
```
