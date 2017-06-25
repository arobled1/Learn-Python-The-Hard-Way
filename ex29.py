people = 20
cats = 30
dogs = 15

# The if-statement is used to check the conditions specified in the
# statement and then have the script run depending on the statement.
# If you don't have the 4 spaces underneath the if-statement, you will get an
# indentation error.
if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"


dogs += 5
# Using "+=" in this case is like saying "dogs = dogs + 5" and it's called the
# "increment by" operator. So since dogs was originally 15, it is now
# considered to be 20, the same value as "people". So all 3 statements should
# be printed when you run the script.
if people >= dogs:
    print "People are greater than or equal to dogs!"

if people <= dogs:
    print "People are less than or equal to dogs."


if people == dogs:
    print "People are dogs."
