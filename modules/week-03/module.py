# module.py

# This file has two functions and one simple class
# It's all about game characters!

def format_name(name):
    # Makes the first letter uppercase
    return name.capitalize()


def average_damage(hits):
    # Finds the average of numbers in a list
    if not hits:
        return 0
    return sum(hits) / len(hits)


class Character:
    # character with a name, level, and health

    def __init__(self, name, level):
        # character's info when it's created
        self.name = format_name(name)
        self.level = level
        self.health = 100  # All characters start with 100 health

    def attack(self):
        # 5 damage per level
        return self.level * 5

    def describe(self):
        # Shows the character's name, level, and health
        return f"{self.name} (Level {self.level}) has {self.health} HP."
