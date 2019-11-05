import random
HP = 30
MP = 12
armor_type = 2
print('----------Maveth:A text adventure----------')
Name = str(input('A glorious adventure awaits you.\nType help for manual or type your name to begin:\n'))
while Name == 'help':
    print('No manual yet')
    Name = str(input('A glorious adventure awaits you.\nType name to begin or type help to refresh manual:\n'))
print('Hello......')
cmd = input('')
print('Lord', Name, 'Wake up')
cmd1 = input('')
print("It's me, Ophelia")
cmd2 = input('')
print(Name, ': ......Good Morning Ophelia')
cmd3 = input('')
print('Ophelia: Today is the day you finally conquer the rest of Pangea')
cmd4 = input('')
print(Name, ': Is the army ready?')
cmd5 = input('')
print('Ophelia: The Inhumans are prepared,')
cmd6 = input('')
print(Name, ': And what of the human resistance')
cmd7 = input('')
print('Ophelia: Under Control')
cmd8 = input('')
print('Ophelia: My Lord what would you like to do?\n1)Prepare for Battle\n2)Eat Breakfast')
choice_1 = int(input('1 or 2:\n'))
if choice_1 == 1:
    HP = 30
    MP = 12
    print('---Entering armory---')
    cmd9 = input('')
    print('Ophelia: Which armor would you like to wear?\n1)Vrell Nexian Repellant Armor'
          '\n2)Kree Battle Armor\n3)Hive Armor')
    armor_type = int(input('1, 2, or 3:\n'))
    if armor_type == 1:
        Repel_Vrell_Nexian = 1
    elif armor_type == 2:
        Repel_Kree = 1
    elif armor_type == 3:
        MP = MP + 10
elif choice_1 == 2:
    print('---Entering Dining Hall---')
    cmd10 = input('')
    print('HP and MP restored')
    cmd = input()
    HP = 40
    MP = 18
print("Ophelia: Lord", Name)
cmd11 = input('')
print("Ophelia: Now it is time for Combat Practice ")
cmd12 = input()
print('---Entering Training Area---')
cmd13 = input()
print("Hi, I am Anton Ivanov")
cmd14 = input()
print('I will be sparing with you today')
cmd15 = input()
Choice_2 = str(input('Are you Ready?(Yes or No)\n'))
if Choice_2 == 'Yes':
    print("Anton: Well,...Let's begin")
elif Choice_2 == 'No':
    print("Anton: Too late lets begin")
print('----Battling Anton Ivanov----')
EnemyHP = 25
HPreal = HP
MPreal = MP
while EnemyHP > 0:
    print('Anton Ivanov HP = ', EnemyHP)
    print(Name, 'HP =', HP)
    print(Name, 'MP =', MP)
    EnemyAttacktype = random.randint(1, 3)
    PlayerAttacktype = int(input('\nChoose your attack:-\n1)Hive Attack\n2)Spear Attack\n3) Punch\n'))
    if EnemyAttacktype > PlayerAttacktype:
        if EnemyAttacktype == 3:
            print('Anton Ivanov used Kick')
            HP = HP - 1
            print('You lost 1 HP')
        else:
            print('Anton Ivanov used Knife throw')
            HP = HP - 2
            print('You lost 2 HP')
        print('Your HP is', HP)
        cmd2 = input('')
        if HP == 0:
            while HP == 0:
                print('---Game Over--')
                cmd1 = input('')
        else:
            if PlayerAttacktype == 1:
                if MP > 2:
                    print('You used Hive Attack')
                    EnemyHP = EnemyHP - 6
                    MP = MP - 3
                    print('Anton Ivanov lost 6HP')
                    print(' You now have', MP, 'MP')
                else:
                    print("You don't have enough MP")
                    print('Anton Ivanov lost no HP')
            else:
                print('You used Spear Attack')
                EnemyHP = EnemyHP - 4
                print('Anton Ivanov lost 4HP')
        print("Anton Ivanov's HP is", EnemyHP)
        cmd3 = input('')
    else:
        if PlayerAttacktype == 1:
            if MP > 2:
                print('You used Hive Attack')
                EnemyHP = EnemyHP - 6
                MP = MP - 3
                print('Anton Ivanov lost 6HP')
                print(' You now have', MP, 'MP')
            else:
                print("You don't have enough MP")
                print('Anton Ivanov lost no HP')
        elif PlayerAttacktype == 2:
            print('You used Spear Attack')
            EnemyHP = EnemyHP - 4
            print('Anton Ivanov lost 4HP')
        elif PlayerAttacktype == 3:
            print('You used Punch')
            EnemyHP = EnemyHP - 2
            print('Anton Ivanov lost 2HP')
        print("Anton Ivanov's HP is", EnemyHP)
        cmd4 = input('')
        if EnemyHP == 0:
            break
        else:
            if EnemyAttacktype == 3:
                print('Anton Ivanov used Kick')
                HP = HP - 1
                print('You lost 1 HP')
            elif EnemyAttacktype == 2:
                print('Anton Ivanov used Knife throw')
                HP = HP - 2
                print('You lost 2 HP')
            elif EnemyAttacktype == 1:
                print('Anton Ivanov used Knife Stab')
                HP = HP - 3
                print('You lost 3 HP')
                print('Your HP is', HP)
                cmd5 = input('')
            if HP <= 0:
                while HP <= 0:
                    print('---Game Over--')
                    cmd1 = input('')
print('You defeaed the Anton Ivanov')
cmd = input()
print('Anton: I must say you have gotten pretty good')
cmdagain = input()
print('Ophelia: Lord', Name, 'I am getting reports of a human attack around the '
                             'southwest corner and they want you to battle with them')
cmdkillme = input()
print(Name, ": How dare these pesky humans challenge me! Let me show them what it is like to "
            "challenge the leader of the Inhuman's First Movement")
cmdyidodis = input()
print('----Entering South-West Wing----')
cmdicantstop = input()
print(Name, ": Ophelia, I dont see any...")
cmdihearnoises = input()
print('----You are being gagged----')
cmdsmthingishappenig = input()
print('--by OPHELIA!--')
cmdhestakingcontrol = input()
print('--You Fainted--')
cmd16 = input()
print('--')
cmd17 = input()
print('--You hear distinct noises--')
cmd18 = input()
print('Unknown: send it to Maveth')
cmd19 = input()
print('--You are being dragged towards a mysterious Monolith--')
cmd20 = input()
print('--Entering Maveth--')
cmdimuststop = input()
print('--You are in a mysterious land--')
cmdhewillcomeback = input()
print('--You hear screeching noises--')
cmdhesback = input()
print('--It looks like a giant roach--')
cmdSENDHEL__ = input()
print('--There is note in your pants--')
cmducanthelphim = input()
print('--It reads "Beware of Vrell Nexians"')
cmdiamtakingcontrol = input()
print('--As you put the note down you see a Vrell Nexian growling at you--')
cmdforever = input()
HP = HPreal
MP = MPreal
if armor_type == 1:
    print('Ít ran away because of your armor')
    cmd21 = input()
else:
    choice_3 = int(input('--What do you do--:\n1)Run\n2)Hide\n3)Fight'))
    if choice_3 == 1:
        print('The Vrell Nexian is faster')
    elif choice_3 == 2:
        print('There is nowhere to hide')
    elif choice_3 == 3:
        print('Get ready to fight')
    print('--A Vrell Nexian is Attacking')
    cmd = input('')
    RoachHP = 40
    while RoachHP > 0:
        print('Vrell Nexian HP = ', RoachHP)
        print(Name, 'HP =', HP)
        print(Name, 'MP =', MP)
        RoachAttacktype = random.randint(1, 3)
        PlayerAttacktype = int(input('\nChoose your attack:-\n1)Hive Attack\n2)Spear Attack\n3) Punch\n'))
        if RoachAttacktype > PlayerAttacktype:
            if RoachAttacktype == 3:
                print('Vrell Nexian used Headbutt')
                HP = HP - 1
                print('You lost 1 HP')
            else:
                print('Vrell Nexian used Bite')
                HP = HP - 2
                print('You lost 2 HP')
            print('Your HP is', HP)
            cmd2 = input('')
            if HP == 0:
                while HP == 0:
                    print('---Game Over--')
                    cmd1 = input('')
            else:
                if PlayerAttacktype == 1:
                    if MP > 2:
                        print('You used Hive Attack')
                        RoachHP = RoachHP - 6
                        MP = MP - 3
                        print('Vrell Nexian lost 6HP')
                        print(' You now have', MP, 'MP')
                    else:
                        print("You don't have enough MP")
                        print('Vrell Nexian lost no HP')
                else:
                    print('You used Spear Attack')
                    RoachHP = RoachHP - 4
                    print('Vrell Nexian lost 4HP')
            print("Vrell Nexian's HP is", RoachHP)
            cmd3 = input('')
        else:
            if PlayerAttacktype == 1:
                if MP > 2:
                    print('You used Hive Attack')
                    RoachHP = RoachHP - 6
                    MP = MP - 3
                    print('Vrell Nexian lost 6HP')
                    print(' You now have', MP, 'MP')
                else:
                    print("You don't have enough MP")
                    print('Vrell Nexian lost no HP')
            elif PlayerAttacktype == 2:
                print('You used Spear Attack')
                RoachHP = RoachHP - 4
                print('Vrell Nexian lost 4HP')
            elif PlayerAttacktype == 3:
                print('You used Punch')
                RoachHP = RoachHP - 2
                print('Vrell Nexian lost 2HP')
            print("Vrell Nexian's HP is", RoachHP)
            cmd4 = input('')
            if RoachHP == 0:
                break
            else:
                if RoachAttacktype == 3:
                    print('Vrell Nexian used Headbutt')
                    HP = HP - 1
                    print('You lost 1 HP')
                elif RoachAttacktype == 2:
                    print('Vrell Nexian used Bite')
                    HP = HP - 2
                    print('You lost 2 HP')
                elif RoachAttacktype == 1:
                    print('Vrell Nexian used Claw Attack')
                    HP = HP - 3
                    print('You lost 3 HP')
                print('Your HP is', HP)
                cmd5 = input('')
                if HP <= 0:
                    while HP <= 0:
                        print('---Game Over--')
                        cmd1 = input('')
    print('You defeated the Vrell Nexian')
    cmd22 = input()
print(Name, ": It all happened so fast.")
cmdC = input()
print(Name, ': How could she betray me')
cmdL = input()
print(Name, ': It does not matter now')
cmdO = input()
print(Name, ': Only my followers can save me')
cmdS = input()
print(Name, ': I hope they remember')
cmdE = input()
print('HAIL HYDRA')
print('''(((((((((((////(///%%%%&@&%%%%%%%%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%%%%%%%%%%%@@&%%%%/((((((((((((((((((
((((((/(///(/(///%%%%@@&%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%&@@%%%%////////((/((((((
((//((/(///////%%%%&@&%%%%%%%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####################&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%%%%%%%%%%&@&%%%%/////((/(((((((
((/(((///////%%%%%@&%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%###############################&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%&@&%%%%/////((((((((
((/////////#%%%%@@%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#######################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%@@%%%%#/////((((((
//(///////%%%%&@%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%&@%%%%//////((/(
////(///(%%%&@&%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#############################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%&&&%%%#/////(//
(//////%%%%@@%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###############################################&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%@@%%%%///////
//(///%%%%@&%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#################################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%&@%%%%//////
/////%%%%@%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#################################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%@&%%%/////
///(%%%&&%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#################################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%&&%%%(///
//#%%%@@%%%%%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#################################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%%%%%%%%@&%%%#//
/(%%%@@%%%%%###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#################################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%&&%%%#(
/%%%&&%%%%%%%%@@@@@@@@@@@&%%%##%%%%%&@@@@@@@@@@@@@@@@@@##############################################&@@@@@@@@@@@@@@@@&&%%%####%%%&&&@@@@@@@@@@%%%%%%%%&&%%%(
%%%@@%%%%%%%%@@@@@@@%%#%####%############%@@@@@@@@@@@@@@###############################################@@@@@@@@@@@@@%#################%#%%%&@@@@@@%%%%%%%%@&%%%
%%&@%%%%%%%%@@@@@%%%%%%#%####################%@@@@@@@@@@###############################################@@@@@@@@@@######################%#%%%@@@@@%%%%%%%%@&%%
%%@%%%%%%%%@@@%%%%%%%%##%@@@@@@@@%##############&@@@@@@@@#############################################@@@@@@@@@@###########%&@@@@@#%%%%%#%%%@@@@%%%%%%%%@%%
%@&%%%%%%#@@@%%%%%%#%%%@@@@@@@@@@@@@%############@@@@@@@@#############################################@@@@@@@@@%###########@@@@@@@@@@@@@@%####%%%%@@&%%%%%%%&@%
&&%%%%%%%&@@%%%%%###%@@@@@@@@@@@@@@@@@##########@@@@@@@@###########################################@@@@@@@@@###########@@@@@@@@@@@@@@@@@@%###%%%%@@&%%%%%%%&&
@%%%%%%%%@@%%%%%%#%%@@@@@@@@@@@@@@@@@@@%##########%@@@@@@@######&@@@@@###############&@@@@@@#######@@@@@@@###########@@@@@@@@@@@@@@@@@@@@@%%%%%%@@%%%%%%%%@
&%%%%%%#@@@%%%%%#%#%@@@@@@@@@@@@@@@@@@@@%##########@@@@@@@#####@@@@@@@@@@@@#########&@@@@@@@@@@####@@@@@@###########%@@@@@@@@@@@@@@@@@@@@@@%%%%%%%@@@%%%%%%%&
%%%%%%%%@@&%%%%%###&@@@@@@@@@@@@@@@@@@@@@##########&@@@@@@%#####&@@@@@@@@@%#########%@@@@@@@@@@#####%@@@@@@###########@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%@@%%%%%%%%
%%%%#%#@@@%%%%%%%##%@@@@@@@@@@@@@@@@@@@@@#########%@@@@@%#######@@########%@#######%%&&@######%@@@@@@##########&@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%@@@%%%%%%%
%%%%%%%@@@%%%%######%@@@@@@@@@@@@@@@@@@@@@############@@@@%##################%@@@%###################@@@@@%##########@@@@@@@@@@@@@@@@@@@@@@@##%%%%%@@@%%%%%%%
%%%%%%@@@@&%%%#######%@@@@@@@@@@@@@@@@@@@@@###########@@@@%##################@@@@@###################@@@@@##########@@@@@@@@@@@@@@@@@@@@@@@%#%##%%%%%@@@@%%%%%%
%%%#%%@@@@@%%###%######@@@&&%######&@@@@@@@%##########@@@@@################%@@@################%@@@@@@##########@@@@@@@#%@@@@@@@@@@@@%####%%%%%%@@@@@%%%%%%
%%%%%%@@@@@&%%#####################%@@@@@@@@##########&@@@@@@#####################################@@@@@@###########@@@@@@@@@%#######%############%%@@@@@@%%%%%%
%%%%%&@@@@@@@%################%@@@@@@@@@@@@###########&@@@@@@@@@@@%######################@@@@@@@@@@@%##########%@@@@@@@@@@@@################%##%&@@@@@@&%%%%%
%%%%%@@@@@@@@@@@%###########%&@@@@@@@@@@@@@@@@@#############%@@@@@@@%######################@@@##################@@@@@@@@@@@@@@@@@@#########%&@@@@@@@@@@@%%%%%
%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##############&@@@%######################@@#################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%
%%%%#@@@@@@@@@@@@@@@@@@@@@@&&&&&&%%%%%%%%%%%%@@@@@@@%#############@@@@@@#############@@@@@%#############&@@@@@@%&@@@@@@@&%%%&&&&&&&@@@@@@@@@@@@@@@@@@@@@%%%%%
%%#%%@@@@@@@@@@@@@################################&@@@@@@%#########%@@@@@@@@%@@@##%@@@@@@@@########&@@@@@################################&@@@@@@@@@@@@%%%%%
%##%#@@@@@@@@@#####################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@######################################%@@@@@@@@@@%%%%%
%%%%%@@@@@@@@########################################%@@@@@@@@@%#########@@@@@@@@@#########@@@@@@@@@#####################################%#%#&@@@@@@@@%%%%%
%%%%%@@@@@@@%###############################################################@@@@@@@##########################################################%###%%@@@@@@@%%%%%
%%%%#&@@@@@%#################%@@@@@@@@@@@##################################%@@@@@@@%##################################&@@@@@@@@@@###############%&@@@@@&%%%%%
%%%%%%@@@@@%###############@@@@@@@@@@@@@@@@@@@##########################&@@@@#&@@@@@#########################@@@@@@@@@@@@@@@@@@@#############%%&@@@@@%%%%%%
%%%%%%@@@@@%############&@@@@@@@@@@@@@@@@@@@@@@@@@#################@@@@@@%##&@##@@@@@@##################&@@@@@@@@@@@@@@@@@@@@@@@@@%########%#%%&@@@@@%%%%%%
%%%%%%&@@@@%##########%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@########&@@@@@@@###&@####@@@@@@@########%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%######%#%#&@@@@&%%%%%%
%%%%%%%@@@@%#######@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#######%@#######&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#####%%%%&@@@@%%%%%%%
%%%%%%%&@@@######@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@###########%@##########&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%###%#%%&@@@&%%%%%%%
%%%%%%%%@@@@#######@@@@@@@@@@@@@@@@@@@@@@@@@@@##&@@@@@@@@@@@@@##############%@#############&@@@@@@@@@@@@@@@##@@@@@@@@@@@@@@@@@@@@@@@@@@@##%%#%%@@@@%%%%%%%%
&%%%%%%#&@@@%%%####@@@@@@@@@@@@@@@@@@@@@@@@@@@###@@@@@@@@@@###################@@###################&@@@@@@@@###%@@@@@@@@@@@@@@@@@@@@@@@@@@###%%%%@@@&%%%%%%%&
&%%%%%%%%@@@@#####%@@@@@@@@@@@@@@@@@@@@@@@@@@@###@@@@@@%####################@@@@@@%#####################@@@@@@###@@@@@@@@@@@@@@@@@@@@@@@@@@@%#%%%%@@@@%%%%%%%%&
&&%%%%%%%%@@@&%#%###&@@@@@@@@@@@@@@@@@@@@@@@@%###@@@@#####################&@@@@@@@@@@#####################&@@@####@@@@@@@@@@@@@@@@@@@@@@@@@%#%%%%&@@@%%%%%%%%@&
%&&%%%%%#%%@@@########&@@@@@@@@@@@@@@@@@@@@@####&@@###############%@@@@@@@@@@@@@@@@@@@@@@@@&%###############@@@####&@@@@@@@@@@@@@@@@@@@@@%##%%%%%@@@%%%%%%%%&@%
%%@%%%%%%%%%@@@%#######@@@@@@@@@@@@@@@@@@@#####%@@############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###########@@######&@@@@@@@@@@@@@@@@@@%###%%%%@@@%%%%%%%%&&%%
%%&&%%%%%%%%&@@@%%#####@@@@@@@@@@@@@@@#######@@##########&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#########%@@#######%@@@@@@@@@@@@@@@%####%%%@@@&%%%%%%%%@%%%
%%%&&%%%%%%%%&@@@%%####@@@@@@@@@@%############@@%########%@@@@@@@@@@@@@@@#@@@@@@@@@@@&@@@@@@@@@@@@@@@#######%@@##########%@@@@@@@@@@@%##%%%%@@@&%%%%%%%%&&%%%
/%%%&&%%%%%%%#&@@@%%##%######################&@######%@@@@@@@@@@@@@@@@@%#%@@@@@@@###@@@@@@@@@@@@@@@@@%#######&@##############%##%##%#%%%%@@@&%%%%%%%%@@%%%(
/(%%%&&%%%%%%%%%@@@#######################%@######&@@@@@@@@@@@@@@@@@@@###&@@@@###%@@@@@@@@@@@@@@@@@@@#######@@%####################%%%%%@@@%%%%%%%%%@&%%%#/
///%%%&&%%%%%%%%%@@@@###%##################%@@#######&@@@@@@@@@@@@@@@@@@@@%####@###@@@@@@@@@@@@@@@@@@@@######@@%###########%#%##%#%%%%@@@@%%%%%%%%%@&%%%#//
////%%%&&%%%%%%%%#&@@@%##%%################@@#######&@@@@@@@@@@@@@@@@@@@@@@####@####%@@@@@@@@@@@@@@@@@@@@@########@@#############%#%#%%%&@@@&%%%%%%%%%@&%%%(///
/////%%%%&&%%%%%%%%%@@@@%%%##############&@@%#######@@@@@@@@@@@@@@@@@@@@@@@@###@####@@@@@@@@@@@@@@@@@@@@@@@#######%@@#########%#%%%%%@@@@%%%%%%%%%&&%%%%/////
//////%%%%&&%%%%%%%%%&@@@@%#############@@@########@@@@@@@@@@@@@@@@@@@@@@@###@####@@@@@@@@@@@@@@@@@@@@@@########%&@@@######%##%%%%%@@@@&%%%%%%%%%&@%%%%//////
///////#%%%&&%%%%%%%%%%@@@@@@@@%%#%%&@@@@@@##########%@@@@@@@@@@@@@@@@@@@@@####@####%@@@@@@@@@@@@@@@@@@@@#######%%#%@@@@@@&%%%%%&@@@@@@@%%%%%%%%%%@&%%%%///////
////////(%%%%&&%%%%%%%%#%@@@@@@@@@@@@@@@@@@%##########%@@@@@@@@@@@@@@@@@@@#####@#####@@@@@@@@@@@@@@@@@@@%######%%%%%@@@@@@@@@@@@@@@@@@%%%%%%%%%%&@%%%%(////////
//////////%%%%&&&%%%%%%%%%%@@@@@@@@@@@@@@@@%############@@@@@@@@@@@@@@@@@######@######@@@@@@@@@@@@@@@@######%%%%%%@@@@@@@@@@@@@@@@&%%%%%%%%%%&&%%%%//////////
////////////%%%%&&%%%%%%%%%%%@@@@@@@@@@@@@@@#############&@@@@@@@@@@@@@@#######@######&@@@@@@@@@@@@@@#######%%%%%%&@@@@@@@@@@@@@@@%%%%%%%%%%%&&%%%%(///////////
/////////////%%%%%@&%%%%%%%%%%%@@@@@@@@@@@@@@@%#%##########&@@@@@@@@@%#########@########%@@@@@@@@@@####%%%%%%%%%&@@@@@@@@@@@@@@@%%%%%%%%%%%@@%%%%%/////////////
///////////////%%%%%@&%%%%%%%%%%%&@@@@@@@@@@@@@@###########%################%@%###########%%%%%#####%%%%%%%%&@@@@@@@@@@@@@@&%%%%%%%%%%%&&%%%%%//////////////(
/////////////////%%%%%&@%%%%%%%%%%%%@@@@@@@@@@@@@@@%%#########################@@############%%##%%%%%%%%%%@@@@@@@@@@@@@@@%%%%%%%%%%%%&&%%%%%/////////(/(((/((
(//////////////////%%%%%@@%%%%%%%%%%%%%@@@@@@@@@@@@@@%#######################@@@@@########%#%%%%%%%%%%%%%&@@@@@@@@@@@@@@%%%%%%%%%%%%%&@%%%%%/////////////(/(/((
/(///////////////////%%%%%&@&%%%%%%%%%%%%%&@@@@@@@@@@@@@%##%###############%&@@@@@@##%%####%%%%%%%%%%%%@@@@@@@@@@@@@@%%%%%%%%%%%%%&@@%%%%%////////////((((/((/(''')
cmdUrnxt = input()
print('--END OF PART ONE--')
print('Credits')
print('Story: Ayan')
print('Game Design: Ayan')
print('Game Balancing: Ayan')
print('Head Superviser: Ayan')
print('Special Thanks to Ayan')