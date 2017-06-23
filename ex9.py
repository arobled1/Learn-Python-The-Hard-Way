days = "Mon Tue Wed Thu Fri Sat Sun"
# \n is cool because it will print whatever comes after it on a "new line" and
# you do not have to use spaces. For atom, this isn't exactly efficient because
# you will then have to scroll to the right a lot to see everything you write
# if you always use \n. But it's very nice on terminal because you have all
# that extra space.
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
# Notice how a comma after a string and then the variable will make python
# print whatever is after the comma. It's the same concept as %s, as you can
# see only faster.
print "Here are the days: %s" % days
print "Here are the months: ", months
# Triple quotes let's you type however much you want without having to put
# "print" and double quotes each time.
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
