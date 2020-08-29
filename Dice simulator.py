from random import randint
def play():
    x = randint(1,6)
    if x==1:
        print '-------'
        print '|     |'
        print '|  0  |'
        print '|     |'
        print '-------'
    elif x==2:
        print '-------'
        print '|     |'
        print '| 0 0 |'
        print '|     |'
        print '-------'
    elif x==3:
        print '--------'
        print '|    0 |'
        print '|  0   |'
        print '|0     |'
        print '--------'
    elif x==4:
        print '--------'
        print '|0    0|'
        print '|0    0|'
        print '--------'
    elif x==5:
        print '-------'
        print '| 0 0 |'
        print '|  0  |'
        print '| 0 0 |'
        print '-------'
    else:
        print '-------'
        print '| 0 0 |'
        print '| 0 0 |'
        print '| 0 0 |'
        print '-------'
    user = raw_input('Press y to roll dice or n to quit: ')
    if user=='y':
        play()
    else:
        print 'Thank you'
print 'Initial dice..'
play()