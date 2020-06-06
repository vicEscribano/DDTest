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
    characters = setup_team()
    # Our adventures needs to fight with the same number of kobolds.
    setup_characters(characters)
    # Now assign their DG and their HP for any adventurer
    # Create any number of kobolds needed
    n_kobolds = len(characters)
    kobolds = setup_kobolds(len(characters))
    # Figth one by one the kobold. The Kobold die if their HP reach 0 else the do damage to the adventurer
    fight(characters, kobolds)


def fight(characters, kobolds):
    while len(kobolds) > 0:
        print("\n")
        print("---------------------------------------------------------------")
        for kobold in kobolds:
            print("Remaining kobolds {n_kobolds}".format(n_kobolds=len(kobolds)))
            kobold_is_alive = True
            for adventurer in characters:
                print("The adventurer {name} damage the kobold".format(name=adventurer["name"]))
                life = kobold["HP"] - adventurer["DG"]
                if life <= 0 and kobold_is_alive:
                    print("The kobold die")
                    kobold_is_alive = False
                    kobolds.remove(kobold)
                else:
                    print("The kobold still alive")
                    kobold["HP"] = life
        input("Press enter to next round")


def setup_team():
    characters = []
    total_characters = int(input("How many adventurers are going to enter? "))
    for i in range(0, total_characters):
        character = dict()
        character_name = input("What is the name of character: ")
        print("Allowed classes: {classes}".format(classes=CLASSES_NAMES))
        character_class = input("What class of is the character: ")
        while character_class not in CLASSES:
            print("Allowed classes: {classes}".format(classes=CLASSES_NAMES))
            character_class = input("What class of is the character: ")
        character["name"] = character_name
        character["profession"] = character_class
        characters.append(character)
    for character in characters:
        print("Name: {name} Class: {profession}".format(name=character["name"], profession=character["profession"]))
    return characters


def setup_kobolds(n_kobolds):
    kobolds = []
    for x in range(0, n_kobolds):
        kobolds.append(KOBOLD)
    return kobolds


def setup_characters(characters):
    for character in characters:
        # Get their class
        profession = CLASSES[character["profession"]]
        # Setup their DM and their HP
        character["HP"] = profession["HP"]
        character["DG"] = profession["DG"]
    return characters


main()
