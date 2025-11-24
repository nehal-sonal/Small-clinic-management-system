FILE = "patients.txt"

def ensurefe():
    f = open(FILE, "a")
    f.close()

def readal():
    f = open(FILE)
    lst = f.readlines()
    f.close()
    return lst

def writeal(lst):
    f = open(FILE, "w")
    for x in lst:
        f.write(x)
    f.close()

def addpat():
    print("\nAdd new patient")
    pid = input("Enter patient id:")
    pname = input("Enter patient Name:")
    page = input("Enter Age:")
    pgen = input("Enter Gender:")

    phist = "None"
    papp = "None"

    rec = pid + "|" + pname + "|" + page + "|" + pgen + "|" + phist + "|" + papp + "\n"

    f = open(FILE, "a")
    f.write(rec)
    f.close()

    print("Patient successfully added!\n")

def view_patient():
    print("\nView patient details")
    pid = input("Enter patient id:")
    lst = readal()

    found = False

    for line in lst:
        row = line.strip().split("|")
        if row[0] == pid:
            print("\nPatient record found")
            print("Patient id     :", row[0])
            print("Name           :", row[1])
            print("Age            :", row[2])
            print("Gender         :", row[3])
            print("History Notes  :", row[4])
            print("Appointments   :", row[5])
            print()
            found = True
            break

    if not found:
        print("No patient found with this id\n")

def patientlist():
    print("\nAll patient records")
    lst = readal()

    if len(lst) == 0:
        print("patient records unavailable\n")
        return

    for line in lst:
            row = line.strip().split("|")
            print("id:", row[0], "| Name:", row[1], "| Age:", row[2], "| Gender:", row[3])
    print()         

def namesearch():
    print("\nSearch by patient name")
    key = input("Enter name to search: ").lower()
    lst = readal()

    found = False

    for line in lst:
        row = line.strip().split("|")
        if key in row[1].lower():
            print("id:", row[0], "| Name:", row[1], "| Age:", row[2], "| Gender:", row[3])
            found = True

    if not found:
        print("No matchiing patient found\n")
    else:
        print()

def addapp():
    print("\nAdd appointment")
    pid = input("Enter patient id: ")
    lst = readal()

    new_lst = []
    found = False

    for line in lst:
        row = line.strip().split("|")

        if row[0] == pid:
            app_date = input("Enter Date (dd/mm/yyyy): ")
            app_reason = input("Enter Reason:")

            if row[5] == "None":
                row[5] = app_date + "-" + app_reason
            else:
                row[5] = row[5] + " || " + app_date + "-" + app_reason

            found = True

        new_lst.append("|".join(row) + "\n")

    writeal(new_lst)

    if found:
        print("Appointment added successfully\n")
    else:
        print("Patient id not found\n")

def histadd():
    print("\nAdd medical history")
    pid = input("Enter patient id:")
    lst = readal()

    new_lst = []
    found = False

    for line in lst:
        row = line.strip().split("|")

        if row[0] == pid:
            note = input("Enter history note:")

            if row[4] == "None":
                row[4] = note
            else:
                row[4] = row[4] + " || " + note

            found = True

        new_lst.append("|".join(row) + "\n")

    writeal(new_lst)

    if found:
        print("History updated successfully\n")
    else:
        print("Patient not found\n")

def patedit():
    print("\nEdit patient info")
    pid = input("Enter patient id - ")
    lst = readal()

    new_lst = []
    found = False

    for line in lst:
        row = line.strip().split("|")

        if row[0] == pid:
            print("\nNew Name:", row[1])
            new_name = input("Enter new name (or press Enter to keep): ")
            if new_name != "":
                row[1] = new_name

            print("New Age:", row[2])
            new_age = input("Enter new age (or press Enter to keep): ")
            if new_age != "":
                row[2] = new_age

            print("C+New Gender:", row[3])
            new = input("Enter new gender (or press Enter to keep): ")
            if new != "":
                row[3] = new

            found = True
        newlst.append("|".join(row) + "\n")

    writeal(newlst)

    if found:
        print("Patient detail record is updated\n")
    else:
        print("Patient id not found\n")

def delpat():
    pid = input("To delete patient details Enter patient id to delete: ")
    lst = readal()

    new_lst = []
    deleted = False

    for line in lst:
        row = line.strip().split("|")
        if row[0] != pid:
            new_lst.append(line)
        else:
            deleted = True

    writeal(new_lst)

    if deleted:
        print("Patient record deleted\n")
    else:
        print("Patient not found\n")

def car():
    print("\nWarning: This will delete all patient records!")
    confirm = input("Type Yes to confirm:")

    if confirm == "Yes":
        writeal([])
        print("All record have been cleared\n")
    else:
        print("Operation is cancelled as the user wanted it \n")

def showstat():
    print("\nClinic statistics from the patient records")
    lst = readal()

    total = len(lst)
    male = 0
    female = 0

    for line in lst:
        row = line.strip().split("|")
        if row[3].lower() == "male":
            male=male+1
        elif row[3].lower() == "female":
            female=female+1

    print("Total No. of patients :", total)
    print("No. of Male patients  :", male)
    print("No. of Female patients:", female)
    print()

def all():
    ensurefe()

    while True:
        print("\nSmall Clinic Manager")
        print("1) Add patient details ")
        print("2) View patient by id ")
        print("3) Search all patients ")
        print("4) Search by patient name ")
        print("5) Add appointment ")
        print("6) Add history note ")
        print("7) Edit patient details ")
        print("8) Delete patient record ")
        print("9) Clear all records ")
        print("10) Show statistics of the clinic ")
        print("11) Exit")

        choice = input("Enter your choice from the given : ")

        if choice == "1":
            addpat()
        elif choice == "2":
            view_patient()
        elif choice == "3":
            patientlist()
        elif choice == "4":
            namesearch()
        elif choice == "5":
            addapp()
        elif choice == "6":
            histadd()
        elif choice == "7":
            patedit()
        elif choice == "8":
            delpat()
        elif choice == "9":
            car()
        elif choice == "10":
            showstat()
        elif choice == "11":
            print("program has ended")
            break
        else:
            print("Invalid option! try again\n")

all()