import unittest
from domain.hospital import *
from domain.patients import *
from infrastructure.repository import *

class RepositoryTest(unittest.TestCase):

    def test_get_size(self):
        hospital = HospitaRepository([
                Department(1, 'red', 4, [
                    Patients('Alisa', 'Berbec', 2361207030060, 'HIV'),

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
                    Patients('Bianca', 'Laura', 1720421070096, 'COVID-19')
                ])
            ])
        self.assertEqual(hospital.get_size(), 4)


    def test_id_exists(self):
        hospital = HospitaRepository([
            Department(1, 'red', 4, [
                Patients('Alisa', 'Berbec', 2361207030060, 'HIV'),

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
                Patients('Bianca', 'Laura', 1720421070096, 'COVID-19')
            ])
        ])

        self.assertEqual(hospital.id_exists(5), True)
        self.assertEqual(hospital.id_exists(1), False)
        self.assertEqual(hospital.id_exists(100), True)

    def test_pc_exists(self):
        hospital = HospitaRepository([
            Department(1, 'red', 4, [
                Patients('Alisa', 'Berbec', 2361207030060, 'HIV')

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
                Patients('Bianca', 'Laura', 1720421070096, 'COVID-19')
            ])
        ])
        self.assertEqual(hospital.pc_exists(2361207030060), False)
        self.assertEqual(hospital.pc_exists(2361207030360), True)
        self.assertEqual(hospital.pc_exists(1521212430069), False)

    def test_add_department(self):
        hospital = HospitaRepository([
            Department(1, 'red', 4, [
                Patients('Alisa', 'Berbec', 2361207030060, 'HIV'),

            ])
        ])
        self.assertEqual(hospital.add_department(3, 'blue', 6), ([Department(1, 'red', 4, [
                Patients('Alisa', 'Berbec', 2361207030060, 'HIV'),

            ]), Department(3, 'blue', 6)]))

        self.assertEqual(hospital.add_department(1000, 'bl', 10), ([Department(1, 'red', 4, [
            Patients('Alisa', 'Berbec', 2361207030060, 'HIV'),

        ]), Department(3, 'blue', 6), Department(1000, 'bl', 10)]))

        self.assertEqual(hospital.add_department(3333, '333', 33), ([Department(1, 'red', 4, [
            Patients('Alisa', 'Berbec', 2361207030060, 'HIV'),

        ]), Department(3, 'blue', 6), Department(1000, 'bl', 10), Department(3333, '333', 33)]))

    def test_check_beds(self):
        hospital = HospitaRepository([
            Department(1, 'red', 4, [
                Patients('Alisa', 'Berbec', 2361207030060, 'HIV')

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
                Patients('Bianca', 'Laura', 1720421070096, 'COVID-19')
            ])
        ])
        self.assertEqual(hospital.check_beds(), True)

    def test_add_patient(self):
        hospital = HospitaRepository([
            Department(1, 'red', 4, [
                Patients('Alisa', 'Berbec', 2361207030060, 'HIV')

            ])
        ])
        self.assertEqual(hospital.add_patients(1, 'BOBO', 'NELSON', 1720421070096, 'COVID'), ([Department(1, 'red', 4, [
            Patients('Alisa', 'Berbec', 2361207030060, 'HIV'),
            Patients('BOBO', 'NELSON', 1720421070096, 'COVID')
        ])]))
        self.assertEqual(hospital.add_patients(1, 'Momo', 'Moma', 1981018200010, 'COVID'), ([Department(1, 'red', 4, [
            Patients('Alisa', 'Berbec', 2361207030060, 'HIV'),
            Patients('BOBO', 'NELSON', 1720421070096, 'COVID'),
            Patients('Momo', 'Moma', 1981018200010, 'COVID')
        ])]))

        self.assertEqual(hospital.add_patients(1, 'Andrew', 'Smith', 1560604450027, 'CANCER'), ([Department(1, 'red', 4, [
            Patients('Alisa', 'Berbec', 2361207030060, 'HIV'),
            Patients('BOBO', 'NELSON', 1720421070096, 'COVID'),
            Patients('Momo', 'Moma', 1981018200010, 'COVID'),
            Patients('Andrew', 'Smith', 1560604450027, 'CANCER')
        ])]))


    def test_delete_department(self):
        hospital = HospitaRepository([
            Department(1, 'red', 4, [
                Patients('Alisa', 'Berbec', 2361207030060, 'HIV')

            ]),

            Department(23, 'ro', 2, [
                Patients('Veronica', 'Rich', 1480516260065, ' COMMON COLD'),
                Patients('Johnson', 'Rich', 5110921290099, 'COMMON COLD'),

            ]),

            Department(19, 'COVID', 10, [
                Patients('Alehandro', 'Ruso', 1981018200010, 'COVID-19'),
                Patients('Bianca', 'Laura', 1720421070096, 'COVID-19')
            ])
        ])
        self.assertEqual(hospital.delete_department(1), ([Department(1, 'red', 4, [
            Patients('Alisa', 'Berbec', 2361207030060, 'HIV')
        ]),

                                                          Department(19, 'COVID', 10, [
                                                              Patients('Alehandro', 'Ruso', 1981018200010, 'COVID-19'),
                                                              Patients('Bianca', 'Laura', 1720421070096, 'COVID-19')
                                                          ])
                                                          ]))

        self.assertEqual(hospital.delete_department(1), ([Department(1, 'red', 4, [
            Patients('Alisa', 'Berbec', 2361207030060, 'HIV')
        ])]))

        self.assertEqual(hospital.delete_department(0), [])


    def test_delete_patient(self):
        hospital = HospitaRepository([


            Department(1000, 'last', 43, [
                Patients('Andrew', 'Ruso', 1560604450027, 'CANCER'),
                Patients('Katy', 'Ruso', 1521212430069, 'COVID-19'),
                Patients('Alexander', 'Ruso', 2580804370065, 'EBOLA VIRUS')
            ])
        ])
        self.assertEqual(hospital.delete_patient(1000, 1), ([Department(1000, 'last', 43, [
                Patients('Andrew', 'Ruso', 1560604450027, 'CANCER'),
                Patients('Alexander', 'Ruso', 2580804370065, 'EBOLA VIRUS')
            ])]))
        self.assertEqual(hospital.delete_patient(1000, 1), ([Department(1000, 'last', 43, [
            Patients('Andrew', 'Ruso', 1560604450027, 'CANCER')

        ])]))

        self.assertEqual(hospital.delete_patient(1000, 0), ([Department(1000, 'last', 43)]))

    def test_sort_patients_by_pc(self):

        hospital = HospitaRepository([

            Department(1000, 'last', 43, [
                Patients('Andrew', 'Ruso', 1560604450027, 'CANCER'),
                Patients('Katy', 'Ruso', 1521212430069, 'COVID-19'),
                Patients('Alexander', 'Ruso', 2580804370065, 'EBOLA VIRUS')
            ])
        ])

        self.assertEqual(hospital.sort_patients_by_pc(1000, 1), ([Department(1000, 'last', 43, [
            Patients('Katy', 'Ruso', 1521212430069, 'COVID-19'),
            Patients('Andrew', 'Ruso', 1560604450027, 'CANCER'),
            Patients('Alexander', 'Ruso', 2580804370065, 'EBOLA VIRUS')

        ])]))

        self.assertEqual(hospital.sort_patients_by_pc(1000, 2), ([Department(1000, 'last', 43, [
            Patients('Alexander', 'Ruso', 2580804370065, 'EBOLA VIRUS'),
            Patients('Andrew', 'Ruso', 1560604450027, 'CANCER'),
            Patients('Katy', 'Ruso', 1521212430069, 'COVID-19')
                                                                                        ])]))





