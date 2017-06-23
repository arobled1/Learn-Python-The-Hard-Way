# Defining a function (don't forget the colon) witand the h 2 arguments
# next 2 lines have the 4 spaces which indicate that I want something
# printed and the actual calculation to be done when I use the function.
def add(a, b):
    print "ADDING %d + %d" % (a, b)
# The return command just returns the value of a specified calculation.
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a*b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(15, 5)
height = subtract(78, 4)
weight = multiply(75, 2)
iq = divide (200, 1)

print "Age: %d, Height: %d inches, Weight: %d inches, iq: %d" % (age, height,
weight, iq)
# This is coding for 20 + (74 - (150 * (200 / 2)))
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print what

# For raw_input, I could do this:
print "Let's use our own numbers!"
print "Let's start by adding."
x = add(float(raw_input("a = ")),float(raw_input("b = ")))
