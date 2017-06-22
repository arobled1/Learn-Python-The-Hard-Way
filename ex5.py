name = 'Alan Robledo'
age = 20
height = 66.0 # inches
inch_to_feet = height / 12
weight = 160 # pounds
eyes = 'Brown'
teeth = 'White'
hair = 'Black'


print "Let's talk about %s." % name
# %s gives you the value you want with no rounding
print "He's %s feet tall." % inch_to_feet
# %d gives you the value you want with rounding (so you might not want it)
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, weight,
age + height + weight)
