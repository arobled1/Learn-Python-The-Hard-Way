from sys import argv

script, user_name, gf_name = argv
prompt = '* '

print "Hi %s, I'm %s, the %s script." % (user_name, gf_name, script)
print "I'd like to ask you a few questions."

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "Where would you like to take me to?"
location = raw_input(prompt)

print "Do you like me %s?" % user_name
likes = raw_input(prompt)
print """
Alright, so you live in %s. Not sure where that is.
You have a %s. You want to take me to %s.
And you said %s about liking me. How sweet!
""" % (lives, computer, location, likes)
