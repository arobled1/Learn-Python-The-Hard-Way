# raw_input lets you type in whatever number or string you want as the file is
# being run on the terminal.
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
# Again, %r will give you raw input in single quotes, but %s will not have the
# quotes because %r is for debugging and %s is for show.
print "So you're %s, %s tall and %s heavy." % (age, height, weight)
