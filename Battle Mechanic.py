import random
PlayerHP = 20
PlayerMP = 1
x = 'Enemy type'
armor_type = 2
Name = 'TEST'
print('----A wild Vrell Nexian appeared----')
cmd = input('')
RoachHP = 10
if armor_type == 1:
    print('It ran away')
else:
    while RoachHP > 0:
        print('Vrell Nexian HP = ', RoachHP)
        print(Name, 'HP =', PlayerHP)
        print(Name, 'MP =', PlayerMP)
        RoachAttacktype = random.randint(1, 3)
        PlayerAttacktype = int(input('\nChoose your attack:-\n1)Hive Attack\n2)Spear Attack\n3) Punch\n'))
        if RoachAttacktype > PlayerAttacktype:
            if RoachAttacktype == 3:
                print('Vrell Nexian used Headbutt')
                PlayerHP = PlayerHP - 1
                print('You lost 1 HP')
            else:
                print('Vrell Nexian used bite')
                PlayerHP = PlayerHP - 2
                print('You lost 2 HP')
            print('Your HP is', PlayerHP)
            cmd2 = input('')
            if PlayerHP == 0:
                while PlayerHP == 0:
                    print('---Game Over--')
                    cmd1 = input('')
            else:
                if PlayerAttacktype == 1:
                    if PlayerMP > 2:
                        print('You used Sway Attack')
                        RoachHP = RoachHP - 6
                        PlayerMP = PlayerMP - 3
                        print('Vrell Nexian lost 6HP')
                        print(' You now have', PlayerMP, 'MP')
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
                if PlayerMP > 2:
                    print('You used Sway Attack')
                    RoachHP = RoachHP - 6
                    PlayerMP = PlayerMP - 3
                    print('Vrell Nexian lost 6HP')
                    print(' You now have', PlayerMP, 'MP')
                else:
                    print("You don't have enough MP")
                    print('Vrell Nexian lost no HP')
            elif PlayerAttacktype == 2:
                print('You used Spear Attack')
                RoachHP = RoachHP - 4
                print('Vrell Nexian lost 4HP')
            elif PlayerAttacktype == 3:
                print('You used Spear Attack')
                RoachHP = RoachHP - 2
                print('Vrell Nexian lost 2HP')
            print("Vrell Nexian's HP is", RoachHP)
            cmd4 = input('')
            if RoachHP == 0:
                break
            else:
                if RoachAttacktype == 3:
                    print('Vrell Nexian used Headbutt')
                    PlayerHP = PlayerHP - 1
                    print('You lost 1 HP')
                elif RoachAttacktype ==2:
                    print('Vrell Nexian used bite')
                    PlayerHP = PlayerHP - 2
                    print('You lost 2 HP')
                elif RoachAttacktype ==1:
                    print('Vrell Nexian used bite')
                    PlayerHP = PlayerHP - 3
                    print('You lost 3 HP')
                print('Your HP is', PlayerHP)
                cmd5 = input('')
                if PlayerHP <= 0:
                    while PlayerHP <= 0:
                        print('---Game Over--')
                        cmd1 = input('')
print('You defeated the Vrell Nexian')







