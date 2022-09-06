print ("Welcome to the Industry Wars")
print("")
print("Prepare for the survival of the Fabulous!!")
print("")
print("Level One: ")
print("")
from CharacterDev import my_hero, enemy_one, enemy_two, enemy_three
import random
def attack_one(hero, villain):
        first_attack = random.choice(hero['attacks'])
        print(f"{my_hero['name']} attack with {first_attack[0]}! ")
        villain['health']-= first_attack[1]
        print("")
        print(f"{villain['name']} health is now at {villain['health']}")

def counter_attack(hero, villain):
        first_attack = random.choice(villain['attacks'])
        print(f"{villain['name']} attacks with {first_attack[0]}")
        hero['health']-= first_attack[1]
        print("")
        print(f"{hero['name']} is hit with {first_attack[0]} and now her health is at {hero['health']}!")

def battle_zone(hero, villain):
    while hero['health'] > 0 and villain['health'] > 0:
        attack_one(hero, villain)
        if villain['health'] > 0:
            counter_attack(hero, villain)

    if hero['health'] > 0:
        loot_equipment(hero, villain)
        loot_coins(hero, villain)

def loot_equipment(hero, villain):
        hero['equipment'].update(villain['equipment'])
        print(hero['equipment'])
def loot_coins(hero, villain):
        hero['coins']['gold'] += villain['coins']['gold']
        print(hero['coins']['gold'])



def run_game():
    print(my_hero['name'])
    print("")
    print(f"{enemy_one['name']}: Ahhhh {my_hero['name']}, you think your are on top, but you will never defeat the {enemy_one['name']}!! ")
    print("")
    print(f"{my_hero['name']}: {enemy_one['name']}, You will never be as great as me, Ha Ha Ha!! Now prepare for your defeat... ")
    print("")

    battle_zone(my_hero, enemy_one)
    battle_zone(my_hero, enemy_two)
    battle_zone(my_hero, enemy_three)  



run_game()

print(run_game)
