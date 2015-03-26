#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alex
#
# Created:     25/06/2014
# Copyright:   (c) Alex 2014
# Licence:     CC
#Not compatable with 2.7, use 3.2
#-------------------------------------------------------------------------------

#To do:
#Converter

#to use money_reset to change large: swap amount to others to change small/meduim and change large to money[2] and change type as required:
#Remerber system is not relative!! Use amount=money[2](1 for medium, 0 for small)-/+price change.
#type=L
#x_money=money[3]
#l_money=amount *set large to x* or "amount=money[2]-/+price change" *increase/decrease large by x"
#m_money=money[1]
#s_money=money[0]
# money_reset(s_money, m_money, l_money, x_money, money)

import os #used for file deleting

#error checking
def is_number(to_check):
    if to_check.isdigit():
        is_number="TRUE"
    else:
        is_number="FALSE"
    return is_number

def is_text(to_check):
    #Not yet used-thought it might be useful
    if to_check.isdigit():
        is_number="TRUE"
    else:
        is_number="FALSE"
    return is_number

def money_reset(s_money, m_money, l_money, x_money, money):
        money.remove(money[3])
        money.remove(money[2])
        money.remove(money[1])
        money.remove(money[0])
        money.append(s_money)
        money.append(m_money)
        money.append(l_money)
        money.append(x_money)
        print("Succsesful money change")
        return money

def change(money, type, amount):
    if type==("S"):
        x_money=money[3]
        l_money=money[2]
        m_money=money[1]
        s_money=amount
        money_reset(s_money, m_money, l_money, x_money, money)
    elif type==("M"):
        x_money=money[3]
        l_money=money[2]
        m_money=amount
        s_money=money[0]
        money_reset(s_money, m_money, l_money, x_money, money)
    elif type==("L"):
        x_money=money[3]
        l_money=amount
        m_money=money[1]
        s_money=money[0]
        money_reset(s_money, m_money, l_money, x_money, money)
    elif type==("X"):
        x_money=amount
        l_money=money[2]
        m_money=money[1]
        s_money=money[0]
        money_reset(s_money, m_money, l_money, x_money, money)
    else:
        print("Error - money type not recognised. Use capital S,M,L or X only for type veriable")
        return money

#starting money
money=[]
x_money=10
l_money=20
m_money=40
s_money=60
money.append(s_money)
money.append(m_money)
money.append(l_money)
money.append(x_money)

global inventry
inventry=[]

def amount(items, item_no):
    if  items[item_no][9]==0 and items[item_no][10]==0 and items[item_no][11]==0:
        ret=items[item_no][12]
    elif  items[item_no][9]==0 and items[item_no][10]==0 and items[item_no][12]==0:
        ret=items[item_no][11]
    elif  items[item_no][9]==0 and items[item_no][11]==0 and items[item_no][12]==0:
        ret=items[item_no][10]
    elif  items[item_no][10]==0 and items[item_no][11]==0 and items[item_no][12]==0:
        ret=items[item_no][9]
    else:
        place="error"
    return ret

def places(items, item_no):
    if  items[item_no][9]==0 and items[item_no][10]==0 and items[item_no][11]==0:
        place="X"
    elif  items[item_no][9]==0 and items[item_no][10]==0 and items[item_no][12]==0:
        place="L"
    elif  items[item_no][9]==0 and items[item_no][11]==0 and items[item_no][12]==0:
        place="M"
    elif  items[item_no][10]==0 and items[item_no][11]==0 and items[item_no][12]==0:
        place="S"
    else:
        place="error"
    return place
#---------------------------------------------------------------------------------------------------
#Arrays
global armour, weapons

clothing = []
armour = []
weapons = []

#Defalts
#Code Specific
currentHandItem = " "
currentArmour = " "

#Items - Examples for testing purposes. To be replaced with finished items.


#Messages
inventMessage = "You currently have " + str(weapons)
currentHandItemMessage = "You are currenty wielding a" + str(weapons)
pickUpMessage = "You have picked up a "
dropItemMessage = "You have dropped a "
failedToEquipMessage = "Therefore you were unable to equip the item."
currentArmourMessage = "You are wearing " + str(armour)
unEquipArmourMessage = "You have unequiped your armour."
unEquipWeaponMessage = "You have unequiped your weapon."

"""
Functions below for actions:
All functions start by finding the category of the item so that it is able to
deal with the appropriate part of the inventory (may be streamlined using a
second function at a later date.) <-- Not applicable to pickUpItem()
"""

#Function for putting an item into the inventory.
def pickUpItem(obj):
    global armour, weapons
    if obj[5] == "clothing":
        clothing.insert(obj[4])
        print(pickUpMessage+obj[4] + ".")
        return invent
    elif obj[5] == 1:
        armour.append(obj)
        print(pickUpMessage+obj[4] + ".")
        return armour
    elif obj[5] == 0:
        weapons.append(obj[4])
        print(pickUpMessage + obj[4] + ".")
        return weapons

#Function for removing an item from the inventory (& at the moment, removing said item from game)
def dropItem(obj):
    global armour, weapons
    if obj[5] == 0:
        weapons.remove(obj[4])
        print(dropItemMessage + obj[4] + ".")
        return weapons
    elif obj[5] == 1:
        armour.remove(obj[4])
        print(dropItemMessage + obj[4] + ".")
        return armour

#Function for equipping an item e.g Sword into your hand/Put on armour
def equipItem(obj, name):
    global armour, weapons
    print("obj =",obj)
    if obj == 0:
        weapon = name
        #Enter Addition To Stats (Waiting for finished weapons)
        print(currentHandItemMessage + str(name) + ".")
        return weapon
    elif obj == 1:
        armour = name
        ##endurance += int(armour[1])
        print(currentArmourMessage + str(name) + ".")
        return armour
    elif obj==2:
        print("clothing is not yet supported")
    else:
        print("error line 184")

#Function to unequip yet keep in inventory
def unEquipItem(obj):
    #not used
    global armour, weapons
    if obj == 1:
        #Resets name of current armour & resets the appropriate stats.
        armour = " "
        ##endurance -= obj[1]
        ##dexterity -= obj[2]
        print(unEquipArmourMessage)

    elif obj == 0:
        weapon = " "
        #Enter Reverse Stats of Weapon (Waiting for finished weapons)
        print(unEquipWeaponMessage)


#Testing... 1,2,3
def pinventory(currentHandItem,currentArmour):
    global inventry
    global armour, weapons
    length = 0
    while length<len(inventry):
        #print(inventry[length][4])
        length = length + 1
    print("You are currently holding:",weapons)
    print("You are currently wearing:",armour)
    print("Your options are:")
    print("unequip equip")
    pdecide = input()
    if pdecide == "equip":
        if len(inventry)==0:
            print("You havnt boughnt anything to equip")
        else:
            print("Choose what you want to equip")
            length=0
            while length<len(inventry):
                print("item number",length,"is",inventry[length][4])
                length = length + 1
            pequip = input("Enter item number")
            pequip = int(pequip)
            if pequip<=len(inventry):
                print(inventry)
                equipItem(inventry[pequip][6],inventry[pequip][4])
            else:
                print("item not found")
    if pdecide == "unequip":
        armour = ""
        weapn = ""
#--------------------------------------------------------------------------------------------------------------------------
#strengthm(0),endurancem(1),dexm(2),spellm(3),name(4),class(5),type(6),description(7),range(8),costs(9),costm(10),costl(11),costx(12)
#possible items to buy
warrior_basic_armour = [10,15,5,0,"basic warrior armour",1,1,"basic armour for beginners",0,30,0,0,0]
warrior_medium_armour = [15,20,10,0,"medium warrior armour",1,1,"better armour for the more experienced",0,45,0,0,0]
warrior_strong_armour = [20,35,15,0,"strong warrior armour",1,1,"very good quality armour",0,70,0,0,0]
warrior_elite_armour = [30,45,25,0,"elite warrior armour",1,1,"elite armour of a great quality",0,0,10,0,0]
warrior_ultimate_armour = [150,225,125,0,"hero's tunic",1,1,"armour of a legendary warrior",0,0,0,5,0]

mage_basic_armour = [0,5,10,15,"basic mage armour",2,1,"basic armour for beginners",0,30,0,0,0]
mage_medium_armour = [0,10,15,20,"medium mage armour",2,1,"better armour for the more experienced",0,45,0,0,0]
mage_strong_armour = [0,15,25,30,"strong mage armour",2,1,"very good quality armour",0,70,0,0,0]
mage_elite_armour = [0,25,35,40,"elite mage armour",2,1,"elite armour of a great quality",0,0,10,0,0]
mage_ultimate_armour = [0,125,175,400,"archmage's cloak",2,1,"WE NEED MORE FIREBALLS",0,0,0,5,0]

paladin_basic_armour = [5,20,5,0,"basic paladin armour",3,1,"basic armour for beginners",0,30,0,0,0]
paladin_medium_armour = [10,25,10,0,"medium paladin armour",3,1,"better armour for the more experienced",0,45,0,0,0]
paladin_strong_armour = [15,40,15,0,"strong paladin armour",3,1,"very good quality armour",0,70,0,0,0]
paladin_elite_armour = [25,50,25,0,"elite paladin armour",3,1,"elite armour of a great quality",0,0,10,0,0]
paladin_ultimate_armour = [125,250,125,0,"armour of favor",3,1,"comes witha cool ring!",0,0,0,5,0]

necromancer_basic_armour = [0,10,0,20,"basic necromancer armour",4,1,"basic armour for beginners",0,30,0,0,0]
necromancer_medium_armour = [0,20,0,25,"medium necromancer armour",4,1,"better armour for the more experienced",0,45,0,0,0]
necromancer_strong_armour = [0,30,0,40,"strong necromancer armour",4,1,"very good quality armour",0,70,0,0,0]
necromancer_elite_armour = [0,40,0,60,"elite nceromancer armour",4,1,"elite armour of a gret quality",0,0,10,0,0]
necromancer_ultimate_armour = [0,200,0,300,"gravelord's cloak",4,1,"cloak of the first of the dead",0,0,0,5,0]

barbarian_basic_armour = [15,5,10,0,"basic barbarian armour",5,1,"basic armour for beginners",0,30,0,0,0]
barbarian_medium_armour = [20,10,15,0,"medium barbarian armour",5,1,"better armour for the more experienced",0,45,0,0,0]
barbarian_strong_armour = [35,15,20,0,"strong barbarian armour",5,1,"very good quality armour",0,70,0,0,0]
barbarian_elite_armour = [45,25,30,0,"elite barbarian armour",5,1,"elite armour of a great quality",0,0,10,0,0]
barbarian_ultimate_armour = [225,125,150,0,"enraging armour",5,1,"get angry and smash!",0,0,10,0,0]

lancer_basic_armour = [20,0,10,0,"basic lancer armour",6,1,"basic armour for beginners",0,30,0,0,0]
lancer_medium_armour = [25,5,15,0,"medium lancer armour",6,1,"better armour for the more experienced",0,45,0,0,0]
lancer_strong_armour = [40,10,20,0,"strong laancer armour",6,1,"very good quality armour",0,70,0,0,0]
lancer_elite_armour = [50,20,30,0,"elite lancer armour",6,1,"elite armour of a great quality",0,0,10,0,0]
lancer_ultimate_armour = [250,100,150,0,"lancelord armor",6,1,"ancient lancer armour imbued with fire",0,0,0,5,0]

archer_basic_armour = [5,10,15,0,"basic archer armour",7,1,"basic armour for beginners",0,30,0,0,0]
archer_medium_armour = [10,15,20,0,"medium archer armour",7,1,"better armour for the more expeienced",0,45,0,0,0]
archer_strong_armour = [15,20,35,0,"strong archer armour",7,1,"very good quality armour",0,70,0,0,0]
archer_elite_armour = [25,30,45,0,"elite archer armour",7,1,"elite armour of a great qualit",0,0,10,0,0]
archer_ultimate_armour = [125,150,225,0,"armour of retribution",7,1,"will have your enemies quivering with fear!",0,0,0,5,0]

warrior_basic_weapon = [15,5,10,0,"basic warrior sword",1,0,"a basic sword for beginners",0,30,0,0,0]
warrior_medium_weapon = [20,10,15,0,"medium warrior sword",1,0,"a better sword for the more experienced",0,45,0,0,0]
warrior_strong_weapon = [35,15,20,0,"strong warrior sword",1,0,"a very good quality sword",0,70,0,0,0]
warrior_elite_weapon = [45,25,30,0,"elite warrior sword",1,0,"an elite sword of a great quality",0,0,10,0,0]
warrior_ultimate_weapon = [225,125,150,0,"the master sword",1,0,"we all know what this is",0,0,0,5,0]

mage_basic_weapon = [0,5,5,20,"basic mage wand",2,0,"a basic wand for beginners",0,30,0,0,0]
mage_medium_weapon = [0,10,10,25,"medium mage wand",2,0,"a better wand for the more experienced",0,45,0,0,0]
mage_strong_weapon = [0,15,15,40,"strong mage wand",2,0,"a very good quality wand",0,70,0,0,0]
mage_elite_weapon = [0,25,25,50,"elite mage wand",2,0,"an elite wand of a great quality",0,0,100,0,0]
mage_ultimate_weapon = [0,125,125,250,"veigar's staff",2,0,"the power to command dark matter is cool",0,0,0,5,0]

berserkers_band = [250,-50,0,0,"Beserkers band of destruction",0,2,"A long dead berserkers band that was enchanted with the power of satan",0,0,0,0,1]
priest_band = [0,100,0,50,"Priests saintly miracle band",0,2,"A saintly clerics lost wedding band",0,0,0,0,1]
#this needs to heal you for 25
Fire_gem_circlet = [0,0,50,150,"Fire gem circlet",0,2,"A gem formed in the fires of hell mounted onto a malachite circlet",0,0,0,0,1]
major_ring = [50,50,50,50,"Major ring of stat boosting",0,2,"A ring to make your power level over 9000",0,0,0,0,1]
ring_of_random_change = [0,0,0,0,"Ring of random change",0,2,"A ring that causes abnormalities in the atmosphere like hats coming out of rabbits",0,0,0,0,1]
#should do random things in battle like kill you or the enemy instantly
blinding_cranium_crab = [0,0,0,0,"Blinding cranium crab",0,2,"A crab for your cranium that jumps and blinds your foe lowering dexterity",0,0,0,0,1]
#should lower enemy dexterity
swiss_army_claymore = [50,0,50,0,"Swiss army claymore",0,2,"A fold out sword application for a strange swiss army knife",0,0,0,0,1]
#needs to make you go second every second turn and then give a strength boost of 200
arrow_target = [0,0,100,0,"Archery circlet of the pure archer",0,2,"An elven kings son once owned this crown and went on to defeat a dark lord",0,0,0,0,1]
#Should give a random chance to mean that all attacks by the player that turn become critical
blight_sludge = [0,0,0,0,"Blight sludge",0,2,"Some sludge taken from a poison riddled place that emanates death",0,0,0,0,1]
#Should deal poison damage over time to the enemy
overpowered_stick = [1000,1000,1000,1000,"The overpowered stick of doom",0,2,"A stick blessed with the power of bad coding",0,0,0,0,1]
#can only be used in one battle then it breaks and can't be used in boss battles
boss_shield = [0,200,0,0,"Boss shield of death",0,2,"A shield that is so big we didn't want to code it so here's a buckler",0,0,0,0,1]
#should protect from all damage for one turn once per battle (doesn't defend against magic)
sleepy_stick = [0,0,0,0,"sleepy stick",0,2,"a cursed squirrel on a stick",0,0,0,0,1]
#gives a chance to send enemies to sleep on a basic attack
lol = [50,50,50,50,"LOL",0,2,"An annoying snail because snails",0,0,0,0,1]
#should say lol at random points in battle
necrotic_bone = [0,0,100,50,"Necrotic bone",0,2,"A bone that was forced into a reverse body",0,0,0,0,1]
#should mean that your healing spells deal damage to the enemy instead.
mr_tiddles = [0,0,50,0,"Mr Tiddles",0,2,"A cat that is so buff that he buffs you!!!",0,0,0,0,1]
#should give you attack buffs based on your endurance

shop = []

items=[warrior_basic_armour,warrior_medium_armour,warrior_strong_armour,warrior_elite_armour,warrior_ultimate_armour,mage_basic_armour,mage_medium_armour,mage_strong_armour,mage_ultimate_armour,paladin_basic_armour,paladin_medium_armour,paladin_strong_armour,paladin_elite_armour,paladin_ultimate_armour,necromancer_basic_armour,necromancer_medium_armour,necromancer_strong_armour,necromancer_elite_armour,necromancer_ultimate_armour,barbarian_basic_armour,barbarian_medium_armour,barbarian_strong_armour,barbarian_elite_armour,barbarian_ultimate_armour,lancer_basic_armour,lancer_medium_armour,lancer_strong_armour,lancer_elite_armour,lancer_ultimate_armour,archer_basic_armour,archer_medium_armour,archer_strong_armour,archer_elite_armour,archer_ultimate_armour,warrior_basic_weapon,warrior_medium_weapon,warrior_strong_weapon,warrior_elite_weapon,warrior_ultimate_weapon,mage_basic_weapon,mage_medium_weapon,mage_strong_weapon,mage_elite_weapon,mage_ultimate_weapon] #maximum defininf length
items_accsesorys=[berserkers_band,priest_band,Fire_gem_circlet,major_ring,ring_of_random_change,blinding_cranium_crab,swiss_army_claymore,arrow_target,blight_sludge,overpowered_stick,boss_shield,sleepy_stick,lol,necrotic_bone,mr_tiddles] #add acsessorys to new array
items.extend(items_accsesorys) #add accsesorys to end of items array

item_no=0
while item_no < len(items):
    shop.append(str(items[item_no]))
    item_no=item_no+1

prices=[]

item_no=0
while item_no < len(items):
    place=amount(items, item_no)
    item_no=item_no+1
    prices.append(place)

place=[]

item_no=0
while item_no < len(items):
    places1=places(items, item_no)
    item_no=item_no+1
    place.append(places1)

store=[]
store.append(shop)
store.append(prices)
store.append(place)
#print(store)

#length of shop
length=len(store[1])
#inventry - place any starting items in array
inventry=[]
while 1>0:
    instruction=input("What would you like to do?")
    if instruction==("\money"):
        print("small orbs " + str(money[0]) + ", medium orbs " + str(money[1]) + ", large orbs " + str(money[2]) + ", special orbs " +str(money[3]))
    elif instruction==("\+money"):
        type=input("Small, Medium, Large or Special")
        amount=int(input("How much?"))
        if type=="S" or type=="M" or type=="L" or type=="X":
            change(money, type, amount)
        else:
            print("Enter capital: S,M,L or X only")
    elif instruction==("\shop"):
        loop=0
        while loop<length:
            #print("Item "+str(loop)+" - "+store[0][loop]+" costs "+store[1][loop]+" from obrb type "+store[2][loop])
            print("Item "+str(loop)+" - "+items[loop][4]+" costs "+str(store[1][loop])+" from obrb type "+str(store[2][loop]))
            loop=loop+1
        print("Type \"leave\" to leave shop")
        to_buy=input("Input item number to buy")
        check=is_number(to_buy) #check user has entered a number
        #check="TRUE" #uncomment to accept letters
        if check=="TRUE":
            if int(to_buy)<=int(length): #check number isnt too big
                print("You have attempted to buy "+str(items[int(to_buy)][4]))
                price=(store[1][int(to_buy)])
                type=store[2][int(to_buy)]
                if store[2][int(to_buy)]=="S":
                    amount=money[0]-int(price)
                    if amount<0:
                        print("You cannot afford that")
                    else:
                        change(money,type,amount)
                        inventry.append(items[int(to_buy)])
                        print("You have sucssesfully bought "+str(items[int(to_buy)][4]))
                elif store[2][int(to_buy)]=="M":
                    amount=money[1]-int(price)
                    if amount<0:
                        print("You cannot afford that")
                    else:
                        change(money,type,amount)
                        inventry.append(items[int(to_buy)])
                        print("You have sucssesfully bought "+str(items[int(to_buy)][4]))
                elif store[2][int(to_buy)]=="L":
                    amount=money[2]-int(price)
                    if amount<0:
                        print("You cannot afford that")
                    else:
                        change(money,type,amount)
                        inventry.append(items[int(to_buy)])
                        print("You have sucssesfully bought "+str(items[int(to_buy)][4]))
                elif store[2][int(to_buy)]=="X":
                    amount=money[3]-int(price)
                    if amount<0:
                        print("You cannot afford that")
                    else:
                        change(money,type,amount)
                        inventry.append(items[int(to_buy)])
                        print("You have sucssesfully bought "+str(items[int(to_buy)][4]))
            else:
                print("Error - item not recognised")
        else:
            print("Error - please enter a number, you have been returned to the main menu")
    elif instruction==("\data"):
        loop=0
        while loop<length:
            print("Item "+str(loop)+" - "+store[0][loop])
            loop=loop+1
        to_buy=input("Input item number to get data on")
        check=is_number(to_buy) #check user has entered a number
        #check="TRUE" #uncomment to accept letters
        if check=="TRUE":
            print("You have requested data on ",store[0][int(to_buy)])
            print("Strength = ",items[int(to_buy)][0])
            print("Endurance = ",items[int(to_buy)][1])
            print("Dexterity = ",items[int(to_buy)][2])
            print("Spell = ",items[int(to_buy)][3])
            #4 is used for name
            print("Class = ",items[int(to_buy)][5])
            print("Type = ",items[int(to_buy)][6])
            #7 used for description, placed at end
            print("Range = ",items[int(to_buy)][8])
            print("Bellow is a description of the item: \n,",items[int(to_buy)][7])
    elif instruction==("\convert"):
        convert_f=input("Convert from (S,M or L)")
        if convert_f=="S":
            print("You can only convert downwards.")
        elif convert_f=="M":
            amount=int(input("How many medium orbs would you like to convert?"))
            if money[1]>=amount:
                print("Ok")
                #Convert code to go here
            else:
                print("You don't have that many")
        elif convert_f=="L":
            amount=int(input("How many large orbs would you like to convert?"))
            if money[2]>=amount:
                print("Ok")
                #Convert code to go here
            else:
                print("You don't have that many")
        else:
            print("Error - use capital S, M and L only")
    elif instruction==("\inventory"):
        if len(inventry)==0:
            print("You have no items in your inventry")
        else:
            print("In your inventory you have: "+str(inventry))
    elif instruction==("\save"):
        file=open("inventory.txt","w")
        file.write(str(inventry))
        file.close()
        file=open("money_s.txt","w")
        file.write(str(money[0]))
        file.close()
        file=open("money_m.txt","w")
        file.write(str(money[1]))
        file.close()
        file=open("money_l.txt","w")
        file.write(str(money[2]))
        file.close()
        file=open("money_x.txt","w")
        file.write(str(money[3]))
        file.close()
        print("completed")
    elif instruction==("\load"):
        f = open("inventory.txt","r")
        inventry=[f.read()]
        f.close()
        money.pop() #not very clever way of deleted previous money
        money.pop()
        money.pop()
        money.pop()
        f = open("money_s.txt","r")
        s_money=f.read()
        f.close()
        f = open("money_m.txt","r")
        m_money=f.read()
        f.close()
        f = open("money_l.txt","r")
        l_money=f.read()
        f.close()
        f = open("money_x.txt","r")
        x_money=f.read()
        f.close()
        money.append(int(s_money))
        money.append(int(m_money))
        money.append(int(l_money))
        money.append(int(x_money))
        print("completed")
    elif instruction==("\clear"):
        os.remove("inventory.txt")
        os.remove("money_s.txt")
        os.remove("money_m.txt")
        os.remove("money_l.txt")
        os.remove("money_x.txt")
        print("completed")
    elif instruction==("\help"):
        print("Availbe commands: \n \shop = shop \n \money = see availbe orbs \n \+money = change current money \n \inventory = see items in inventory (to be removed). \n \management = manage your inventory & equip items. New way to see what you own. \n \data = find out the statistics of an item \n \save = save current inventory and money \n \load - load previous inventory and money - do not do this without saving a file first \n \clear = delete any save inventory and money")
    elif instruction==("\management"):
        pinventory(currentHandItem,currentArmour)
    else:
        print("Error - command not recognised - uses \"\help\" for a list of instructions.")
