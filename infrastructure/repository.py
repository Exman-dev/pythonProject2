from domain.hospital import Department
from domain.patients import Patients
from general.generals import *
class HospitaRepository():
    def __init__(self, department_list = []):
        """
        Initializes the repository
        :param department_list:
        """
        self.__department = department_list.copy()

    def __str__(self):
        """
        Converting a HospitalRepository object into a string
        :return:
        """
        repr_str = ""
        for departments in self.__department:
            repr_str += str(departments) + "\n"
        return repr_str

    def get_size(self):
        """
        Finds the size
        :param index:
        :return: The size of the department/patient list
        """
        return len(self.__department)

    def get_all(self):
        """
        Prints all the departments and all their patients
        :return:
        """
        return self.__department



    def id_exists(self, id):
        """
        Checks if the id is unique
        :param id:
        :return: bool
        """
        for i in range(len(self.__department)):
            if self.__department[i].getId() == id:
                return False
        return True

    def pc_exists(self, pc):
        """
        Checks if the pc is unique
        :param pc:
        :return:
        """
        for i in range(len(self.__department)):
            for j in range(len(self.__department[i].patients)):
                if self.__department[i].patients[j].getPc() == pc:
                    return False
        return True

    def add_department(self, id, name, number_of_beds):
        """
        Adds a new department to the repository
        :param id:
        :param name:
        :param number_of_beds:
        :return: The new department list
        """
        self.__department.append(Department(id, name, number_of_beds))
        return self.__department

    def check_beds(self):
        """
        Checks if there are enough beds for the patients
        :return: bool
        """
        ok = 0
        for i in range(len(self.__department)):
            k = self.__department[i].getNb() - len(self.__department[i].getP())
            if k > 0:
                print("There are " + str(k) + " beds availabe in the department with Id: " + str(self.__department[i].getId()))
                ok = 1
        if ok == 0:
            print("There are no available beds in any department. In order to add more patients create another department with any number of beds you want")
            return False
        return True

    def add_patients(self, id, first_name, last_name, personal_code, disease):
        """
        Adds a patient to a department identified by its id
        :param id:
        :param first_name:
        :param last_name:
        :param personal_code:
        :param disease:
        :return: The modified department list with its patient list
        """
        ok = 1
        for i in range(len(self.__department)):
            if self.__department[i].getId() == id:
                if len(self.__department[i].getP()) == self.__department[i].getNb():
                    print("Please chose another department, this one is full")
                    ok = 0
        if ok == 1:
            for i in range(len(self.__department)):
                if self.__department[i].getId() == id:
                    self.__department[i].patients.append(Patients(first_name, last_name, personal_code, disease))

        return self.__department

    def update_department(self, index, id, name, number_of_beds):
        """
        Updates a department given by index
        :param index:
        :param id:
        :param name:
        :param number_of_beds:
        :return: The modified department list
        """
        if number_of_beds < len(self.__department[index].getP()):
            print("There are less beds than the patients located there, try again")
        else:
            self.__department[index].setId(id)
            self.__department[index].setName(name)
            self.__department[index].setNb(number_of_beds)
        return self.__department

    def update_patient(self, id, index, first_name, last_name, personal_code, disease):
        """
        Updates a patient given by index from a department given by its id
        :param id:
        :param index:
        :param first_name:
        :param last_name:
        :param personal_code:
        :param disease:
        :return: The modified patient list
        """
        ok = 0

        for i in range(len(self.__department)):
            if id == self.__department[i].getId():
                ok = 1
                pos = i
        if ok == 0:
            print("There are no departments with the given id")
            return self.__department
        else:
            if index < 0 or index > len(self.__department[pos].getP()):
                raise ValueError
                print("Index error")
            else:
                self.__department[pos].patients[index].setFn(first_name)
                self.__department[pos].patients[index].setLn(last_name)
                self.__department[pos].patients[index].setPc(personal_code)
                self.__department[pos].patients[index].setDs(disease)

        return self.__department

    def delete_department(self, index):
        """
        Deletes a department given by index
        :param index:
        :return:
        """
        self.__department.pop(index)
        return self.__department

    def delete_patient(self, id, index):
        """
        Deletes a patient given by index from a department indentified by id
        :param id:
        :param index:
        :return:
        """
        ok = 0

        for i in range(len(self.__department)):
            if id == self.__department[i].getId():
                ok = 1
                pos = i
        if ok == 0:
            print("There are no departments with the given id")
            return self.__department
        else:
            if index < 0 or index > len(self.__department[pos].getP()):
                raise ValueError
                print("Index error")
            else:
                self.__department[pos].patients.pop(index)
        return self.__department

    def sort_patients_by_pc(self, id, increasing):
        """
        Sorts the patients by their personal code from a department identified by their id
        :param id:
        :param increasing:
        :return:
        """
        ok = 0

        for i in range(len(self.__department)):
            if id == self.__department[i].getId():
                ok = 1
                pos = i
        if ok == 0:
            print("There are no departments with the given id")
            return self.__department
        else:
            if increasing == 1:
                return general_sort(self.__department[pos].patients, lambda p1, p2: p1.getPc() <= p2.getPc())

            elif increasing == 2:
                return general_sort(self.__department[pos].patients, lambda p1, p2: p1.getPc() >= p2.getPc())

            else:
                raise ValueError("The given input should be 1 or 2")

    def sort_departments_by_NoP(self, increasing):
        """
        Sorts the departments by the number of patients
        :param increasing:
        :return:
        """
        if increasing == 1:
            return general_sort(self.__department, lambda d1, d2: d1.getNp() <= d2.getNp())

        elif increasing == 2:
            return general_sort(self.__department, lambda d1, d2: d1.getNp() >= d2.getNp())
        else:
            raise ValueError("The given input should be 1 or 2")

    def sort_departments_by_age(self, limit, increasing):
        """
        Sorts departments by the number of patients whose age is higher than a limit
        :param limit:
        :param increasing:
        :return:
        """
        for i  in range(len(self.__department)):
            k = 0
            for j in range(len(self.__department[i].patients)):
                if self.__department[i].patients[j].getAg() > limit:
                    k = k + 1
            self.__department[i].setAux(k)
        if increasing == 1:
            return general_sort(self.__department, lambda d1, d2: d1.getAux() <= d2.getAux())

        elif increasing == 2:
            return general_sort(self.__department, lambda d1, d2: d1.getAux() >= d2.getAux())
        else:
            raise ValueError("The given input should be 1 or 2")

    def reset_aux(self):
        """
        Resets the aux for every department for further usages
        :return:
        """
        for i in range(len(self.__department)):
            self.__department[i].setAux(-1)

        return self.__department

    def sort_patients(self, i, increasing):
        """
        Sorts the patients by their last name and first name in an alphabetical order
        :param id:
        :param increasing:
        :return:
        """

        if increasing == 1:
            return general_sort(self.__department[i].patients, lambda d1, d2: d1.getName() <= d2.getName())

        elif increasing == 2:
            return general_sort(self.__department[i].patients, lambda d1, d2: d1.getName() >= d2.getName())
        else:
            raise ValueError("The given input should be 1 or 2")

    def identify_department(self, limit):
        """
        Searches for the departments which have patients with a lesser age than the limit
        :param limit:
        :return:
        """
        for i  in range(len(self.__department)):
            k = 0
            for j in range(len(self.__department[i].patients)):
                if self.__department[i].patients[j].getAg() < limit:
                    k = k + 1
            self.__department[i].setAux(k)
        return general_search(self.__department, lambda d1: d1.getAux() > 0)

    def identify_patient(self, id, string):
        """
        Searches for the patients with the given name from a department identified by its id
        :param id:
        :param string:
        :return:
        """
        ok = 0

        for i in range(len(self.__department)):
            if id == self.__department[i].getId():
                ok = 1
                pos = i
        if ok == 0:
            print("There are no departments with the given id")
            return self.__department
        else:
            return general_search(self.__department[pos].patients, lambda patient: string in patient.getFn()
                                  or string in patient.getLn())

    def identify_departments(self, first):
        """
        Identifies the departments with patients that have a certain First Name
        :param first:
        :return:
        """
        for i in range(len(self.__department)):
            for j in range(len(self.__department[i].patients)):
                if self.__department[i].patients[j].getFn() == first:
                    self.__department[i].setAux(1)
        return general_search(self.__department, lambda d1: d1.getAux() > 0)

    def check_group(self, groups) -> bool:
        """
        Checks if a group is valid
        :param groups:
        :return:
        """
        for group in groups:
            disease = ""
            for patient in group:
                if disease == "":
                    disease = patient.getDs()
                elif disease != patient.getDs():
                    return False
        return True



    def check_group2(self, groups) -> bool:
        list_g = []

        for group in groups:
            disease = ""
            for patient in group:
                if disease == "":
                    disease = patient.getDs()
                elif disease != patient.getDs():
                    return False
                if list_g.__contains__(disease):
                    return False
            list_g.append(disease)

        return True

    def form_groups(self, index, k):
        """
        Forms the groups
        :param index:
        :param k:
        :return:
        """
        return(groups(self.__department[index].patients, k, self.check_group))


    def form_groups_2(self, k ,p):
        list_group = []


        for i in range (k):
            #to do
            list_group.append(groups(self.__department[i].patients, p, self.check_group2))
        return list_group












