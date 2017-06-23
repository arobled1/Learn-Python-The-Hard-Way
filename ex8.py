# The trick to this is to notice that the variable is a string of commands %r,
formatter = "%r %r %r %r"
# and when formatter is printed, it will run the command %r 4 times, and it will
# print whatever is to the right of the percent symbol, just like before. And
# since there are 4 %r commands, there needs to be 4 strings/numbers after the
# percent symbol, which python recognizes using the ( ), just like in
# Mathematica when you use the { }.
print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
