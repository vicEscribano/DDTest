CLASSES = ["Bard", "Cleric", "Rogue", "Warrior", "Druid", "Barbarian"]


def main():
    print("Welcome to your dungeon simulator")
    setup_team()


def setup_team():
    characters = []
    total_characters = int(input("How many adventurers are going to enter? "))
    for i in range(0, total_characters):
        character = dict()
        character_name = input("What is the name of character: ")
        print("Allowed classes: {classes}".format(classes=str(CLASSES)))
        character_class = input("What class of is the character: ")
        while character_class not in CLASSES:
            print("Allowed classes: {classes}".format(classes=str(CLASSES)))
            character_class = input("What class of is the character: ")
        character["name"] = character_name
        character["class"] = character_class
        characters.append(character)
    print(characters)


main()
