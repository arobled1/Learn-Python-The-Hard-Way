def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly."
cheese_and_crackers(20,30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10+20,5+6)



print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def women_and_men(number_of_men,number_of_women):
    print "There are %d men and %d women at the party!" % (number_of_men,
    number_of_women)
    
women_and_men(20,30)
women_and_men(10+20,30+10)
number_of_men = 10
number_of_women = 20
women_and_men(number_of_men+10, number_of_women+10)
women_and_men(number_of_men, number_of_women)
