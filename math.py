#!/usr/bin/env python3
import random
score=0

try:
    while True:
        n1= random.randint(1, 10)
        n2= random.randint(1, 10)
        op= random.choice(['+', '-', '*'])
        st=str(n1) + op + str(n2)
        re=eval(st)
        print(st+'=?')
        while True:
            inpt=int(input('>>'))
            if inpt==re:
                print('Correct!')
                score+=1
                break
            else:
                print('Wrong!')
                score-=1
except KeyboardInterrupt:
    print('\nGame Over!')
    print('Score: '+str(score))