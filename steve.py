import random
# Demo of basic input in python
# name = input("Enter your name: ")
# print("Hello " + name)

# Demo of a program that computes for an area of a circle
# radius = float(input("Enter the radius: "))
# area = 3.14 * (radius**2)
# print("The area of the Circle is: " + str(area))

# Demo of a program that computes for a volume of a cylinder
# radius = float(input("Enter the Radius: "))
# height = float(input("Enter the Height: "))
# volume = 3.14 *(radius**2 * height)
# print("The Volume of the Cylinder: " + str(volume))

#Demo for array 
# fruits = ["apple", "banana", "cherry", "strawberry", "melon", "watermelon"]
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

#Demo for for Loop
# for x in fruits:
#     print(x)

# i = 0
# while i < 10:
#     print("Hello World")
#     print(i)
#     i = i + 1



#sample text-based game with simple conditional statement
#the character and it's attribute
character_health = 100
max_health = 100
min_health = 1
character_attack = 15
character_crit_damage = character_attack * 2
danger_health = False
item = ""
inventory = ["Paladin sword","Battle Fury","Buriza do kyanon"]
character_inventory = []
cleared_bonus = ["Cyclops", "Chimera"]
monster_pet = []

name = input("Enter your name: ")
print("Hello Master " + name)

while character_health > 0:
    #healing the character
    if character_health <= max_health and item == "Fish":
        n = input("You have taken some damage to heal select [1to heal/ 0 to ignore]")
        if n == "1" and character_health < max_health:
            character_health += 50
            print("Your character's health is back to " + str(character_health))
                
        else :
             print("Your character's health is back to " + str(character_health))


    v = str(input("Choose 1 if you want to cross the river\nChoose 2 if you want to jump on the ravine\nChoose 3 if you want to fight monster in the dungeon \nInput: "))
   
    #Start of Journey
    if v == "1": 
        choice = input("If you want to go fishing select [1 for yes/ 0 for no]")
        if choice == "1":
            
            #Fishing minigame
            print("You have chosen Fishing! ")
            chance = random.randint(0,9)
            if chance < 6:
                item = "Fish"
                print("You have catch a Fish!")
            else:
                print("There is no fish to catch")

        elif choice == "0":
            print("You have crossed the river")


    elif v == "2":
        
        #damages the player
        print("You have jumped into the ravine")
        print("Your character has taken 10pt of damage")
        character_health -= 10
        
    elif v == "3":
        #Entering the dungeon
        print("You have enter the dungeon")

        #mosnters in the dungeon and it's attributes
        monster_list = ["cyclops", "chimera"]
        monster = monster_list[0]
        print("oh no a", monster + "!")
        cyclops_health = 500
        cyclops_damage = 20
        cyclops_crit_damage = cyclops_damage * 2
        chimera_health = 1000
        chimera_damage = 40
        chimera_crit_damage = chimera_damage * 2
        dungeon_cleared = False
        
        #dueling the monster inside the dungeon
        print("Starting the duel")

        while True:
            
            if danger_health == True:
                break
            
            #stops
            if dungeon_cleared == True:
                break
            
            #cyclops and attacking the character
            crit_hit = random.randint(1,50)
            if monster == "cyclops":
                if crit_hit <= 5:
                    print ("Monster Brutality Ughh!!")
                    character_health = character_health - cyclops_crit_damage            
                else:
                    print(" AHHHHHHHHHHHHH! I've been hit by cyclops.")
                    character_health = character_health - cyclops_damage
                        
                #game over
                if character_health <= 0:
                    break

                
                #gaining exp upgrading the character
                if character_health <= 30:
                    print("oh no! your character health is " + " " + str(character_health) + " " + "it is below 30!!! \nDo you want to continue or exit the dungeon press [1] to exit or press [2] to continue fighting\nWaring! If you exit the dungeon the mosnter cylops will heal.")
                    pressed = str(input())
                    if pressed == "1":
                        max_health += 25
                        character_attack += 30
                        print("You've gained some exp: max health + 25 and character attack +30\nExited the  Dungeon")
                        break
                    else:
                        continue
                    
                #attacking the cyclops
                print("press [1] to attack")
                attack = str(input())
                if attack == "1":
                    #chance of critical hit for the character
                    if crit_hit <= 2:
                        print("character crtical hit * 2 damage")
                        cyclops_health = cyclops_health - character_crit_damage
                        print("Cyclops health  is " + str(cyclops_health))       
                    else:
                        print("Attacking the cyclops")
                        cyclops_health = cyclops_health - character_attack
                        print("Cyclops health  is " + str(cyclops_health))
                        
                        
                    #defeated monster
                    if cyclops_health <= 0:
                        print(" You have defeated cyclops!\n" + " " + random.choice(inventory))
                        print("")
                        #gaining inventory
                        if "                                          Paladin sword":
                            character_inventory.append("Paladin sword")
                            character_attack += 30
                            print("                             .                                                               ")
                            print("                         /   ))     |\         )               ).                         ")
                            print("                   c--. (\  ( `.    / )  (\   ( `.     ).     ( (                         ")
                            print("                   | |   ))  ) )   ( (   `.`.  ) )    ( (      ) )                        ")
                            print("                   | |  ( ( / _..----.._  ) | ( ( _..----.._  ( (                         ")
                            print("     ,-.           | |---) V.'-------.. `-. )-/.-' ..------ `--) \._                      ")
                            print("     | /===========| |  (   |      ) ( ``-.`\/'.-''           (   ) ``-._                 ")
                            print("     | | / / / / / | |--------------------->  <-------------------------_>=-              ")
                            print("     | \===========| |                 ..-'./\.`-..                _,,-'                  ")
                            print("     `-'           | |-------._------''_.-'----`-._``------_.-----'                       ")
                            print("                   | |         ``----''            ``----''                               ")
                            print("                   | |                                                                    ")
                            print("                   c--`                                                                   ")
                            print("                                                                                          ")
                            print("                                    WEAPON ACQUIRE                                        ")
                            print("                                                                                          ")
                          
                            
                    
                            print("You gained additional attack", character_attack)
                            
                        elif "                                        Battle Fury":
                            print("You You gained additional attack", character_attack)
                           
                            
                            character_attack += 25
                            
                            character_inventory.append("Battle Fury")
                            
                        elif "                                         Buriza de Canyon":
                            character_inventory.append("Buriza De Canyon")
                            if crit_hit < 18:
                                character_crit_damage
                                


                                
                                print("You gained more chance to crit", character_damage)
                        n = str(input("Do you want to continue to clear the dungeon press [1] to continue, press [2] to exit"+" Your health is " + " "+ str(character_health) +" "+ "\n\t\t\tWarning if you exit the cyclops will respawn "))

                        #the boss
                        if n == "1":
                            print("The boss has arrived!")
                        else:
                            max_health = max_health + 50
                            character_attack = character_attack + 50
                            print("You gained the additional 50 max health and 50 additional damage")
                            break
                        
                        while n == "1":
                            
                            #boss monster
                            monster = "chimera"
        
                            #chimera attack and its chance to crit
                            crit_hit = random.randint(1,50)
                            if monster == "chimera":
                                if crit_hit <= 15:
                                    print ("Chimera Monster Brutality Ughh!!")
                                    chimera_damage * 2
                                    character_health = character_health - chimera_crit_damage
        
                                else:        
                                    character_health = character_health - chimera_damage
                                    print(" AHHHHHHHHHHHHH! I've been hit by chimera.")

                                #game over
                                if character_health <= 0:
                                    break

                                #gaining exp and upgrading  the  character  
                                if character_health <= 30:
                                    print("oh no! your character health is " + " " + str(character_health) + " " + "it is below 30, Do you want to continue or exit the dungeon press [1] to exit or press [2] to continue fighting")
                                    choice_pressed = str(input())
                                    if choice_pressed == "1":
                                        dangered_health = True
                                        max_health += 75
                                        character_attack += 70
                                        print("You've gained some exp: max health + 75 and character attack + 70\nExited the  Dungeon")
                                        break
                                    else:
                                        continue
                                #attacking the character
                                print("press [1] to attack")
                                attack = str(input())
                                if attack == "1":
                                    #chance of critical hit for the character
                                    if crit_hit <= 2:
                                        print("character crtical hit * 2 damage")
                                        chimera_health = chimera_health - character_crit_damage
                                        print("Chimera health  is " + str(chimera_health))                           
                                    else:
                                        print("Attacking the chimera")
                                        chimera_health = chimera_health - character_attack
                                        print("Chimera health  is " + str(chimera_health))
                                        
                   
                        
                                #defeated monster and dungeon cleared
                                if chimera_health <= 0:
                                    print("                    __                                           __                     ")
                                    print("                   (**)                                         (**)                     ")
                                    print("                   IIII                                         IIII                    ")
                                    print("                   ####                                         ####                   ")
                                    print("                   HHHH     Madness comes, and madness goes     HHHH                   ")
                                    print("                   HHHH    An insane place, with insane moves   HHHH                   ")
                                    print("                   ####   Battles without, for battles within   ####                   ")
                                    print("                ___IIII___        Where evil lives,          ___IIII___                ")
                                    print("             .-`_._    _._`-.      and evil rules         .-`_._    _._`-.             ")
                                    print("            |/``  .`\/`.  ``\|    Breaking them up,      |/``  .`\/`.  ``\|             ")
                                    print("            `     }    {     '  just breaking them in    `     }    {     '             ")
                                    print("                  ) () (  Quickest way out, quickest way wins  ) () (                   ")
                                    print("                  ( :: )      Never disclose, never betray     ( :: )                   ")
                                    print("                  | :: |   Cease to speak or cease to breath   | :: |                   ")
                                    print("                  | )( |        And when you kill a man,       | )( |                   ")
                                    print("                  | || |          you're a murderer            | || |                   ")
                                    print("                  | || |             Kill many                 | || |                    ")
                                    print("                  | || |        and you're a conqueror         | || |                    ")
                                    print("                  | || |        Kill them all ... Ooh..        | || |                   ")
                                    print("                  | || |           Oh you're a God!            | || |                    ")
                                    print("                  ( () )                                       ( () )                    ")
                                    print("                   \  /                                         \  /                     ")
                                    print("                    \/                                           \/                      ")
                                    print("                                                                                         ")
                                    print("                                                                                        ")
                                    print("                                                                                        ")
                                    print("                                                                                        ")
                                    print("                                                                                        ")
                                    
                            
                            

                                    
                                    print(" You have defeated chimera!\n Congratulation You cleared the dungeon")
                                    #gaining a pet
                                    print("You gained a monster pet"+ " " + random.choice(cleared_bonus))
                                    print("")
                                    print("")
                                    
                                    if "cylops":
                                        monster_pet.append("cyclops")
                                    elif "chimera":
                                        monster_pet.append("chimera")
                                    print("Exited the dungeon")
                                    dungeon_cleared = True
                                    break
                        #if exited the dungeon after defeating the cyclops gaining exp
                        else:
                            print("Exited the dungeon you gained + 50 max health and 75 additional attack damage  ")
                            max_health += 50
                            character_attack += 75
                            break 
            else:
                break
        else:
            break
    else:
        print("Invalid input")
        
    
    print("Your character's Health: " + str(character_health))
    print(monster_pet)
    
print("Your Character is dead!")
