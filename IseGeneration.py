from datetime import datetime as dt
import RandomGenerator as gen
import random as ran

class IseGeneration:
    def __init__(self,
                 project_categories_amount,
                 project_amount,
                 project_rol_amount,
                 medewerker_amount):

        self.project_categories_amount = project_categories_amount
        self.project_amount = project_amount
        self.project_rol_amount = project_rol_amount
        self.medewerker_amount = medewerker_amount

        self.project_categories = []
        self.project = []
        self.project_rol_type = []
        self.medewerker = []

    def create_insert_script(self):
        self.fill_project_categorie()
        self.fill_project()
        self.fill_project_rol_type()
        self.fill_medewerker()

    def fill_project_categorie(self):
        category_list = []
        for x in range(self.project_categories_amount):
            category_name = "'" + gen.generate_alpha_string(ran.randrange(3, 10)) + "'"
            category_list.append(category_name)
            if ran.randrange(1) == 0:
                subcategory_name = category_list[ran.randrange(len(category_list))]
                if subcategory_name == category_name:
                    subcategory_name = 'NULL'
            else:
                subcategory_name = 'NULL'

            print('INSERT INTO project_categorie VALUES({}, {})'.format(category_name, subcategory_name))
            self.project_categories.append([category_name, subcategory_name])
        print('')

    def fill_project(self):
        for x in range(self.project_amount):
            categorie_naam = self.project_categories[ran.randrange(len(self.project_categories))][0]
            begin_datum = gen.generate_random_date(dt.strptime('1/1/2015 1:30 PM', '%d/%m/%Y %I:%M %p'), dt.today())
            eind_datum = gen.generate_random_date(dt.today(), dt.strptime('2/10/2020 1:30 PM', '%d/%m/%Y %I:%M %p'))
            project_naam = "'" + gen.generate_alpha_string(ran.randrange(5, 20)) + "'"
            project_code = project_naam[:5] + str(begin_datum.year) + "'"
            self.project.append([project_code, categorie_naam, begin_datum, eind_datum, project_naam])
            print("INSERT INTO project VALUES ({}, {}, '{}', '{}', {})".format(project_code, categorie_naam, begin_datum.strftime('%Y/%m/%d'), eind_datum.strftime('%m/%d/%Y'), project_naam))
        print('')

    def fill_project_rol_type(self):
        for x in range(self.project_rol_amount):
            project_rol = "'" + gen.generate_alpha_string(ran.randrange(5, 9)) + "'"
            self.project_rol_type.append(project_rol)
            print("INSERT INTO project_rol_type VALUES ({})".format(project_rol))
        print('')

    def fill_medewerker(self):
        medewerkers = []
        for x in range(self.medewerker_amount):
            voornaam = gen.generate_alpha_string(ran.randrange(3, 20))
            achternaam = gen.generate_alpha_string(ran.randrange(3, 20))
            medewerker_code = (voornaam[0] + achternaam[0]).upper()
            medewerkers.append(medewerker_code)
            medewerker_code_count = medewerkers.count(medewerker_code) - 1
            if medewerker_code_count != 0:
                medewerker_code += str(medewerker_code_count)


            self.medewerker.append([medewerker_code, voornaam, achternaam])
            print("INSERT INTO medewerker VALUES('{}', '{}', '{}')".format(medewerker_code, voornaam, achternaam))
        print('')



generator = IseGeneration(10, 100, 5, 200)
generator.create_insert_script()