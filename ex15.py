from sys import argv
# The script is the name of the file "ex15.py" and the filename is the one we
# are trying to open which is "ex15_sample".
script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()
# This is another way to open a file. The first way is actually easier because
# we just have to type in the name of the file once and we don't have to
# deal with the raw_input command.
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
