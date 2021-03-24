
help = '''
start - To start you car 
stop - to stop the car
quit - to exit
'''

###if car is already started give message
started = False
while True:
    x = (input('>'))
    x = x.lower()
    if x == 'help':
        print (help)
    elif x == 'start':
        if started:
            print('car is already started')
        else:
            started = True
            print('Car started...Ready to go')
    elif x == 'stop':
        if not started:
            print('Car is already stopped')
        else:
            started = False
            print('Car Stopped')
    elif x == 'quit':
        break
    else:
        print('I dont understand that...')

    
