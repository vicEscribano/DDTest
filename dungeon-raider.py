CLASSES = {
    "Bard": {"HP": 8, "DG": 2, },
    "Cleric": {"HP": 10, "DG": 2, },
    "Rogue": {"HP": 6, "DG": 3, },
    "Warrior": {"HP": 10, "DG": 3, },
    "Druid": {"HP": 12, "DG": 2, },
    "Barbarian": {"HP": 10, "DG": 4, }
}
CLASSES_NAMES = ""

for key in CLASSES.keys():
    CLASSES_NAMES += "%s, " % key

CLASSES_NAMES = CLASSES_NAMES[:-2]

KOBOLD = {"HP": 3, "DG": 1}


def main():
    print("Welcome to your dungeon simulator")

def adventurers():
    adventurers = int(input("How many adventurers go to play?"))
    for number in range(0,adventurers):
        name = input("What is your name?")
        if len(name) >= 1 :
          job = clase()
        else:
            print("Try again")
        return adventurers
        return name


def clase():
    clase = input("What is your class?")
    while clase not in CLASSES:
        print("Try again")
        clase = input("What is your class?")
    return clase














    # You need to write a function. What recieve a number of adventurers. After you need to ask many times
    # as adventurers his name and his class. If his class is not allowed you need to ask again. The function need to
    # return the list of adventurers

    # You need to write a function. As input recieve the list of adventurers and update each adventurer
    # with his HP and DG determinated by his class.

    # Our adventures needs to fight with the same number of kobolds. Write a function that recieve the number of
    # adventurers and return a list of kobolds.

    # Create a function what recieve a list of kobolds and a list of adventurers. While a kobold still alive the
    # adventurers will atack them. If the HP of the kobold reach zero or below the kobold die.

main()
