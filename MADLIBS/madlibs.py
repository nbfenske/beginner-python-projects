# Objective: Create a script which implements the basic functionality of the madlibs game
#            This means we will have to take advantage of string concatenation to fill in the blanks of our "script".

# suppose we want to print the string "buy beats from ________"
producer = "DIRTBOYSTUNNA.com" # some string

# implementations
print("buy beats from " + producer)
print("buy beats from {}".format(producer))
print(f"buy beats from {producer}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
job = input("Job: ")

madlib = f"Programming is so {adj}! I'm always happy because I love to {verb1}. Stay hydrated and {verb2} like you're a {job}!"

print(madlib)