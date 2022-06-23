"""start
regestred
non\regestred
admin
"""

def start():
    print('welcome to AIRLINE RESERVATIONS SYSTEM (ARS)\n')

    while True:
        print("\nPlease choose your membership")
        print(" [ 1 ] : Registered")
        print(" [ 2 ] : Not Registered")
        print(" [ 3 ] : Admin")
        print(" [ e ] : Exit")
        inp = input("\nChoice: ").replace(' ','')
        #try:
        if inp in ["e","r",""]:
            print("\nGood Bye!\n")
            break

        elif inp == "1":
            registered()
        elif inp == "2":
            not_registered()
        elif inp == "3":
            login_admin()
        else:
            print("\nPlease enter a valid choice:")

"""# registered"""

def registered():
    while True:
        print("\nRegistered Membership")
        print(" [ 1 ] : Log In")
        print(" [ r ] : Return")
        inp = input("\nChoice: ").lower().replace(' ','')

        if inp in ['','r']: break

        elif inp == "1":
            log_in()
        else:
            print("\nPlease enter a valid choice:")

def log_in():
    while True:
        users = {}
        with open('users.txt','r') as ff:
            for line in ff:
                users[line.strip().split(',')[0]] = line.strip().split(',')[1:]

        user_name = input("\nlogging in\nPlease Enter Your Username: (leave empty to return)\n\n").strip()

        if user_name in ['','r']:
            break

        elif users.get(user_name, False):

            print('\nlogged in successfully')
            registered_options(user_name,users)

        else:
            print("\nUsername {} Invalid,\n [ r ] : Return\n [ t ] : Try again".format(user_name))
            answer = input("\nChoice: ").replace(' ','')

            if answer in ['','r']: break

            elif answer == "t":
                pass
            else:
                print("\nPlease enter a valid choice:")

def registered_options(user_name,users):
    while True:
        print("\nRegistered Membership")
        print(" [ 1 ] : Display")
        print(" [ 2 ] : Add")
        print(" [ 3 ] : Modify")
        print(" [ r ] : Log out")

        inp3 = input("\nChoice: ").lower().replace(' ','')

        if inp3 in ['','r']: break

        # 1 Display
        elif inp3 == "1":
            registered_display(user_name,users)
            # complete

        elif inp3 == "2":
            registered_add(user_name)
                #Complete
        elif inp3 == "3":
            registered_modify(user_name,users)
            #Complete

        else:
            print("\nPlease enter a valid choice:")

def registered_display(user_name,users):
    while True:
        print("\nDisplay")
        print(" [ 1 ] : My Profile")
        print(" [ 2 ] : My Bookings")
        print(" [ r ] : return")

        inp4 = input("\nChoice: ").lower().replace(' ','')

        if inp4 in ["r",""]: break

        elif inp4 == "1":
            print("\nMy Profile\n")
            titls = "Username,Name,Phone No,Citizenship,Email,Travel Doc Det,Emerg Contact,Saved Paynment"
            values = [user_name] + users[user_name]
            titls = titls.split(",")
            for i,v in enumerate(titls):
                print(i,v,":",values[i])

        elif inp4 == "2":
            print("\nMy Bookings\n")

            with open('Book2.txt','r') as ffdb:
                lldb = ffdb.read().splitlines()
                out = []

                for line in lldb:
                    line = line.strip().split(',')
                    if line[0].strip() == user_name:
                        out.append(' '.join([word + " "*(15-len(word)) for word in line]))

                if len(out) > 0:
                    print()
                    print(' '.join([word + " "*(15-len(word)) for word in lldb[0].split(',')]))
                    [print(pl) for pl in out]

                else:
                    print("No Brookings")

def registered_add(user_name):
    print("Add")
    print(" [ 1 ] : Flight")
    print(" [ r ] : Return")

    inp5 = input("\nChoice: ").lower().replace(' ','')

    if inp5 in ["r",""]:
        pass

    elif inp5 == "1":
        with open('Book1.txt','r') as ffnr:
            ll = ffnr.read().splitlines()

        for i,line in enumerate(ll):
            line = line.strip().split(',')
            print(i,' '.join([word + " "*(15-len(word)) for word in line]))

        while True:
            try:
                inp511 = input("\nplease choose flight number: ").replace(' ','')
                inp51 = int(inp511)
            except:
                if inp511 in ['','r']: break
                inp51 = 0
                print('\nplease enter a valid number')

            if inp51 not in list(range(1,len(ll))):
                print(f'please choose a flight between 1 - {len(ll)-1}')
                continue

            else:
                data = '\n' +",".join([user_name,ll[inp51]])

                with open('Book2.txt','a') as ff2:
                    ff2.write(data)

                print('added the flight{}'.format(ll[inp51].split(',')[0]))
                break

def registered_modify(user_name, users):
    while True:
        print("Modify")
        print(" [ 1 ] : My Account")
        print(" [ r ] : return")

        inp6 = input("\nChoice: ").lower().replace(' ','')

        if inp6 in ["r",""]:
            break

        elif inp6 == "1":
            # display the current profile
            titls = "Username,Name,Phone No,Citizenship,Email,Travel Doc Det,Emerg Contact,Saved Paynment".split(",")
            values = [user_name] + users[user_name]
            for i,v in enumerate(titls):
                print(i,v,":",values[i])

            while True:
                #get numeric value
                inp511 = input("\nplease choose the number of what you want to modify: ").replace(' ','')
                if inp511 in ['','r']:
                    #c_var = false
                    break
                try:
                    inp51 = int(inp511)
                except:
                    #if not numeric
                    inp51 = 0
                    print('\nplease enter a valid number')


                if inp51 not in list(range(1,len(values))):
                    print(f'please choose a property between 1 - {len(values)-1}')
                    continue

                else:
                    values[inp51] = input("\nplease enter the new value of {}: ".format(titls[inp51])).replace(' ','')
                    print("\nThe new value of '",titls[inp51],"'is",values[inp51])
                    new_data = values
                    #get lines
                    with open("users.txt", "r") as a_file:
                        list_of_lines = a_file.readlines()

                    #edit date
                    out = []
                    for line in list_of_lines:
                        if line.strip().split(",")[0] == user_name:
                            out.append(",".join(new_data)+"\n")
                        else:
                            out.append(line)
                    #save changes
                    with open("users.txt", "w") as a_file:
                        a_file.writelines("".join(out))
                    break
        else:
            print("\nPlease enter a valid choice:")

""" not registered """

def not_registered():

    while True:
        print("\nUn Registered Membership")
        print(" [ 1 ] : Display all airline schedules")
        print(" [ 2 ] : Search airlines")
        print(" [ 3 ] : Register")
        print(" [ r ] : Return")

        inp = input("\nChoice: ").lower().replace(' ','')

        if inp in ["r",""]:
            break

        elif inp == "1":
            print("\nDisplay all airline schedules\n")

            with open('Book1.txt','r') as ffnr:
                ll = ffnr.read().splitlines()
            for line in ll:
                line = line.strip().split(',')
                print(' '.join([word + " "*(15-len(word)) for word in line]))

        elif inp == "2":
            while True:
                print("\nSearch airlines by:\n")
                print(" [ 1 ] : From")
                print(" [ 2 ] : To")
                print(" [ 3 ] : date departure")
                print(" [ 4 ] : date return")
                print(" [ r ] : return")

                with open('Book1.txt','r') as ffnr:
                    ll = ffnr.read().splitlines()

                inps = input("\nChoice: ").lower().replace(' ','')

                if inps in ['','r']: break

                elif inps == "1":
                        while True:
                            print("\nSearch airlines by: 'From'")
                            inpsfr = input("\nFrom: (empty or 'r' to return) ").strip()
                            inpsf = inpsfr.lower()

                            if inpsf in ['','r']: break

                            out = []

                            for line in ll:
                                line = line.strip().split(',')
                                if line[1].lower().strip() == inpsf:
                                    out.append(' '.join([word + " "*(15-len(word)) for word in line]))

                            if len(out) > 0:
                                print()
                                print(' '.join([word + " "*(15-len(word)) for word in ll[0].split(',')]))
                                [print(pl) for pl in out]

                            else:
                                print("No airlines From '{}'\n".format(inpsfr))

                #end search by form

                # start search by to
                elif inps == "2":
                    while True:
                        print("\nSearch airlines by: 'To'")
                        inpsfr = input("\nTo: (empty or 'r' to return) ").strip()
                        inpsf = inpsfr.lower()

                        if inpsf in ['','r']: break

                        out = []

                        for line in ll:
                            line = line.strip().split(',')
                            if line[2].lower().strip() == inpsf:
                                out.append(' '.join([word + " "*(15-len(word)) for word in line]))

                        if len(out) > 0:
                            print()
                            print(' '.join([word + " "*(15-len(word)) for word in ll[0].split(',')]))
                            [print(pl) for pl in out]

                        else:
                            print("No airlines To '{}'\n".format(inpsfr))
                #end search by To

                elif inps == "3":
                    while True:
                        print("\nSearch airlines by: 'Date departure'")
                        inpsfr = input("\nDate departure dd/mm/yyyy: (empty or 'r' to return) ").strip()
                        inpsf = inpsfr.lower()

                        if inpsf in ['','r']: break

                        out = []

                        for line in ll:
                            line = line.strip().split(',')
                            if line[3].lower().strip() == inpsf:
                                out.append(' '.join([word + " "*(15-len(word)) for word in line]))

                        if len(out) > 0:
                            print()
                            print(' '.join([word + " "*(15-len(word)) for word in ll[0].split(',')]))
                            [print(pl) for pl in out]

                        else:
                            print("No airlines departure at '{}'\n".format(inpsfr))

                #end search by date departure

                elif inps == "4":
                    while True:
                        print("\nSearch airlines by: 'date return'")
                        inpsfr = input("\ndate return dd/mm/yyyy: (empty or 'r' to return) ").strip()
                        inpsf = inpsfr.lower()

                        if inpsf in ['','r']: break

                        out = []

                        for line in ll:
                            line = line.strip().split(',')
                            if line[4].lower().strip() == inpsf:
                                out.append(' '.join([word + " "*(15-len(word)) for word in line]))

                        if len(out) > 0:
                            print()
                            print(' '.join([word + " "*(15-len(word)) for word in ll[0].split(',')]))
                            [print(pl) for pl in out]

                        else:
                            print("No airlines return at '{}'\n".format(inpsfr))

                #end search by date return

                else:
                    print("\nPlease enter a valid choice:")

        elif inp == "3":
            just_registered = False
            user_data = False

            while True:

                users = {}

                with open('users.txt','r') as ff2:
                    for line in ff2:
                        users[line.strip().split(',')[0]] = line.strip().split(',')[1:]

                print("\nRegistering\nPlease Enter Your Username: (leave empty to return)")
                user_name = input("\nChoice: ").replace(' ','')

                if user_name == '': break

                elif users.get(user_name, False):
                    print("\nUsername '{}' is Taken".format(user_name))
                    continue

                else:

                    while True:

                        print("\nUsername {} is Available,\n [ s ] : Save and Register\n [ r ] : Return".format(user_name))
                        answer = input("\nChoice: ").replace(' ','')

                        if answer in ['','r']: break

                        elif answer == "s":
                            user_data = save_username(user_name)
                            break
                        else:
                            print("\nPlease enter a valid choice:")

                    if user_data:
                        just_registered = True
                        break
            if just_registered: break
        else:
            print("\nPlease enter a valid choice:")

def save_username(username):
    print("\nCreating Profile Username: '{}' \n".format(username))
    while True:
        name = input('\nEnter your Name: ')
        if name == '':
            print("\nPlease enter a valid Name")
            continue
        else:
            break
    while True:
        phone = input('\nEnter your Phone no: ')
        if phone == '':
            print("\nPlease enter a valid Phone no")
            continue
        else:
            break
    while True:
        citizenship = input('\nEnter your Citizenship: ')
        if citizenship == '':
            print("\nPlease enter a valid Citizenship")
            continue
        else:
            break
    while True:
        email = input('\nEnter your Email: ')
        if email == '':
            print("\nPlease enter a valid Email")
            continue
        else:
            break
    while True:
        travel_doc = input('\nEnter your Travel Document Details: ')
        if travel_doc == '':
            print("\nPlease enter a valid Travel Document Details")
            continue
        else:
            break
    while True:
        e_contact = input('\nEnter your Emergency Contact: ')
        if e_contact == '':
            print("\nPlease enter a valid Emergency Contact")
            continue
        else:
            break
    while True:
        p_datails = input('\nEnter your Saved Paynment Details: ')
        if p_datails == '':
            print("\nPlease enter a valid Saved Paynment Details")
            continue
        else:
            break
    data = ",".join([username,name,phone,citizenship,email,travel_doc,e_contact,p_datails])
    with open('users.txt','a') as ff2:
        ff2.write('\n')
        ff2.write(data)
        ff2.close()

    print("\nProfile Created Username: '{}'".format(username))
    return True

"""#admin"""

def login_admin():
    while True:
        loogin_in = False
        admins = {}
        with open('admins.txt','r') as ff:
            for line in ff:
                line = line.strip().split(',')
                admins[line[0]] = line[1]

        user_name = input("\nlogging in\n\nPlease Enter Your Username: (leave empty to return)\n\n").strip()

        if user_name in ['','r']:
            break

        elif admins.get(user_name, False):
            while True:
                password = input("\nPlease Enter Your password: (leave empty to return)\n\n").strip()
                if password in ['','r']:
                    break
                elif admins.get(user_name, False) == password.strip():
                    print('\nlogged in successfully')
                    loogin_in = True
                    break
                else:
                    print("\npassword incorrect")
                
        else:
            print("\nUsername {} Invalid".format(user_name))
        if loogin_in:
            admin()

def admin():
    while True:
        print("\nADMIN")
        print(" [ 1 ] : Add Flight Schedules")
        print(" [ 2 ] : Modify Flight Schedules")
        print(" [ 3 ] : Display")
        print(" [ r ] : Return")

        inp = input("\nChoice: ").lower().replace(' ','')

        if inp in ['','r']:
            break
        elif inp == "1":
            add_flight()
        elif inp == "2":
            modify_flight()
        elif inp == "3":
            display_flight()
        else:
            print("\nPlease enter a valid choice:")

def display_flight():
    while True:
        print("\nADMIN Display")
        print(" [ 1 ] : Flight schedules by flight number")
        print(" [ 2 ] : Flight booked by customer")
        print(" [ 3 ] : Total tickets ")
        print(" [ r ] : Return")

        inp = input("\nChoice: ").lower().replace(' ','')

        if inp in ['','r']:
            break
        elif inp == "1":
            display_flights_name()
        elif inp == "2":
            while True:
                user = input('\nEnter user name (r or blank to return)').strip()
                if user in ['','r']:
                    break
                else:
                    display_flights_user(user)
        elif inp == "3":
            display_flights_users()
        else:
            print("\nPlease enter a valid choice:")

def display_flights_name():
    with open('Book1.txt','r') as ffnr:
        ll = ffnr.read().splitlines()
    for line in ll:
        line = line.strip().split(',')
        print(' '.join([word + " "*(15-len(word)) for word in line]))

def display_flights_user(user):
    out =[]
    with open('Book2.txt','r') as ffnr:
        ll = ffnr.read().splitlines()
    for line in ll:
        line = line.strip().split(',')
        if line[0].strip() == user:
            out.append(' '.join([word + " "*(15-len(word)) for word in line]))

    if len(out) > 0:
        print()
        print(' '.join([word + " "*(15-len(word)) for word in ll[0].split(',')]))
        [print(pl) for pl in out]
    else:
        print('\nno flights found')

def display_flights_users():
    with open('Book2.txt','r') as ffnr:
        ll = ffnr.read().splitlines()
    for line in ll:
        line = line.strip().split(',')
        print(' '.join([word + " "*(15-len(word)) for word in line]))

def modify_flight():
    flight_data=open('Book1.txt','r')
    flightdata_list = flight_data.readlines()
    flight_data.close()
    print(flightdata_list)
    flight_no=input("\n Enter Flight number you want to modify :")
    for i,val in enumerate(flightdata_list):
        data_str=val.split(',')
        if(data_str[0]==flight_no):
            index2modify=i
    
    print("Modifying the flight with flight number '{}' at index {}".format(flight_no,index2modify))

    while True:
        flight_number = input('\nEnter Flight Number (This data will be modified): ')
        if flight_number == '':
            print("\nPlease enter a valid 'Flight Number'")
            continue
        else:
            break
    while True:
        fromm = input("\nEnter 'From': ")
        if fromm == '':
            print("\nPlease enter a valid 'From'")
            continue
        else:
            break
    while True:
        too = input('\nEnter "To": ')
        if too == '':
            print("\nPlease enter a valid 'To'")
            continue
        else:
            break
    while True:
        date_departure = input('\nEnter Date Departure: ')
        if date_departure == '':
            print("\nPlease enter a valid Date Departure")
            continue
        else:
            break
    while True:
        date_return = input('\nEnter Date Return: ')
        if date_return == '':
            print("\nPlease enter a valid Date Return")
            continue
        else:
            break
    while True:
        ticket = input('\nEnter ticket: ')
        if ticket == '':
            print("\nPlease enter a valid ticket")
            continue
        else:
            break

    data =  ",".join([flight_number,fromm,too,date_departure,date_return,ticket])
    
    print("\n The following details are updating...")
    print(flightdata_list[index2modify])

    print("The Details are updated to ...")
    print(data)
    flightdata_list[index2modify]=data+'\n'
    flight_data=open('Book1.txt','w')
    modified_data=''.join(flightdata_list)
    flight_data.write(modified_data)
    flight_data.close()

    print("\n Your Flight has been modified")


def add_flight():
    while True:
        flight_number = input('\nEnter Flight Number: ')
        if flight_number == '':
            print("\nPlease enter a valid 'Flight Number'")
            continue
        else:
            break
    while True:
        fromm = input("\nEnter 'From': ")
        if fromm == '':
            print("\nPlease enter a valid 'From'")
            continue
        else:
            break
    while True:
        too = input('\nEnter "To": ')
        if too == '':
            print("\nPlease enter a valid 'To'")
            continue
        else:
            break
    while True:
        date_departure = input('\nEnter Date Departure: ')
        if date_departure == '':
            print("\nPlease enter a valid Date Departure")
            continue
        else:
            break
    while True:
        date_return = input('\nEnter Date Return: ')
        if date_return == '':
            print("\nPlease enter a valid Date Return")
            continue
        else:
            break
    while True:
        ticket = input('\nEnter ticket: ')
        if ticket == '':
            print("\nPlease enter a valid ticket")
            continue
        else:
            break

    data =  '\n' +",".join([flight_number,fromm,too,date_departure,date_return,ticket])
    with open('Book1.txt','a') as ff2:
        ff2.write(data)

    print("\nFlight Created flight number: '{}'".format(flight_number))

if(__name__=='__main__'):
    start()
