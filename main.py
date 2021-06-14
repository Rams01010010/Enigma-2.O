import Eni2 as rse

rotor,rings,Rot,plugb,reflector = [],[],[],'',''

#Enigma Settings
def select_settings(isFullSetting=True):

    global rotor,rings,Rot,plugb,reflector
    
    if isFullSetting == True:
        
        # Getting Rotor Order
        x = input("Rotor (Eg : I-S-III-S-VI-S-X-S-IX): ").upper().split("-S-")
        rotor = ['I','II','III','IV','V'] if x == [''] else x
        
        # Getting Reflector
        x = input("Reflector (A/B/C/D) : ").upper()
        reflector = 'A' if x == '' else x

        #Getting RingSetting
        x = input("Rings of Rotors (Eg : A-S-8-S-$-S-V-S-!): ").split("-S-")
        rings = ['A','A','A','A','A'] if x == [''] else x

        #Getting Plugboard Setting
        plugb = input("Plugboard Pairs - Eg : a^-s-Cd-s-e1-s-**-s-45 : ").replace('-s-','-S-')
        
        #initialSetting
        x = input("Rotor initial setting (Eg : Q-S-#-S-R-S-@-S-1) : ").split("-S-")
        Rot = ['A','A','A','A','A'] if x == [''] else x

    else:
        #initialSetting
        x = input("Rotor initial setting (Eg : Q-S-#-S-R-S-@-S-1) : ").split("-S-")
        Rot = ['A','A','A','A','A'] if x == [''] else x

    #setting machine
    rs.setter(rotor[0],rotor[1],rotor[2],rotor[3],rotor[4],rings[0],rings[1],rings[2],rings[3],rings[4],plugb,reflector,Rot[0],Rot[1],Rot[2],Rot[3],Rot[4])

def start():
    plainMsg = input("Enter message : ")
    encryptedMsg = ''
    for i in plainMsg:
        encryptedMsg += rs.typeMsg(i)
    print("\nEncrypted Msg : "+str(encryptedMsg))

def displayCurrentSetting():
    R1,R2,R3,R4,R5,r1,r2,r3,r4,r5,plugBoard,reflector,i1,i2,i3,i4,i5 = rs.getter()
    print()
    print("Rotor Settings : ",R1,R2,R3,R4,R5)
    print("Ring Settings : ",r1,r2,r3,r4,r5)
    print("Initial Settings : ",i1,i2,i3,i4,i5)
    print("Plugboard : ",plugBoard)
    print("Reflector : ",reflector)

def displayRotorSettings():
    R1,R2,R3,R4,R5 = rs.getRotorPosition()
    print('\t',R1,R2,R3,R4,R5)
    
ch = 0

rs = rse.ENIGMA()
rs.setter()
f = 0
while ch != 5:
    try:
        print("\n\tMENU\n1.Settings\n2.Initial Setting\n3.Start\n4.Display Settings\n5.Exit")
        ch = input("Enter your choice : ")
        if ch == '1':
            select_settings()
            f=1
        elif ch == '2':
            select_settings(False)
        elif ch == '3':
            if f != 0:
                print()
                displayRotorSettings()
                print()
                start()
            else:
                select_settings()
                f = 1
        elif ch == '4':
            displayCurrentSetting()
        elif ch == '5':
            break
        else:
            print('\n\t"Invalid choice"')
    except:
        print("\n\tInput values correctly !")