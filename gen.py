


storyWithBlanks = "I used to go to %s stores with my friends. We'd take the %s into Boston, and go to The %s District, which is this huge %s warehouse. Everything is arranged by %s, and somehow that makes all of the %s %s. It's kind of like if you went through the %s in the Narnia books, only instead of finding %s and the White Witch and horrible Eustace, you found this magic %s world-instead of talking animals, there were %s boas and %s dresses and %s shoes, and %s shirts and %s and everything hung up on racks so that first you have black %s, all together, like the world's largest indoor funeral, and then blue dresses-all the blues you can imagine-and then red dresses and so on. Pink-reds and orangey reds and purple-reds and exit-light reds and candy reds. Sometimes I would close my eyes and Natasha and Natalie and Jake would drag me over to a rack, and rub a dress against my %s. \"Guess what %s this is.\""

blanks = [
    "noun",
    "noun",
    "noun",
    "noun",
    "noun",
    "noun",
    "adjective",
    "noun",
    "proper noun",
    "noun",
    "adjective",
    "adjective",
    "adjective",
    "adjective",
    "proper noun",
    "noun",
    "noun",
    "noun",
]

answers = ()

for thing in blanks:
    answer = raw_input("Give me a " + thing + ":")
    answers = answers + (answer,)


print storyWithBlanks % answers


