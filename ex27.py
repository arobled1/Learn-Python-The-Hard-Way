# Disclaimer: This is just what I made up to memorize logic statments.

# When memorizing logic statements, it is easier to memorize them with a little
# bit of boolean algebra. In boolean algebra, we only deal with adding and
# multiplying ones and zeros. Some useful equations to remember from boolean
# algebra are:
# 0 + 0 = 0
# 1 + 0 = 1
# 0 + 1 = 1
# 1 + 1 = 1

# The first 3 equations seem obvious because that's elementary school math.
# But in boolean algebra, that kind of math is thrown out the window. Instead,
# we have to consider the idea that any number other than 1 or 0 does not
# exist. If we consider zero to be a number that has no value, then, by logic,
# any equation that does not look like it'll be 0, will be 1. So for the 4th
# equation, since 1 + 1 does not give you nothing, it must give you something,
# so it should be 1. It's just as weird as modular arithmetic where
# (1 + 1) modulo 2 = 0. But it's cool!


# To remember True and False statements with "or" in between, if we think of
# True as the number 1, False as the number 0, and "or" as a plus, then we can
# apply the 4 equations from boolean algebra.
# (False or False)  False
# (True or False)   True
# (False or True)   True
# (True or True)    True

# To remember True and False statements with "and" in between, if we think of
# False as the number 1, True as the number 0, and "and" as a plus, then we
# can again apply the 4 equations from boolean algebra.
# (True and True)    True
# (False and True)   False
# (True and False)   False
# (False and False)  False

# Statements with "not" just means to take the opposite of whatever is inside
# the "not". Remember that the only responses are either True or False.
# (not(True or False)) False
# (not(True or True))  False
# (not(False or False)) True

# =! is the same as "not equal to"

# == is the same as "equal to"

# >= is the same as "greater than or equal to"

# <= is the same as "less than or equal to"
