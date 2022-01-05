from utils.functions import form_age
class Patients():
    def __init__(self, first_name = '', last_name = '', personal_code = 0, disease = ''):
        """
        Initializes the Patients class
        :param first_name:
        :param last_name:
        :param personal_code:
        :param disease:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.personal_code = personal_code
        self.disease = disease
        self.age = form_age(personal_code)

    def getFn(self):
        """
        Getter for First name
        :return:
        """
        return self.first_name

    def setFn(self,first_name):
        """
        Setter for First Name
        :param first_name:
        :return:
        """
        self.first_name = first_name

    def getLn(self):
        """
        Getter for Last name
        :return:
        """
        return self.last_name

    def setLn(self, last_name):
        """
        Setter for Last name
        :param last_name:
        :return:
        """
        self.last_name = last_name

    def getPc(self):
        """
        Getter for Personal code
        :return:
        """
        return self.personal_code

    def setPc(self,personal_code):
        """
        Setter for Personal code
        :param personal_code:
        :return:
        """
        self.personal_code = personal_code

    def getDs(self):
        """
        Getter for Disease
        :return:
        """
        return self.disease


    def setDs(self, disease):
        """
        Setter for Disease
        :param disease:
        :return:
        """
        self.disease = disease

    def setAg(self, age):
        """
        Setter for Age
        :param age:
        :return:
        """
        self.age = age

    def getAg(self):
        """
        Getter for Age
        :return:
        """
        return self.age

    def getName(self):
        """
        Getter for full Name
        :return:
        """
        list = []
        list.append(self.last_name)
        list.append(self.first_name)
        return list



    def __repr__(self):
        """
        Prints the Patient class
        :return:
        """
        return "The patient " + str(self.first_name) + " " + str(self.last_name) + " of " + str(self.age) + " years old with the personal code: " + str(self.personal_code) + " suffering from " + str(self.disease)

    def __eq__(self, other):
        """
        Checks if all the Values are equal
        :param other:
        :return:
        """
        if self.first_name == other.getFn() and self.last_name == other.getLn() and self.personal_code == other.getPc() and self.disease == other.getDs() and self.getAg() == other.getAg():
            return True
        return False