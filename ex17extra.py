from sys import argv;
from os.path import exists

script, orig_file, new_file = argv

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")
new = "%s\n%s\n%s" % (line1, line2, line3)

firstdata = open(orig_file, 'w')

firstdata.write(new)
firstdata.close()

seconddata = open(orig_file).read()

thirddata = open(new_file, 'w')

thirddata.write(seconddata)
thirddata.close()
