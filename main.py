from ui.console import *
from services.controller import HospitalRepositoryController
from domain.hospital import Department
from domain.patients import Patients
from infrastructure.repository import HospitaRepository
import unittest
import time

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover("C:/Users/David/PycharmProjects/pythonProject2/tests", pattern="test_*.py")
    unittest.TextTestRunner(verbosity=2).run(suite)
    time.sleep(1)



    controller = HospitalRepositoryController(HospitaRepository([
                Department(1, 'red', 4, [
                    Patients('Alisa', 'Berbec', 2361207030060, 'HIV'),
                    Patients('John', 'Smith', 2531230120071, 'TBC'),
                    Patients('Alex', 'Rock', 1840905300081, 'COMMON COLD'),
                    Patients('Alice', 'Gold', 2850701160088, 'COMMON COLD'),
                    Patients('Katy', 'Kiki', 2550222070079, 'COVID-19')
                ]),

                Department(23, 'ro', 2, [
                    Patients('Veronica', 'Rich', 1480516260065, ' COMMON COLD'),
                    Patients('Johnson', 'Rich', 5110921290099, 'COMMON COLD'),

                ]),

                Department(1000, 'last', 43, [
                    Patients('Andrew', 'Ruso', 1560604450027, 'COVID-19'),
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
            ]))
    run(controller)
