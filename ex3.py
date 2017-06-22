# Commanding python to say what I want.
print "I will now count my chickens:"
# Python obeys PEMDAS so it does 30/6 then 25 + 5.
print "Hens", 25+30/6
# The % modulus is evaluated after PEM in PEMDAS, and it works by taking the
# number on the left of the % and dividing it by the number on the right of the
# % and giving you the remainder. So 25*3%4 = 75%4 = 3 because 4 goes into 75
# 18 times which is 72 and there is a remainder of 3.
print "Roosters", 100-25*3%4
# Commanding python to say what I want.
print "Now I will count the eggs:"
# Python doesn't do fractions, so it will give you 0 for 1/4. If you do 1.0/4
# or 1/4.0, then python will give you 0.25. Notice that it still does not give
# you a fraction.
print 3+2+1-5+4%2-1/4+6
# Commanding python to say what I want.
print "Is it true that 3+2<5-7?"
# < is considered a less than sign in python, so it is doing the math and then
# evaluating whether or not 5 is less than -2, which it is not, so it tells
# you "False".
print 3+2<5-7
# Commanding python to say what I want. The comma does not appear in python, so
# it is meant to separate text from calculations. If the comma is not there,
# Python will give you a syntax error.
print "What is 3+2?"
print 3+2
# Same thing as line 25. Remember the comma.
print "What is 5-7?", 5-7
# Commanding python to say what I want.
print "Oh, that's why it's False."
# Commanding python to say what I want.
print "How about some more."
# Notice the comma again. But now Python is trying to evaluate if 5 is greater
# than -2, which it is so it tells youb "True".
print "Is it greater?", 5>-2
# Another comma incident. But now Python is trying to evaluate if 5 is greater
# than or equal to -2. It's not equal but it is greater than so Python will say
# "True".
print "Is it greater or equal?", 5>=-2
# More commas. But this time, 5 is not less than nor equal to 2, so Python says
# "False".
print "Is it less or equal?", 5<=-2
