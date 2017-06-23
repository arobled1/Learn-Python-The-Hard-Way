# The %d means that python will print whatever number is next to the percent
# symbol after the sentence is done.
x = "There are %d types of people." % 10
# binary is the variable and "binary" is the value assigned to the variable
binary = "binary"
do_not = "don't"
# The parantheses are used to say that multiple arguments are being called, just
# like in Mathematica, where you need to use the { }. In python, it's ( ).
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
# Not sure what %r does yet.
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evlauation = "Isn't that joke so funny?! %r"

print joke_evlauation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e


print "I am %d years old." % 20
