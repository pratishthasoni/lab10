import flights

f = flights.Flights('f.dat')
#f.add_flight('LAX','ORD','545','1230','N','1640')
#f.add_flight('ORD','CLE','409','1733','N','1857')
#f.add_flight('CLE','IAD','83','1953','N','2119')
#f.add_flight('IAD','LHR','999','2200','Y','0530')

while True:
    print("      *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU")
    print()
    print("1. Add flight")
    print("2. Print flight schedule")
    print("3. Set flight schedule filename")
    print("9. Exit the program")
    print()
    choice = int(input("Enter menu choice: "))
    print()

    # ADD FLIGHT
    if choice == 1:
        org = input("Enter origin: ")
        dest = input("Enter destination: ")
        num = input("Enter flight number: ")
        dep = input("Enter departure time (HHMM): ")
        arr = input("Enter arrival time (HHMM): ")
        next_day = input("Is arrival next day (Y/N): ")
        f.add_flight(org, dest, num, dep, next_day, arr)
        print()

    # PRINT FLIGHT SCHEDULE
    elif choice == 2:
        fts = f.get_flights()
        print("================== FLIGHT SCHEDULE ==================")
        print('Origin Destination Number Departure  Arrival Duration')
        print('====== =========== ====== ========= ======== ========')
        for x in fts:
            org = x[0]
            dest = x[1]
            num = x[2]
            dep = x[3]
            arr = x[4]
            dur = x[5]
            print(f'{org:7}{dest:12}{num:>6}{dep:>10}{arr:>9}{dur:>9}')
        print()

    # SET FLIGHT SCHEDULE FILENAME
    elif choice == 3:
        fn = input("Enter new filename: ")
        f = flights.Flights(fn)
        print()

    #EXIT
    elif choice == 9:
        break;
