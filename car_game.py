started = False

while True:
    command = input('> ').lower()
    if command == "start":
        if started:
            print('Car is already started!')
        else:
            print("Car started... Ready to go!")
            started = True
    elif command == 'stop':
        if not started:
            print('Car is already stopped!')
        else:
            print('Car stopped.')
            started = False
    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit''')
    elif command == "quit":
        break
    else:
        print('I dont understand')
