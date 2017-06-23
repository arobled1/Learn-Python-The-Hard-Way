def print_two(*args):
    arg1, arg2 = args
    print "arg1: %s, arg2: %s" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %s, arg2: %s" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %s" % arg1

def print_none():
    print "I got nothin'."

print_two("Alan","Robledo")
print_two_again("alan","Robledo")
print_one("First!")
print_none()

# def means to "define" a function. Don't forget the colon at the end of the
# parantheses. This is like in Mathematica when you want to make a function and
# you put a colon and an equals sign.
def print_three(arg1, arg2, arg3):
# Then you add 4 spaces and say what you want the function to do every time you
# call it. In this case, you're saying that every time you call "print_three",
# you want python to print whatever you tell it to print.
    print "%s %s %s" % (arg1, arg2, arg3)
# Then you call the function.
print_three("Alan","Is","Awesome")
