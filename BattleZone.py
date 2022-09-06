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
        hero_attack_phrase = random.choice(hero['phrases']['challenges'])
        villain_plea_phrase = random.choice(villain['phrases']['pleas'])
        print(hero_attack_phrase)
        print(villain_plea_phrase)
        print(f"{my_hero['name']} attacks with {first_attack[0]}! ")
        villain['health']-= first_attack[1]
        print("")

        print(f"{villain['name']} health is now at {villain['health']}")

print("")

def counter_attack(hero, villain):
        first_attack = random.choice(villain['attacks'])
        print(f"{villain['name']} attacks with {first_attack[0]}")
        hero['health']-= first_attack[1]
        print("")
        print(f"{hero['name']} is hit with {first_attack[0]} and now her health is at {hero['health']}!")

print("")

def battle_zone(hero, villain):
    while hero['health'] > 0 and villain['health'] > 0:
        attack_one(hero, villain)
        if villain['health'] > 0:
            counter_attack(hero, villain)

    if hero['health'] > 0:
        print("")
        print(f"{villain['name']}, You have been defeated!!")
        print("")
        loot_equipment(hero, villain)
        loot_coins(hero, villain)
        print(f'Thanks for the items')
        print("")

print("")

def loot_equipment(hero, villain):
        hero['equipment'].update(villain['equipment'])
        print(hero['equipment'])

print("")

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
    print('')
    print(f"Great job {my_hero['name']} You completed Level 1. Prepare for Level 2")
    print("")
    print(f"Prepare to battle {enemy_two['name']}!! ")
    print("")

    if my_hero['health'] > 0:
        battle_zone(my_hero, enemy_two) 
    elif my_hero['health'] < 0:   
        print(f"{my_hero['name']}, You have been Slayyyyyed, You Lose!!")

    if my_hero['health'] > 0:
        print(f"Congratulations, {my_hero['name']}; Level 2 completed. Prepare for Level 3")
        battle_zone(my_hero, enemy_three)  
    elif my_hero['health'] < 0:   
        print(f"{my_hero['name']}, You have been Slayyyyyed, You Lose!!")

    if my_hero['health'] > 0:   
        print(f"{my_hero['name']}, All the girls are in formation and you are the most fabulous Queen!!")
        print("")
        print("They will never Break Your Soul!!")
        print("")


run_game()

print(run_game)
