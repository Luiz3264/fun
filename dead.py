#!/usr/bin/env python3
import random
import time

name=[
    'Bob','Dave','Eric','Frank',
    'George','Harry','Jack','Kevin',
    'Leo','Mike','Nate','Oscar',
    'Paul','Quinn','Ryan','Steve',
    'Tom','Victor','Will','Zack'
]

monster=[
    'Goblin','Skeleton','Zombie','Orc',
    'Slime','Giant Spider','Giant Rat','Rat King',
    'Ghost','Vampire','Werewolf','Demon',
    'Spirit','Rat','Snake','Giant Snake'
]

food=[
    'apple','bread','meat','cheese',
    'mushroom','berry','fish','egg',
    'fruit','vegetable','candy','potion',
    'stew','soup','pie','cake'
]

run=True
score=0

print('DEAD v0.8')
print('====-=-=---- - -')
hp=random.randint(1,6)*10
dm=random.randint(1,6)*5
print(random.choice(name),'is entering dungeon...')
time.sleep(1)

while run:
    dice=random.randint(1,6)
    if dice==1:
        print('...')
    elif dice==2:
        print('Found',random.choice(food),'!')
        if random.randint(0,1)==1: hp+=10
        else: dm+=5
        score+=10
    elif dice==3:
        print(random.choice(monster),'appears!')
        monster_hp=random.randint(1,hp+10)
        monster_dm=random.randint(1,dm+5)
        while monster_hp>0 and hp>0:
            monster_hp-=random.randint(0,dm)
            hp-=random.randint(0,monster_dm)
            time.sleep(1)
        if hp<=0:
            print('Died!')
            run=False
        else:
            print('Won!')
        score+=random.randint(1,monster_dm)*10
    elif dice==4:
        print('Treasure!')
        score+=random.randint(1,10)*10
    elif dice==5:
        print('Trap!')
        hp-=random.randint(1,10)*5
        if hp<=0:
            print('Died!')
            run=False
    elif dice==6:
        print('Blessed!')
        hp+=random.randint(1,10)*5
        dm+=random.randint(1,10)*5
    time.sleep(1)
print('- - - -')
print('Score:',score)
input('Press Enter to exit...')