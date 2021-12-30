from domain.patients import Patients
class Department():
    def __init__(self, id, name = '', number_of_beds = 0, patients = [] , aux = -1):
        self.id = id
        self.name = name
        self.number_of_beds = number_of_beds

        self.patients = patients
        self.aux = aux


    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getName(self):
        return self.name

    def setName(self, name = ''):
        self.name = name

    def getNb(self):
        return self.number_of_beds

    def setNb(self, beds):
        self.number_of_beds = beds

    def getP(self):
        return self.patients

    def setP(self, patients):
        self.patients = patients

    def getNp(self):
        return len(self.patients)

    def getAux(self):
        return self.aux

    def setAux(self, aux):
        self.aux = aux




    def __repr__(self):

        sir = "The department " + str(self.name) + " with id: " + str(self.id) + " has " + str(self.number_of_beds) + " beds and its patients are:\n"
        for patient in self.patients:
            sir = sir + (str(patient) + '\n')
        return sir

    def __eq__(self, other):
        if self.id == other.getId() and self.name == other.getName() and self.number_of_beds == other.getNb() and self.patients == other.getP():
            return True
        return False
