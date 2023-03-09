#!/usr/bin/env python
# coding: utf-8

# # In Class Assignment #3: 
# # Teachings of the Deadly Dragon

# Build a treasure map by hiding a treasure in Middle Earth (From Lord of The Rings).
# 
# Choose any start location you would like and build a path for your adventurer (user).
# 
# ## You Must:
# 1. Encompass your WHOLE game in a LOOP and allows the adventurer to attempt the adventure again if they fail in their journey. 
# 2. Save the adventurer's progress each loop in a dictionary.
# e.g.  {Step 1: "user goes north from gondor to rohan", Step 2: "user digs to find treasure"}
# 3. Create a path for the adventurer to interact with using INPUT statements within IF/ELIF/ELSE statements
# 4. Use At least *2* IF statements, *2* ELIF statements, and *1* else statement\

# In[ ]:


weaponChoice = 0
playerChoice = 0
progressChoice = 0


print("                   ,     \    /      ,            ")       
print("                  / \    )\__/(     / \           ")
print("                 /   \  (_\  /_)   /   \          ")
print("            ____/_____\__\@  @/___/_____\____     ")
print("           |             |\../|              |    ")
print("           |              \VV/               |    ")
print("           | тєα¢нιиgѕ σf тнє ∂єα∂ℓу ∂яαgσи  |    ")
print("           |_________________________________|    ")
print("            |    /\ /      ))       \ /\    |     ")
print("            |   /  V        ))       V  \   |     ")
print("                  ᴀ ᴛᴇxᴛ-ʙᴀꜱᴇᴅ ɢᴀᴍᴇ             ")
print("                   ᴠᴇʀꜱɪᴏɴ 1.0.0.0                  ")
print("                   ꜱᴀɢᴇ ʜᴏᴇᴘꜰʟ 2023                     ")
print("")
print("")

#Choosing character

p = {}

print("Hello adventurer! Please select your character!")
playerChoice = int(input("[̲̅1̲̅] Sassy Wizard [̲̅2̲̅] Curious Elf [̲̅3̲̅] Built Orgre: "))
if playerChoice == 1:
    print(r"                            .")
    print(r"")
    print(r"                             .")
    print(r"                   /^\     .")
    print(r"              /\   'V'")
    print(r"             /__\   I      O  o")
    print(r"            //..\\  I     .")
    print(r"            \].`[/  I")
    print(r"            /l\/j\  (]    .  O")
    print(r"           /. ~~ ,\/I          .")
    print(r"           \\L__j^\/I       o")
    print(r"            \/--v}  I     o   .")
    print(r"            |    |  I   _________")
    print(r"            |    |  I c(`       ')o")
    print(r"            |    l  I   \.     ,/")
    print(r"          _/j  L l\_!  _//^---^\\_  ")
    print("")
    print("\nOhhh so you're sassy... Anyways, welcome Wizard")


    p["Player Choice"] = "Sassy Wizard"
        
elif playerChoice == 2:
    print("                           ,`-.")
    print("                         ,'   |")
    print("                       ,'     |")
    print("                     ,'       :")
    print("                   ,<\        |")
    print("                 ,' //         .")
    print("               ,' ,'/          :")
    print("             ,'  /,'           |")
    print("            /._,'/             |")
    print("           /.__,'              |")
    print("          /                    |")
    print("       .-'                     |")
    print("       '.                      |")
    print("         |`-._          ,      |")
    print("         ; -. `-.     ,'|      :")
    print("        / |@)\  |   ,', ;      '")
    print("       /        |  : /| |     |")
    print("      /         |  |: | |     :")
    print("    ,'          |  |'-' ;     |")
    print("   |   .      ,'`._|   /-._   `")
    print("   `-.\ )   ,'       -'    `-,-'")
    print("      |    :                :")
    print("      ;._                   |")
    print("      \__`.         )       |")
    print("      /_         ,-'        |")
    print("     ,'       ,-'           |")
    print("    (     _,-'\             |")
    print("     `._,'     :            | ")
    print("               '")
    print("")
    print("\nYou know... curiousity kills the cat right? Good thing you are not a cat. Welcome Elf!")

    
    p["Player Choice"] = "Curious Elf"

elif playerChoice == 3:
    print(r"""
                           __,='`````'=/__
                          '//  (o) \(o) \ `'         _,-,
                          //|     ,_)   (`\      ,-'`_,-\
                        ,-~~~\  `'==='  /-,      \==```` \__
                       /        `----'     `\     \       \/
                    ,-`                  ,   \  ,.-\       \
                   /      ,               \,-`\`_,-`\_,..--'\
                  ,`    ,/,              ,>,   )     \--`````\
                  (      `\`---'`  `-,-'`_,<   \      \_,.--'`
                   `.      `--. _,-'`_,-`  |    \
                    [`-.___   <`_,-'`------(    /
                    (`` _,-\   \ --`````````|--`
                     >-`_,-`\,-` ,          |
                   <`_,'     ,  /\          /
                    `  \/\,-/ `/  \/`\_/V\_/
                       (  ._. )    ( .__. )
                       |      |    |      |
                        \,---_|    |_---./
                        ooOO(_)    (_)OOoo\)
                        
                        """)
    print("\nYou lift bro? Welcome Ogre!")
    
    p["Player Choice"] = "Ogre"
    
else:
    print("\nAre you dumb? You need to pick either 1, 2, or 3. That simple.")


while True:
#Choosing weapon

    print("\nGood job selecting your character. The next choice... Better choose wisely.")

    print("\nTime to choose your weapon!")

    weaponChoice = int(input("\n[̲̅1̲̅] Bow & Arrow [̲̅2̲̅] Magic [̲̅3̲̅] Two Small Swords: "))
    if weaponChoice == 1:
        print(r"""
                                4$$-.                               
                               4   ".                                        
                               4    ^.                                       
                               4     $                                       
                               4     'b                                      
                               4      "b.                                    
                               4        $                                    
                               4        $r                                   
                               4        $F                                   
                    -$b========4========$b====*P=-                           
                               4       *$$F                                  
                               4        $$"                                  
                               4       .$F                                   
                               4       dP                                    
                               4      F                                      
                               4     @                                       
                               4    .                                        
                               J.  @                                          
                              '$$    
        """)
        print("\nGoing with the classics, I see. Welcome Archer.")

        p["Weapon Choice"] = "Bow & Arrow"
    elif weaponChoice == 2:
        print(r"""
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠠⡶⠄⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⣷⣧⣀⠀⠀⠀⠀⠐⣤⡴⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⡀⡀⠀⠀⠀⠈⢹⠋⠁
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢻⠓⠀⠸⡮⠄⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⢲⠈⠀⠀⢀⠀⠀⠀⠼⡮
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣇⠔⠁⠀⠠⢷⠯⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⡔⢁⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """)
        print("\nYou gonna show me a card trick? Just kidding. Welcome Magican.")
        p["Weapon Choice"] = "Magic"
        
    elif weaponChoice == 3:
        print(r"""
                           /\                                                 /\
                 _         )( ______________________   ______________________ )(         _
                (_)///////(**)______________________> <______________________(**)\\\\\\\(_)
                           )(                                                 )(
                           \/                                                 \/
        """)
        print("\nYou got some strength, hm? We'll see. Welcome Swordsperson.")
        p["Weapon Choice"] = "Two Small Swords"
        
    else:
        print("\nYou need to pick either 1, 2, or 3. That simple.")

#First task with Archer


    if weaponChoice == 1:
        print("\nAlright Archer. The Superior Court of Archer's has given you a young Archer to teach.")
        print("\nAfter working with the young Archer for some time,")
        print("the Archer asks you to teach them a deadly trick.")
        print("\nWhat will you do? ")
        progressChoice = int(input("[̲̅1̲̅] Teach them the trick [̲̅2̲̅] Do not teach them the trick: "))
        if progressChoice == 1:
            print(r"""

                            ░░░░░░░░░░░░▄▄░░░░░░░░░
                            ░░░░░░░░░░░█░░█░░░░░░░░
                            ░░░░░░░░░░░█░░█░░░░░░░░
                            ░░░░░░░░░░█░░░█░░░░░░░░
                            ░░░░░░░░░█░░░░█░░░░░░░░
                            ███████▄▄█░░░░░██████▄░░
                            ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                            ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                            ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                            ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                            ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                            ▓▓▓▓▓▓█████░░░░░░░░░█░░
                            ██████▀░░░░▀▀██████▀░░░░
                """)
            print("\nCongrats you know how to teach. The young Archer respects you more.")
            p["Progress Choice 1"] = "Team them a trick"

#Second task with Archer

            print("\nThe young Archer would like to go stake out a Dragon with you. ")
            print("\nWhat will you do?")
            progressChoice = int(input("[̲̅3] Go with them [̲̅4] You don't trust them enough. You go by yourself: "))
            if progressChoice == 3:
                print(r"""

                                ░░░░░░░░░░░░▄▄░░░░░░░░░
                                ░░░░░░░░░░░█░░█░░░░░░░░
                                ░░░░░░░░░░░█░░█░░░░░░░░
                                ░░░░░░░░░░█░░░█░░░░░░░░
                                ░░░░░░░░░█░░░░█░░░░░░░░
                                ███████▄▄█░░░░░██████▄░░
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                                ▓▓▓▓▓▓█████░░░░░░░░░█░░
                                ██████▀░░░░▀▀██████▀░░░░
                    """)
                print("\nCongrats you and the young Archer slayed the dragon!")
                p["Progress Choice 2"] = "Go with them to slay dragon"

#Third task with Archer   

                print("\nGreat. You have trained the Archer.")
                print("\nDo you think they're ready to showcase their skills to the Superior Court of Archer's?")
                progressChoice = int(input("[̲̅5] Showcase their skills [̲̅6] They're not ready: "))
                if progressChoice == 6:
                    print("\nThe Archer's thank you for your honesty.")
                    print("The young Archer learns new tricks and eventually becomes a great Archer of the land.")
                    print(r"""

                            ░░░░░░░░░░░░▄▄░░░░░░░░░
                            ░░░░░░░░░░░█░░█░░░░░░░░
                            ░░░░░░░░░░░█░░█░░░░░░░░
                            ░░░░░░░░░░█░░░█░░░░░░░░
                            ░░░░░░░░░█░░░░█░░░░░░░░
                            ███████▄▄█░░░░░██████▄░░
                            ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                            ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                            ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                            ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                            ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                            ▓▓▓▓▓▓█████░░░░░░░░░█░░
                            ██████▀░░░░▀▀██████▀░░░░
                            """""")
""")
                    print(" \nＹФＵ ＷＩＮ ")
                    print(" \nＧＡＭＥ ФＶＥＲ ")
                    p["Progress Choice 3"] = "YOU WIN"
                    break
        elif progressChoice == 2: 
            print("\nThe young archer gets mad at you and kills you. Bye Bye!")
            print(r"""
                                ███████▄▄███████████▄
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓███░░░░░░░░░░░░█
                                ██████▀░░█░░░░██████▀
                                ░░░░░░░░░█░░░░█
                                ░░░░░░░░░░█░░░█
                                ░░░░░░░░░░░█░░█
                                ░░░░░░░░░░░█░░█
                                ░░░░░░░░░░░░▀▀ 
            """)
            print(" \nＹФＵ ＬФＳＥ ")
            print(" \nＧＡＭＥ ФＶＥＲ ")
            print("\nHey! You're Awake!!")
            p["Progress Choice 1"] = "YOU LOSE"
        else:
            progressChoice = 0

    if progressChoice == 4:
        print("\nYour arrogance has cost you your life. Bye Bye!")
        print(r"""
                                ███████▄▄███████████▄
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓███░░░░░░░░░░░░█
                                ██████▀░░█░░░░██████▀
                                ░░░░░░░░░█░░░░█
                                ░░░░░░░░░░█░░░█
                                ░░░░░░░░░░░█░░█
                                ░░░░░░░░░░░█░░█
                                ░░░░░░░░░░░░▀▀ 
            """)
        print(" \nＹФＵ ＬФＳＥ ")
        print(" \nＧＡＭＥ ФＶＥＲ ")
        print("\nHey! You're Awake!!")
        p["Progress Choice 2"] = "YOU LOSE"
        progressChoice = 0

    if progressChoice == 5:
        print("\nThe young Archer fails at the test and the Superior Court of Archers kill you. Bye Bye!")
        print(r"""
                                ███████▄▄███████████▄
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓███░░░░░░░░░░░░█
                                ██████▀░░█░░░░██████▀
                                ░░░░░░░░░█░░░░█
                                ░░░░░░░░░░█░░░█
                                ░░░░░░░░░░░█░░█
                                ░░░░░░░░░░░█░░█
                                ░░░░░░░░░░░░▀▀ 
            """)
        print(" \nＹФＵ ＬФＳＥ ")
        print(" \nＧＡＭＥ ФＶＥＲ ")
        print("\nHey! You're Awake!!")
        p["Progress Choice 3"] = "YOU LOSE"
        progressChoice = 0


#First task with Magican         


    elif weaponChoice == 2:
        print("\nAlright Magican. The Superior Court of Magican's has given you a young Magican to teach.")
        print("\nAfter working with the young Magican for some time,")
        print("the Magican asks you to teach them a deadly trick.")
        print("\nWhat will you do? ")
        progressChoice = int(input("[̲̅1̲̅] Teach them a potion instead [̲̅2̲̅] Teach them the trick: "))
        if progressChoice == 1:
            print(r"""

                            ░░░░░░░░░░░░▄▄░░░░░░░░░
                            ░░░░░░░░░░░█░░█░░░░░░░░
                            ░░░░░░░░░░░█░░█░░░░░░░░
                            ░░░░░░░░░░█░░░█░░░░░░░░
                            ░░░░░░░░░█░░░░█░░░░░░░░
                            ███████▄▄█░░░░░██████▄░░
                            ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                            ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                            ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                            ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                            ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                            ▓▓▓▓▓▓█████░░░░░░░░░█░░
                            ██████▀░░░░▀▀██████▀░░░░
                """)
            print("\nCongrats the potion was great for the young Magican's level of skill.")
            p["Progress Choice 1"] = "Team them the potion"

#Second task with Magican

            print("\nThe young Magican would like to go kill a Dragon with you. ")
            print("\nWhat will you do?")
            progressChoice = int(input("[̲̅3] You don't trust them enough. You go by yourself [̲̅4] Go with them : "))
            if progressChoice == 4:
                print(r"""

                                ░░░░░░░░░░░░▄▄░░░░░░░░░
                                ░░░░░░░░░░░█░░█░░░░░░░░
                                ░░░░░░░░░░░█░░█░░░░░░░░
                                ░░░░░░░░░░█░░░█░░░░░░░░
                                ░░░░░░░░░█░░░░█░░░░░░░░
                                ███████▄▄█░░░░░██████▄░░
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                                ▓▓▓▓▓▓█████░░░░░░░░░█░░
                                ██████▀░░░░▀▀██████▀░░░░
                    """)
                print("\nCongrats you and the young Magican slayed the dragon!")
                p["Progress Choice 2"] = "Go with them"
#Third task with Magican   

                print("\nGreat. You have trained the Magican.")
                print("\nDo you think they're ready to showcase their skills to the Superior Court of Magican's?")
                progressChoice = int(input("[̲̅5] Showcase their skills [̲̅6] They're not ready: "))
                if progressChoice == 5:
                    print(r"""

                                    ░░░░░░░░░░░░▄▄░░░░░░░░░
                                    ░░░░░░░░░░░█░░█░░░░░░░░
                                    ░░░░░░░░░░░█░░█░░░░░░░░
                                    ░░░░░░░░░░█░░░█░░░░░░░░
                                    ░░░░░░░░░█░░░░█░░░░░░░░
                                    ███████▄▄█░░░░░██████▄░░
                                    ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                                    ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                                    ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                                    ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                                    ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                                    ▓▓▓▓▓▓█████░░░░░░░░░█░░
                                    ██████▀░░░░▀▀██████▀░░░░
                        """)
                    print("\nThe young Magican woos the superior Magican's.")
                    print("The young Magican becomes a great Magican of the land")
                    print(" \nＹФＵ ＷＩＮ ")
                    print(" \nＧＡＭＥ ФＶＥＲ ")
                    p["Progress Choice 3"] = "YOU WIN"
                    break
        elif progressChoice == 2: 
            print("\nThe young Magican wants to be the best and kills you with the deadly trick. Bye Bye!")
            print(r"""
                                ███████▄▄███████████▄
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓███░░░░░░░░░░░░█
                                ██████▀░░█░░░░██████▀
                                ░░░░░░░░░█░░░░█
                                ░░░░░░░░░░█░░░█
                                ░░░░░░░░░░░█░░█
                                ░░░░░░░░░░░█░░█
                                ░░░░░░░░░░░░▀▀ 
            """)
            print(" \nＹФＵ ＬФＳＥ ")
            print(" \nＧＡＭＥ ФＶＥＲ ")
            print("\nHey! You're Awake!!")
            p["Progress Choice 1"] = "YOU LOSE"
        else:
            progressChoice = 0

    if progressChoice == 3:
        print("\nYour arrogance has cost you your life. Bye Bye!")
        print(r"""
                                ███████▄▄███████████▄
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓███░░░░░░░░░░░░█
                                ██████▀░░█░░░░██████▀
                                ░░░░░░░░░█░░░░█
                                ░░░░░░░░░░█░░░█
                                ░░░░░░░░░░░█░░█
                                ░░░░░░░░░░░█░░█
                                ░░░░░░░░░░░░▀▀ 
            """)
        print(" \nＹФＵ ＬФＳＥ ")
        print(" \nＧＡＭＥ ФＶＥＲ ")
        print("\nHey! You're Awake!!")
        progressChoice = 0
        p["Progress Choice 2"] = "YOU LOSE"
    if progressChoice == 6:
        print("\nThe superior court of Magican's kill you as they see you as an unworthy teacher.")
        print(r"""
                                ███████▄▄███████████▄
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓███░░░░░░░░░░░░█
                                ██████▀░░█░░░░██████▀
                                ░░░░░░░░░█░░░░█
                                ░░░░░░░░░░█░░░█
                                ░░░░░░░░░░░█░░█
                                ░░░░░░░░░░░█░░█
                                ░░░░░░░░░░░░▀▀ 
            """)
        print(" \nＹФＵ ＬФＳＥ ")
        print(" \nＧＡＭＥ ФＶＥＲ ")
        print("\nHey! You're Awake!!")
        progressChoice = 0
        p["Progress Choice 3"] = "YOU LOSE"


#First task with Swordsperson        


    elif weaponChoice == 3:
        print("\nAlright Swordsperson. The Superior Court of Swordsmen's has given you a young Swordwoman to teach.")
        print("\nAfter working with the young Swordwoman for some time,")
        print("the Swordwoman asks you to teach her a deadly trick.")
        print("\nWhat will you do? ")
        progressChoice = int(input("[̲̅1̲̅] Teach them the trick [̲̅2̲̅] Teach them the textbook verison instead: "))
        if progressChoice == 1:
            print(r"""

                            ░░░░░░░░░░░░▄▄░░░░░░░░░
                            ░░░░░░░░░░░█░░█░░░░░░░░
                            ░░░░░░░░░░░█░░█░░░░░░░░
                            ░░░░░░░░░░█░░░█░░░░░░░░
                            ░░░░░░░░░█░░░░█░░░░░░░░
                            ███████▄▄█░░░░░██████▄░░
                            ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                            ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                            ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                            ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                            ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                            ▓▓▓▓▓▓█████░░░░░░░░░█░░
                            ██████▀░░░░▀▀██████▀░░░░
                """)
            print("\nCongrats the Swordswoman is more equipped for battle due to your trust.")
            p["Progress Choice 1"] = "Teach them the trick"

#Second task with Swordsperson

            print("\nThe young Swordsman would like to go kill a Dragon with you. ")
            print("\nWhat will you do?")
            progressChoice = int(input("[̲̅3] You go with the young Swordswoman to kill the dragon. [̲̅4] Let them do it by themselves: "))
            if progressChoice == 3:
                print(r"""

                                ░░░░░░░░░░░░▄▄░░░░░░░░░
                                ░░░░░░░░░░░█░░█░░░░░░░░
                                ░░░░░░░░░░░█░░█░░░░░░░░
                                ░░░░░░░░░░█░░░█░░░░░░░░
                                ░░░░░░░░░█░░░░█░░░░░░░░
                                ███████▄▄█░░░░░██████▄░░
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                                ▓▓▓▓▓▓█████░░░░░░░░░█░░
                                ██████▀░░░░▀▀██████▀░░░░
                    """)
                print("\nCongrats you and the young Magican slayed the dragon!")
                p["Progress Choice 2"] = "Go with them to slay the dragon"

#Third task with Swordsperson   

                print("\nGreat. You have trained the Swordswoman.")
                print("\nDo you think they're ready to showcase their skills to the Superior Court of Swordsmen's?")
                progressChoice = int(input("[̲̅5] They're not ready [̲̅6] Showcase their skills: "))
                if progressChoice == 6:
                    print(r"""

                ░░░░░░░░░░░░▄▄░░░░░░░░░
                ░░░░░░░░░░░█░░█░░░░░░░░
                ░░░░░░░░░░░█░░█░░░░░░░░
                ░░░░░░░░░░█░░░█░░░░░░░░
                ░░░░░░░░░█░░░░█░░░░░░░░
                ███████▄▄█░░░░░██████▄░░
                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█░
                ▓▓▓▓▓▓█████░░░░░░░░░█░░
                ██████▀░░░░▀▀██████▀░░░░
    """)
                    print("\nThe young Swordswoman woos the superior Swordmen.")
                    print("The young Swordwoman becomes a great Swordswoman of the land")
                    print(" \nＹФＵ ＷＩＮ ")
                    print(" \nＧＡＭＥ ФＶＥＲ ")
                    p["Progress Choice 3"] = "YOU WIN"
                    break
        elif progressChoice == 2: 
            print("\nThe young Swordwoman get's frustrated as they do not like learning by reading and kills you. Bye Bye!")
            print(r"""
                                ███████▄▄███████████▄
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓███░░░░░░░░░░░░█
                                ██████▀░░█░░░░██████▀
                                ░░░░░░░░░█░░░░█
                                ░░░░░░░░░░█░░░█
                                ░░░░░░░░░░░█░░█
                                ░░░░░░░░░░░█░░█
                                ░░░░░░░░░░░░▀▀ 
            """)
            print(" \nＹФＵ ＬФＳＥ ")
            print(" \nＧＡＭＥ ФＶＥＲ ")
            print("\nHey! You're awake!!")
            p["Progress Choice 1"] = "YOU LOSE"
        else:
            progressChoice = 0

    if progressChoice == 4:
        print("\nYou had too much trust in the young Swordswoman. She died. Bye Bye!")
        print(r"""
                                ███████▄▄███████████▄
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓███░░░░░░░░░░░░█
                                ██████▀░░█░░░░██████▀
                                ░░░░░░░░░█░░░░█
                                ░░░░░░░░░░█░░░█
                                ░░░░░░░░░░░█░░█
                                ░░░░░░░░░░░█░░█
                                ░░░░░░░░░░░░▀▀ 
            """)
        print(" \nＹФＵ ＬФＳＥ ")
        print(" \nＧＡＭＥ ФＶＥＲ ")
        print("\nHey! You're awake!!")
        p["Progress Choice 2"] = "YOU LOSE"
        progressChoice = 0

    if progressChoice == 5:
        print("\nThe superior court of Swordsmen kill you as they see you as an unworthy teacher.")
        print(r"""
                                ███████▄▄███████████▄
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓█░░░░░░░░░░░░░░█
                                ▓▓▓▓▓▓███░░░░░░░░░░░░█
                                ██████▀░░█░░░░██████▀
                                ░░░░░░░░░█░░░░█
                                ░░░░░░░░░░█░░░█
                                ░░░░░░░░░░░█░░█
                                ░░░░░░░░░░░█░░█
                                ░░░░░░░░░░░░▀▀ 
            """)
        print(" \nＹФＵ ＬФＳＥ ")
        print(" \nＧＡＭＥ ФＶＥＲ ")
        print("\nHey! You're awake!!")
        p["Progress Choice 3"] = "YOU LOSE"
        progressChoice = 0


# In[ ]:


p


# In[ ]:




