from utils.functions import form_age
class Patients():
    def __init__(self, first_name = '', last_name = '', personal_code = 0, disease = ''):
        self.first_name = first_name
        self.last_name = last_name
        self.personal_code = personal_code
        self.disease = disease
        self.age = form_age(personal_code)

    def getFn(self):
        return self.first_name

    def setFn(self,first_name):
        self.first_name = first_name

    def getLn(self):
        return self.last_name

    def setLn(self, last_name):
        self.last_name = last_name

    def getPc(self):
        return self.personal_code

    def setPc(self,personal_code):
        self.personal_code = personal_code

    def getDs(self):
        return self.disease

    def setDs(self, disease):
        self.disease = disease

    def setAg(self, age):
        self.age = age

    def getAg(self):
        return self.age

    def getName(self):
        list = []
        list.append(self.last_name)
        list.append(self.first_name)
        return list



    def __repr__(self):
        return "The patient " + str(self.first_name) + " " + str(self.last_name) + " of " + str(self.age) + " years old with the personal code: " + str(self.personal_code) + " suffering from " + str(self.disease)

    def __eq__(self, other):
        if self.first_name == other.getFn() and self.last_name == other.getLn() and self.personal_code== other.getPc() and self.disease == other.getDs() and self.getAg() == other.getAg():
            return True
        return False