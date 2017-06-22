# "print" is used when you want python to tell you something. It's usually
# followed by single quotes or double quotes. Either can be used.

# If you want python to run a calculation, put it in front of "print" or put it
# after a comma when you're "print"ing something else.

# Variables are assigned the same way as in Mathematica.

# Functions are assigned similarly to Mathematica, except in Python, you do not
# need to put an underscore after an argument, and you only need a colon. Not
# colon and equals sign.

# You can use format characters like %r, %s, and %d to tell Python to replace a
# string or a numerical value to it whenever you add the format character. To
# use them, you place the format character wherever you'd like in your string.
# Once the string is complete, you add a percent symbol and then the arguments
# that you want to assign to the format character. One format character can
# only be used for one argument. So multiple arguments need multiple format
# characters.

# You use %r when you're debugging and Python will put whatever is in place of
# the %r with quotes when you print the script.

# You use %s when you want to print your script and have it look "normal", so
# no quotes would be used when you print your script. %s can be used in
# place of strings and numbers. Though it's safe to just use %s for strings,
# because this does not apply all the time.

# You use %d in place of numbers that you want to put it while a script is
# running, similarly to %r and %s. Strings can't be used with %d.

# \n is used when you want a new line to be made when a script is being
# printed but you do not want to go on a new line when you're making the script
# in your text editor.

# \t is used when you want there to be an indent before something when your
# script is being printed but you do not want to make the indent yourself
# when you are making the script in your text editor.

# Triple quotes can be used when you want to write multiple lines but don't want
# to keep putting quotes on each line.

# raw_input() is used when you want to manually input an argument as the script
# is being printed. This concept is heavily used in games like Zork. raw_input()
# can be used 2 ways but the easiest way is to input a string inside the ().

# You import new modules from packages by putting "from (package) import
# (modules)". We've been using argv often and we use it when we're working with
# another script or when we're using a new variable throughout a script.
# So when we're using it, we have to assign "argv" to the script that we're
# working with and something else.

# When we want to take something from a file, we open the file using the
# "open()" module and assign it to a variable, with the file name inside the
# parentheses. If we want to write on the file, we add a comma after the file
# name, followed by a 'w'. If we just want to take the contents of a file, we
# use the open() module but put a period after the end parentheses, followed by
# read(). 
