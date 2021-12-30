from domain.patients import Patients
from domain.hospital import Department
from infrastructure.repository import HospitaRepository
from utils.functions import check_pc
from general.generals import *


def menu():
    print("0 - Exit from the program")
    print("1 - Print menu")
    print("2 - Print the departments and their patients")
    print("3 - Add a department")
    print("4 - Add a patient")
    print("5 - Update a department give by index")
    print("6 - Update a patient given by index from a department that corresponds a given id")
    print("7 - Delete a department given by index")
    print("8 - Delete a patient given by index from a department that corresponds a given id")
    print("9 - Sort the patients in a department by personal numerical code")
    print("10 - Sort departments by the number of patients")
    print("11 - Sort departments by the number of patients having the age above a given limit")
    print("12 - Sort the patients from a department that corresponds a given id alphabetically")
    print("13 - Identify departments where there are patients under a given age")
    print("14 - Identify patients from a given department for which the first name or last name contain a given string")
    print("15 - Identify department/departments where there are patients with a given first name")
    print("16 - Form groups of 𝒌𝒌patients from the same department and the same disease")










def open():
    try:
        menu()
        command = int(input())
        hospital = HospitaRepository([
            Department(1, 'red', 4, [
                Patients('Alisa', 'Berbec', 2361207030060, 'HIV'),
                Patients('John', 'Smith' , 2531230120071, 'TBC'),
                Patients('Alex', 'Rock', 1840905300081, 'LEUKEMIA'),
                Patients('Alice', 'Gold', 2850701160088, 'COMMON COLD'),
                Patients('Katy', 'Kiki' , 2550222070079, 'COVID-19')
            ]),

            Department(23, 'ro', 2, [
                Patients('Veronica', 'Rich', 1480516260065, ' COMMON COLD'),
                Patients('Johnson', 'Rich', 5110921290099, 'COMMON COLD'),

            ]),

            Department(1000, 'last', 43, [
                Patients('Andrew', 'Ruso', 1560604450027, 'CANCER'),
                Patients('Katy', 'Ruso', 1521212430069, 'COVID-19'),
                Patients('Alexander', 'Ruso', 2580804370065, 'EBOLA VIRUS')
            ]),

            Department(19, 'COVID', 10, [
                Patients('Alehandro', 'Ruso', 1981018200010, 'COVID-19'),
                Patients('Kata', 'Ruso', 1210215170031, 'COVID-19'),
                Patients('Alexa', 'Ruso', 1400103050014, 'COVID-19'),
                Patients('Fernando', 'Smith', 2850225180061, 'COVID-19'),
                Patients('Mary', 'Pent', 2790224160077, 'SARSCOV'),
                Patients('Hello', 'Mary', 1310401510031, 'SARSCOV'),
                Patients('Dan', 'Danny', 1520508340011, 'COVID-19'),
                Patients('Penny', 'Dime', 2810709090076, 'SARSCOV'),
                Patients('Quartary', 'Levi', 1621025020082, 'SARSCOV'),
                Patients('Bianca', 'Laura', 1720421070096, 'COVID-19')
            ])
        ])


        while True:  # while command != 0

            if command == 1:
                menu()


            elif command == 2:
                print(str(hospital))

            elif command == 3:
                try:
                    ok = 0
                    while ok == 0:
                        id = int(input("Give an id: "))
                        if hospital.id_exists(id):
                            ok = 1
                        else:
                            print("The id already exists, please give another one")
                    name = input("Give a name: ")
                    number_of_beds = int(input("Give the number of beds: "))
                    hospital.add_department(id, name, number_of_beds)
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)



            elif command == 4:
                try:
                    if hospital.check_beds():
                        id = int(input("Give an id: "))
                        fn = input("First name: ")
                        ln = input("Last name: ")
                        pc = int(input("Personal code: "))
                        if check_pc(pc) and hospital.pc_exists(pc):

                            ds = input("Disease: ")
                            hospital.add_patients(id, fn, ln, pc, ds)
                        else:
                            print("The personal code isn't valid/unique, please try again!")
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 5:
                try:
                    index = int(input("Give an index: "))
                    if index < 0 or index > hospital.get_size():
                        print(menu())
                        raise ValueError
                    ok = 0
                    while ok == 0:
                        id = int(input("Give an id: "))
                        if hospital.id_exists(id):
                            ok = 1
                        else:
                            print("The id already exists, please give another one")
                    name = input("Give a name: ")
                    number_of_beds = int(input("Give the number of beds: "))
                    hospital.update_department(index, id, name, number_of_beds)
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 6:
                try:
                    id = int(input("Give an id:"))
                    index = int(input("Give an index"))
                    fn = input("First name: ")
                    ln = input("Last name: ")
                    pc = int(input("Personal code: "))
                    if check_pc(pc) and hospital.pc_exists(pc):
                        ds = input("Disease: ")
                        hospital.update_patient(id, index, fn, ln, pc, ds)
                    else:
                        print("The personal code isn't valid, please try again!")
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 7:
                try:
                    index = int(input("Give an index: "))
                    if index < 0 or index > hospital.get_size():
                        print(menu())
                        raise ValueError
                    hospital.delete_department(index)
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 8:
                try:
                    id = int(input("Give an id: "))
                    index = int(input("Give an index: "))
                    hospital.delete_patient(id, index)

                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 9:
                try:
                    id = int(input("Give an id: "))
                    increasing = input("Select if the list should be increasing or decreasing:")
                    hospital.sort_patients_by_pc(id, increasing)
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 10:
                try:

                    increasing = input("Select if the list should be increasing or decreasing: ")
                    hospital.sort_departments_by_NoP( increasing)
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 11:
                try:
                    limit = int(input("Give a limit age: "))
                    increasing = input("Select if the list should be increasing or decreasing: ")
                    hospital.sort_departments_by_age(limit, increasing)
                    hospital.reset_aux()
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 12:
                try:
                    id = int(input("Give an id: "))
                    increasing = input("Select if the list should be increasing or decreasing: ")
                    hospital.sort_patients(id, increasing)
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 13:
                try:
                    age = int(input("Give an age: "))
                    print(hospital.identify_department(age))
                    hospital.reset_aux()
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 14:
                try:
                    id = int(input("Give an Id: "))
                    string = input("Give a string: ")
                    print(hospital.identify_patient(id, string))
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 15:
                try:
                    first = input("Give a name: ")
                    print(hospital.identify_departments(first))
                    hospital.reset_aux()
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)
            elif command == 16:
                try:
                    k = int(input("Chose how many patients should form a group: "))
                    index = int(input("Give an Index: "))
                    n = 1
                    for i in hospital.form_groups(index, k):
                        print("Group " + str(n) + ":")
                        n = n + 1
                        for j in i:
                            print(str(j))
                        print(" ")


                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 0:
                print("Program closed")
                break


            else:
                print("Command does not exist!\nEnter a new one.")
            command = int(input(">>> "))
    except ValueError as ve:
        print(ve)
    except IndexError as ie:
        print(ie)