import RE as mac

rotors,rings,initialRotPos,plugboard,reflector = [],[],[],"",""

#Select_Settings
def selectSettings(fullSettings=True):
    global rotors,rings,initialRotPos,plugboard,reflector
    if fullSettings == True:
        # Getting Rotor Order
        inp = input("Rotor (Eg : I-S-III-S-VI-S-X-S-IX): ").upper().split("-S-")
        rotors = ['I','II','III','IV','V'] if inp == [''] else inp

        # Getting Reflector
        inp = input("Reflector (A/B/C/D) : ").upper()
        reflector = 'A' if inp == '' else inp

        #Getting RingSetting
        inp = input("Rings of Rotors (Eg : A-S-8-S-$-S-V-S-!): ").replace('-s-','-S-').split("-S-")
        rings = ['A','A','A','A','A'] if inp == [''] else inp

        #Getting Plugboard Setting
        plugboard = input("Plugboard Pairs - Eg : a^-s-Cd-s-e1-s-*/-s-45 : ").replace('-s-','-S-')
        
        #initialSetting
        inp = input("Rotor initial setting (Eg : Q-S-#-S-R-S-@-S-1) : ").replace('-s-','-S-').split("-S-")
        initialRotPos = ['A','A','A','A','A'] if inp == [''] else inp

    else:

        #initialSetting
        inp = input("Rotor initial setting (Eg : Q-S-#-S-R-S-@-S-1) : ").replace('-s-','-S-').split("-S-")
        initialRotPos = ['A','A','A','A','A'] if inp==[''] else inp
        
    #setting machine
    re.Settings(rotors[0],rotors[1],rotors[2],rotors[3],rotors[4],rings[0],rings[1],rings[2],rings[3],rings[4],initialRotPos[0],initialRotPos[1],initialRotPos[2],initialRotPos[3],initialRotPos[4],plugboard,reflector)

def displaySettings():
    R1,R2,R3,R4,R5,r1,r2,r3,r4,r5,i1,i2,i3,i4,i5,plugBoard,reflector = re.getDetails()
    print()
    print("Rotor Settings : ",R1,R2,R3,R4,R5)
    print("Ring Settings : ",r1,r2,r3,r4,r5)
    print("Initial Settings : ",i1,i2,i3,i4,i5)
    print("Plugboard : ",plugBoard)
    print("Reflector : ",reflector)

def displayRotorSettings():
    R1,R2,R3,R4,R5 = re.getCurrentRotorPos()
    print('\t',R1,R2,R3,R4,R5)

re = mac.RE()
re.Settings()
ch,settingsFlag = 0,0

while ch != 5:
    try:
        print("\n\tMENU\n1.Settings\n2.Initial Setting\n3.Display Settings\n4.Type\n5.Exit")
        ch = input("Enter your choice : ")
        if ch == '1':
            selectSettings()
            settingsFlag=1
        elif ch == '2':
            selectSettings(False)
        elif ch == '3':
            displaySettings()
        elif ch == '4':
            if settingsFlag != 0:
                print()
                displayRotorSettings()
                print()
                message = input("Enter a message   : ")
                print("Encrypted Message :",re.typeMessage(message))
            else:
                selectSettings()
                settingsFlag = 1
                print()
                displayRotorSettings()
                print()
                message = input("Enter a message   : ")
                print("Encrypted Message :",re.typeMessage(message))
        elif ch == '5':
            break
        else:
            print('\n\t"Invalid choice"')
    except:
        print("\n\tInput values correctly !")