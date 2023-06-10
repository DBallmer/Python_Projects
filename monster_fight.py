import random

#select random oppoonent
def opponent_roll(num):
    return opp_tup[num]

#Print opponents stats
def opp_grabstats(num):
    return opp_stat[num]

#create list of 4 items for merchant to offer
def gen_equip():
    swag = list(equip.items())
    stufflist = []
    for i in range(4):
        rando = random.randint(0, 9)
        while swag[rando] in stufflist:
            rando = random.randint(0, 9)
        stufflist.append(swag[rando])
    return(stufflist)

#display items merchant offers
def show_items(item_list):
    for i in range(len(item_list)):
        print("Item", i + 1, ":", equip_offer[i], )

#apply equipment bonuses
def equip_boost(i_name):
    global attack
    global defense

    if i_name==("sword", 3):
        attack = attack + 3
        return()
    elif i_name==("shield", 2):
        defense = defense +2
        return()
    elif i_name==("chainmail", 5):
        defense = defense + 5
        return()
    elif i_name==("bow", 2):
        attack = attack + 2
        return()
    elif i_name==("dagger", 2):
        attack = attack + 2
        return()
    elif i_name==("helmet", 1):
        defense = defense + 1
        return()
    elif i_name==("horse", 5):
        defense = defense + 5
        return()
    elif i_name==("fire wand", 6):
        attack = attack + 6
        return()
    elif i_name==("leather armor", 3):
        defense = defense + 3
        return()
    elif i_name==("war puggle", 4):
        attack = attack + 4
        return()
    else:
        print("This should be impossible to reach")

def print_sep():
    print("\033[1;36;40m---~~~)|(~~~---""\033[1;33;40m---~~~)|(~~~---""\033[1;36;40m---~~~)|(~~~------~~~)|(~~~---""\033[1;33;40m---~~~)|(~~~---""\033[1;36;40m---~~~)|(~~~---")

def k_press():
    a = input("\033[1;36;40m[Press enter to continue]")

def combat(mylife, monlife, myatk, monatk, mydef, mondef):
    while mylife > 0 and monlife > 0:
        print("\033[1;32;40mYou attack and ...")
        k_press()
        atkroll = random.randint(1,20)
        if atkroll - mondef < 1:
            print("\033[1;31;40m-=[MISS]=-")
            k_press()
            life_totes(mylife, monlife)
        else:
            print("\033[1;34;40m-=[HIT for", (atkroll - mondef) + myatk,"]=-")
            monlife = monlife - ((atkroll - mondef) + myatk)
            k_press()
            life_totes(mylife, monlife)
            if monlife < 1:
                return(mylife)

        print("\033[1;32;40mThe", opponent,"attacks YOU and ...")
        k_press()
        atkroll = random.randint(1, 20)
        if atkroll - mondef < 1:
            print("\033[1;34;40m-=[MISSES]=-")
            k_press()
            life_totes(mylife, monlife)
        else:
            print("\033[1;31;40m-=[HITS for", (atkroll - mydef) + monatk,"]=-")
            mylife = mylife - ((atkroll - mydef) + monatk)
            k_press()
            life_totes(mylife, monlife)
            if mylife < 1:
                return (None)

def life_totes(mylife, monlife, opponent):
    print("\033[1;46;30m-=[LIFE TOTALS]=-\033[1;31;40m")
    print("\033[1;31;40m",opponent)
    for i in range(monlife):
        print("*", end="")
    print("\n")
    print("\033[1;34;40m", name)
    for i in range(mylife):
        print("*", end="")
    print("\n")



#char base stats
life = 40
attack = 10
defense = 10

#tuple of random opponents
opp_tup=("Orc", "Goblin", "Skeleton", "Dragon", "Rat", "Giant Snake","Griffin")
#tuple of oppoenet's stats
opp_stat = ([45, 12, 3],[25, 6, 8], [25, 10, 10], [60, 20, 15], [10, 6, 8], [40, 12, 9], [45, 13, 13] )

#Dictionary of equipment
equip = {"sword" : 3,
         "shield" : 2,
         "chainmail": 5,
         "bow" : 2,
         "dagger" : 2,
         "helmet" : 1,
         "horse" : 5,
         "fire wand" : 6,
         "leather armor" : 3,
         "war puggle" : 4
         }

name = input("\033[1;37;40m What is your name, hero? ")
opponent_num = random.randint(0, 6)
opponent = opp_tup[opponent_num]
print("\033[1;37;40m", name, "- you are going to fight a", "\033[1;31;40m", opponent,"!!!")

k_press()

print_sep()

#assign monster stats
mon_stat = opp_grabstats(opponent_num)
opp_life = mon_stat[0]
opp_attack = mon_stat[1]
opp_defense = mon_stat[2]

print("\033[2;44;40mCOMBATANTS:")
print("\033[1;31;40m",opponent, "stats | Life:", opp_life, "| Attack:", opp_attack, "| Defense:", opp_defense)
print("\033[1;32;40m Your stats | Life:", life, "| Attack:", attack, "| Defense:", defense)

print_sep()

k_press()

#Merchant and equipment section
print("\033[1;37;40mA friendly merchant offers to give you two items from his cart (item name and power).")
equip_offer = gen_equip()
my_equip =[]
choice = 2

show_items(equip_offer)

while(choice):
    my_pick = int(input("\033[1;37;40mPick the number of the item you want: "))
    if my_pick <= len(equip_offer) and my_pick > 0:
        choice -= 1
        my_equip.append(equip_offer[my_pick-1])
        del(equip_offer[my_pick-1])
        if choice ==0:
            break
        print("\033[1;37;40mNext choice:")
        show_items(equip_offer)

    else:
        print("\033[1;36;40mTry again! (Hint, you need to pick a number between 1 and", len(equip_offer))
        continue

print_sep()
print ("You have taken: ", my_equip)

for k in range(len(my_equip)):
    equip_boost(my_equip[k])

print ("\033[1;32;40mYour new stats are: | Life:", life, "| Attack:", attack, "| Defense:", defense)
print_sep()
print("\033[1;31;40mGet ready to fight!")
k_press()

mylife = combat(life, opp_life, attack, opp_attack, defense, opp_defense)
if (mylife):
    print("You Win!!!")
else:
    print("Tough break,", name," - it looks like the monsters got you this time")
