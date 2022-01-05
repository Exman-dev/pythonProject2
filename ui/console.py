from services.controller import HospitalRepositoryController
from utils.functions import *

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
    print("12 - Sort departments by the number of patients and the patients in a department alphabetically")
    print("13 - Identify departments where there are patients under a given age")
    print("14 - Identify patients from a given department for which the first name or last name contain a given string")
    print("15 - Identify department/departments where there are patients with a given first name")
    print("16 - Form groups of 𝒌𝒌patients from the same department and the same disease")










def run(controller: HospitalRepositoryController):
    try:
        menu()
        command = int(input())



        while True:  # while command != 0

            if command == 1:
                menu()


            elif command == 2:
                for (index, hospital) in enumerate(controller.get_all()):
                    print(index, hospital)

            elif command == 3:
                try:
                    ok = 0
                    while ok == 0:
                        id = int(input("Give an id: "))
                        if controller.id_exists(id):
                            ok = 1
                        else:
                            print("The id already exists, please give another one")
                    name = input("Give a name: ")
                    number_of_beds = int(input("Give the number of beds: "))
                    controller.add_department(id, name, number_of_beds)
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)



            elif command == 4:
                try:
                    if controller.check_beds():
                        id = int(input("Give an id: "))
                        fn = input("First name: ")
                        ln = input("Last name: ")
                        pc = int(input("Personal code: "))
                        if check_pc(pc) and controller.pc_exists(pc):

                            ds = input("Disease: ")
                            controller.add_patient(id, fn, ln, pc, ds)
                        else:
                            print("The personal code isn't valid/unique, please try again!")
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 5:
                try:
                    index = int(input("Give an index: "))
                    if index < 0 or index > controller.get_size():
                        print(menu())
                        raise ValueError
                    ok = 0
                    while ok == 0:
                        id = int(input("Give an id: "))
                        if controller.id_exists(id):
                            ok = 1
                        else:
                            print("The id already exists, please give another one")
                    name = input("Give a name: ")
                    number_of_beds = int(input("Give the number of beds: "))
                    controller.update_department(index, id, name, number_of_beds)
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
                    if check_pc(pc) and controller.pc_exists(pc):
                        ds = input("Disease: ")
                        controller.update_patient(id, index, fn, ln, pc, ds)
                    else:
                        print("The personal code isn't valid, please try again!")
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 7:
                try:
                    index = int(input("Give an index: "))
                    if index < 0 or index > controller.get_size():
                        print(menu())
                        raise ValueError
                    controller.delete_department(index)
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 8:
                try:
                    id = int(input("Give an id: "))
                    index = int(input("Give an index: "))
                    controller.delete_patient(id, index)

                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 9:
                try:
                    id = int(input("Give an id: "))
                    increasing = int(input("Select if the list should be increasing (1) or decreasing (2): "))
                    controller.sort_patients_by_pc(id, increasing)
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 10:
                try:

                    increasing = int(input("Select if the list should be increasing (1) or decreasing (2): "))
                    controller.sort_departments_by_NoP(increasing)
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 11:
                try:
                    limit = int(input("Give a limit age: "))
                    increasing = int(input("Select if the list should be increasing (1) or decreasing (2): "))
                    controller.sort_departments_by_age(limit, increasing)
                    controller.reset_aux()
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 12:
                try:
                    increasing = int(input("Select if the list should be increasing (1) or decreasing (2): "))
                    controller.sort_departments_by_NoP(increasing)
                    increasing = int(input("Select if the list should be increasing (1) or decreasing (2): "))
                    for i in range(controller.get_size()):
                        controller.sort_patients(i, increasing)
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 13:
                try:


                    age = int(input("Give an age: "))
                    rez = controller.identify_department(age)
                    if not rez:
                        raise Exception("No groups found")
                    for i in rez:

                        print(i)


                        print(" ")
                    controller.reset_aux()






                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 14:
                try:
                    id = int(input("Give an Id: "))
                    string = input("Give a string: ")

                    rez = controller.identify_patient(id, string)
                    if not rez:
                        raise Exception("No groups found")
                    for i in rez:
                        print(i)

                        print(" ")
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)

            elif command == 15:
                try:
                    first = input("Give a name: ")

                    rez = controller.identify_departments(first)
                    if not rez:
                        raise Exception("No groups found")
                    for i in rez:
                        print(i)

                        print(" ")
                    controller.reset_aux()
                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)
            elif command == 16:
                try:
                    k = int(input("Chose how many patients should form a group: "))
                    index = int(input("Give an Index: "))
                    n = 1
                    rez = controller.form_groups(index, k)
                    if not rez:
                        raise Exception("No groups found")
                    for i in rez:
                        print("Group " + str(n) + ":")
                        n = n + 1
                        for j in i:
                            print(str(j))
                        print(" ")




                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)
                except Exception as e:
                    print(e)

            elif command == 17:
                try:
                    p = int(input("Chose how many patients should form a group: "))
                    k = int(input("Chose from how many departments should form a group: "))

                    n = 1
                    rez = controller.form_groups_2(k, p)
                    if not rez:
                        raise Exception("No groups found")
                    for i in rez:
                        print("Group " + str(n) + ":")
                        n = n + 1
                        for j in i:
                            print(str(j))
                        print(" ")




                except ValueError as ve:
                    print(ve)
                except IndexError as ie:
                    print(ie)
                except Exception as e:
                    print(e)

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