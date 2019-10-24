


storyWithBlanks = "I am a %s, but I smell like a %s!"

blanks = [
    "noun",
    "noun",
]

answers = ()

for thing in blanks:
    answer = raw_input("Give me a " + thing + ":")
    answers = answers + (answer,)


print storyWithBlanks % answers


