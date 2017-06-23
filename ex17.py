from sys import argv
from os.path import exists
# Now we have 3 arguments. The script is the first one. The from_file is an
# already made .txt file. And to_file is a file that does not exist but will
# exist after using the script.
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

indata = open(from_file).read()
# len() function tells you length of a file.
print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CRTL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done!"

out_file.close()
