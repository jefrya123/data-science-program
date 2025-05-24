from module import format_name, average_damage, Character

# Use the format_name function
print("Formatted name:", format_name("jeff"))  # ➜ Jeff

# Use the average_damage function
print("Average damage:", average_damage([10, 20, 30]))  # ➜ 20.0

# Make a character and show info
hero = Character("luna", 3)
print(hero.describe())              # ➜ Luna (Level 3) has 100 HP.
print("Attack Damage:", hero.attack())  # ➜ 15
