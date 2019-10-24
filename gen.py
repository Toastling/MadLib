


storyWithBlanks = "I have quite a collection of %s in my %s. My %s is very angry about it. He says to me that I should have a collection of %s instead. I think he is %s and should be sent back.\""

blanks = [
    "noun",
    "place",
    "animal",
    "food",
    "adjective",
]

answers = ()

for thing in blanks:
    answer = raw_input("Give me a " + thing + ":")
    answers = answers + (answer,)


print storyWithBlanks % answers


