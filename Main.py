import random

words = ["puzzled", "silk", "calculating", "wrong", "resonant", "resonant", "consist", "telling", "obey", "peotomy", "vallation", "essorant", "uvala", "incarnadine", "hercogamy", "hamular", "verbid", "anapeiratic", "yikker", "hyponym", "zoilism", "isotherm", "omphalopsychite", "urochs", "veduta", "bursal", "bardocucullus", "quaquaversal", "xiphopagus", "wang", "yeep", "isagogic", "wort", "falsidical", "konimeter", "item", "fissiparous", "yearling", "tromometer"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
characters = ["!", "£", "%", "$"]

while True:
        print("")

        amountin = input("How many passwords would you like to generate : ")
        amount = int(amountin)

        for i in range(amount):
                gen_password = random.choice(words) + random.choice(numbers) + random.choice(numbers) + random.choice(characters)
                gen_password = gen_password.replace("e", "3")
                gen_password = gen_password.replace("E", "3")
                gen_password = gen_password.replace("l", "1")
                gen_password = gen_password.replace("L", "1")
                print(gen_password)
