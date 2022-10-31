import math
def greet():
    name = input('hello what is your name?')
    age = int(input('how old are you?'))
    if age < 18:
        grad = input("what grade are you?")
    
    elif age > 18:
        print ("you are a man")

    print(f"hello {name}")

#greet()


def paint_calc():
    number_of_cans = math.ceil((test_h * test_w) / coverage)
    print(f"You'll need {number_of_cans} cans of paint") 
    
test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5
paint_calc()


