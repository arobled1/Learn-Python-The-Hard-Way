# We can input these logic expressions in python and python should return
# either True or False.

# We can use the True and False expressions from ex27 to predict new
# expressions ourselves.

# (1 == 1 and 2 == 1)  should give you "False" because "1 == 1" is True and
# "2 == 1" is False so you now have "True and False". By making the connection
# with boolean algebra, as explained in ex27, we should get False.

# ("chunky" == "bacon" and (not(3 == 4 or 3 == 3))) should give you False
# because if we start with (3 == 4 or 3 == 3), we have (False or True), which
# should give you True. Then we have not(True), which should give you False.
# So we now have False and False, which is False.
