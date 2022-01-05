from typing import List

from infrastructure.repository import *

class HospitalRepositoryController():
    """
    Controller which manages the interaction between the UI and the infrastructure of the project
    """

    def __init__(self, repo: HospitaRepository = HospitaRepository()):
        self.__repo = repo

    def __str__(self) -> str:
        """
        Returns a string representation
        :return:String
        """
        return(str(self.__repo))

    def get_all(self) -> List[Department]:
        """
        Gets all the departments and all their patients
        :return:
        """
        return self.__repo.get_all()

    def get_size(self):
        """
        Finds the size
        :param index:
        :return: The size of the list
        """
        return self.__repo.get_size()

    def id_exists(self, id):
        """
        Checks for id
        :param id:
        :return:
        """
        return self.__repo.id_exists(id)

    def pc_exists(self, pc):
        """
        Checks for personal code
        :param pc:
        :return:
        """
        return self.__repo.pc_exists(pc)

    def add_department(self, id, name, number_of_beds):
        """
        Adds a department
        :param id:
        :param name:
        :param number_of_beds:
        :return:
        """
        return self.__repo.add_department(id, name, number_of_beds)

    def check_beds(self):
        """
        Checks the number of beds
        :return:
        """
        return  self.__repo.check_beds()

    def add_patient(self, id, first_name, last_name, personal_code, disease):
        """
        Adds a patient
        :param id:
        :param first_name:
        :param last_name:
        :param personal_code:
        :param disease:
        :return:
        """
        return self.__repo.add_patients(id, first_name, last_name, personal_code, disease)

    def update_department(self, index, id, name, number_of_beds):
        """
        Updates a department
        :param index:
        :param id:
        :param name:
        :param number_of_beds:
        :return:
        """
        return self.__repo.update_department(index, id, name, number_of_beds)

    def update_patient(self, id, index, first_name, last_name, personal_code, disease):
        """
        Updates a patient
        :param id:
        :param index:
        :param first_name:
        :param last_name:
        :param personal_code:
        :param disease:
        :return:
        """
        return self.__repo.update_patient(id, index, first_name, last_name, personal_code, disease)

    def delete_department(self, index):
        """
        Deletes a department
        :param index:
        :return:
        """
        return self.__repo.delete_department(index)

    def delete_patient(self, id, index):
        """
        Deletes a patient
        :param id:
        :param index:
        :return:
        """
        return self.__repo.delete_patient(id, index)

    def sort_patients_by_pc(self, id, increasing):
        """
        Sorts the patients by their personal code
        :param id:
        :param increasing:
        :return:
        """
        return self.__repo.sort_patients_by_pc(id, increasing)

    def sort_departments_by_NoP(self, increasing):
        """
        Sorts the departments by their number of patients
        :param increasing:
        :return:
        """
        return self.__repo.sort_departments_by_NoP(increasing)

    def sort_departments_by_age(self, limit, increasing):
        """
        Sorts the departments by their number of patients who are older than a limit
        :param limit:
        :param increasing:
        :return:
        """
        return self.__repo.sort_departments_by_age(limit, increasing)

    def reset_aux(self):
        """
        Resets an aux param
        :return:
        """
        return self.__repo.reset_aux()

    def sort_patients(self, i, increasing):
        """
        Sorts the patients
        :param id:
        :param increasing:
        :return:
        """
        return self.__repo.sort_patients(i,increasing)

    def identify_department(self, limit):
        """
        Searches for departments
        :param limit:
        :return:
        """
        return self.__repo.identify_department(limit)

    def identify_patient(self, id, string):
        """
        Identifies patients
        :param id:
        :param string:
        :return:
        """
        return self.__repo.identify_patient(id, string)

    def identify_departments(self, first):
        """
        Identifies departments
        :param first:
        :return:
        """
        return self.__repo.identify_departments(first)

    def form_groups(self, index, k):
        """
        Forms a group of patients
        :param index:
        :param k:
        :return:
        """
        return self.__repo.form_groups(index, k)

    def form_groups_2(self, k, p):
        return self.__repo.form_groups_2(k, p)

