
class Department():
    def __init__(self, id, name = '', number_of_beds = 0, patients = [] , aux = -1):
        """
        Initializes the Department class
        :param id:
        :param name:
        :param number_of_beds:
        :param patients:
        :param aux:
        """
        self.id = id
        self.name = name
        self.number_of_beds = number_of_beds

        self.patients = patients
        self.aux = aux


    def getId(self):
        """
        Getter for Id
        :return:
        """
        return self.id

    def setId(self, id):
        """
        Setter for Id
        :param id:
        :return:
        """
        self.id = id

    def getName(self):
        """
        Getter for Name
        :return:
        """

        return self.name

    def setName(self, name = ''):
        """
        Setter for Name
        :param name:
        :return:
        """
        self.name = name

    def getNb(self):
        """
        Getter for the Number of beds
        :return:
        """
        return self.number_of_beds

    def setNb(self, beds):
        """
        Setter for the Number of beds
        :param beds:
        :return:
        """
        self.number_of_beds = beds

    def getP(self):
        """
        Getter for Patient list
        :return:
        """
        return self.patients

    def setP(self, patients):
        """
        Setter for Patient list
        :param patients:
        :return:
        """
        self.patients = patients

    def getNp(self):
        """
        Getter for the Number of patients
        :return:
        """
        return len(self.patients)

    def getAux(self):
        """
        Getter for Aux
        :return:
        """
        return self.aux

    def setAux(self, aux):
        """
        Setter for aux
        :param aux:
        :return:
        """
        self.aux = aux




    def __repr__(self):
        """
        Prints the class
        :return:
        """

        sir = "The department " + str(self.name) + " with id: " + str(self.id) + " has " + str(self.number_of_beds) + " beds and its patients are:\n"
        for patient in self.patients:
            sir = sir + (str(patient) + '\n')
        return sir

    def __eq__(self, other):
        """
        Checks if all the values are the same
        :param other:
        :return:
        """
        if self.id == other.getId() and self.name == other.getName() and self.number_of_beds == other.getNb() and self.patients == other.getP():
            return True
        return False
