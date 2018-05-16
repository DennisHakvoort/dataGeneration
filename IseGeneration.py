from datetime import datetime as dt, date
import RandomGenerator as gen
import random as ran

class IseGeneration:
    def __init__(self,
                 project_categories_amount,
                 project_amount,
                 project_rol_amount,
                 medewerker_amount,
                 medewerker_rol_type_amount):

        self.project_categories_amount = project_categories_amount
        self.project_amount = project_amount
        self.project_rol_amount = project_rol_amount
        self.medewerker_amount = medewerker_amount
        self.medewerker_rol_type_amount = medewerker_rol_type_amount

        self.project_categories = []
        self.project = []
        self.project_rol_type = []
        self.medewerker = []
        self.medewerker_rol_type = []
        self.medewerker_rol = []
        self.medewerker_beschikbaarheid = []
        self.medewerker_op_project = []
        self.medewerker_ingepland_project = []

        self.file = open('generated.sql', 'w+')
        self.file.write('USE LeanDb')
        self.file.write('\n')
        self.file.write('GO')
        self.file.write('\n')
        self.file.write('\n')
        self.file.write('DBCC CHECKIDENT (medewerker_op_project, RESEED, 0)')
        self.file.write('\n')
        self.file.write('\n')


    def create_insert_script(self):
        self.fill_project_categorie()
        self.fill_project()
        self.fill_project_rol_type()
        self.fill_medewerker()
        self.fill_project_rol_type()
        self.fill_medewerker_rol_type()
        self.fill_medewerker_rol()
        self.fill_medewerker_op_project()
        self.fill_medewerker_ingepland_project()
        self.fill_medewerker_beschikbaarheid()

    def fill_project_categorie(self):
        category_list = []
        for x in range(self.project_categories_amount):
            category_name = "'" + gen.generate_alpha_string(ran.randrange(3, 10)) + "'"
            category_list.append(category_name)
            if ran.randrange(2) == 0:
                subcategory_name = category_list[ran.randrange(len(category_list))]
                if subcategory_name == category_name:
                    subcategory_name = 'NULL'
            else:
                subcategory_name = 'NULL'

            self.file.write('INSERT INTO project_categorie VALUES({}, {})'.format(category_name, subcategory_name))
            self.file.write('\n')
            self.project_categories.append([category_name, subcategory_name])
        self.file.write('\n')

    def fill_project(self):
        for x in range(self.project_amount):
            categorie_naam = self.project_categories[ran.randrange(len(self.project_categories))][0]
            begin_datum = gen.generate_random_date(dt.strptime('1/1/2015 1:30 PM', '%d/%m/%Y %I:%M %p'), dt.today())
            eind_datum = gen.generate_random_date(dt.today(), dt.strptime('2/10/2020 1:30 PM', '%d/%m/%Y %I:%M %p'))
            project_naam = "'" + gen.generate_alpha_string(ran.randrange(5, 20)) + "'"
            project_code = project_naam[:5] + str(begin_datum.year) + "'"
            self.project.append([project_code, categorie_naam, begin_datum, eind_datum, project_naam])
            self.file.write("INSERT INTO project VALUES ({}, {}, '{}', '{}', {})".format(project_code, categorie_naam, begin_datum.strftime('%Y/%m/%d'), eind_datum.strftime('%m/%d/%Y'), project_naam))
            self.file.write('\n')
        self.file.write('\n')

    def fill_project_rol_type(self):
        for x in range(self.project_rol_amount):
            project_rol = "'" + gen.generate_alpha_string(ran.randrange(5, 9)) + "'"
            self.project_rol_type.append(project_rol)
            self.file.write("INSERT INTO project_rol_type VALUES ({})".format(project_rol))
            self.file.write('\n')
        self.file.write('\n')

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
            self.file.write("INSERT INTO medewerker VALUES('{}', '{}', '{}')".format(medewerker_code, voornaam, achternaam))
            self.file.write('\n')
        self.file.write('\n')

    def fill_medewerker_rol_type(self):
        for x in range(self.medewerker_rol_type_amount):
            medewerker_rol = "'" + gen.generate_alpha_string(ran.randrange(5, 9)) + "'"
            self.medewerker_rol_type.append(medewerker_rol)
            self.file.write("INSERT INTO medewerker_rol_type VALUES ({})".format(medewerker_rol))
            self.file.write('\n')
        self.file.write('\n')

    def fill_medewerker_rol(self):
        for x in self.medewerker:
            beschikbare_rollen = self.medewerker_rol_type.copy()
            medewerker_code = x[0]
            first_loop = True

            while (ran.randrange(2) == 0 or first_loop) and len(beschikbare_rollen) != 0:
                first_loop = False
                medewerker_rol = beschikbare_rollen[ran.randrange(len(beschikbare_rollen))]
                beschikbare_rollen.remove(medewerker_rol)
                self.medewerker_rol.append([medewerker_code, medewerker_rol])
                self.file.write("INSERT INTO medewerker_rol VALUES ('{}', {})".format(medewerker_code, medewerker_rol))
                self.file.write('\n')
        self.file.write('\n')

    def fill_medewerker_op_project(self):
        id_teller = 1
        for x in self.medewerker:
            beschikbare_projecten = self.project.copy()
            medewerker_code = x[0]
            first_loop = True

            while (ran.randrange(2) == 0 or first_loop) and len(beschikbare_projecten) != 0:
                first_loop = False
                id = id_teller
                id_teller += 1
                project_code = beschikbare_projecten[ran.randrange(len(beschikbare_projecten))][0]
                project_rol = self.project_rol_type[ran.randrange(len(self.project_rol_type))]
                self.medewerker_op_project.append([id, project_code, medewerker_code, project_rol])
                self.file.write("INSERT INTO medewerker_op_project (project_code, medewerker_code, project_rol) VALUES ({}, '{}', {})".format(project_code, medewerker_code, project_rol))
                self.file.write('\n')
        self.file.write('\n')

    def fill_medewerker_ingepland_project(self):
        for x in self.medewerker_op_project:
            id = x[0]

            huidige_project = None
            for y in self.project:
                if y[0] == x[1]:
                    huidige_project = y
                    break

            year = huidige_project[2].year
            month = huidige_project[2].month
            while date(year, month, 1) < dt.date(huidige_project[3]):
                maand_datum = "'" + str(year) + '/' + str(month) + "/1'"
                month += 1
                if month > 12:
                    month = 1
                    year += 1
                if ran.randrange(2) == 0:
                    medewerker_uren = ran.randrange(182)
                    self.medewerker_ingepland_project.append([id, medewerker_uren, maand_datum])
                    self.file.write("INSERT INTO medewerker_ingepland_project VALUES ({}, {}, {})".format(id, medewerker_uren, maand_datum))
                    self.file.write('\n')
        self.file.write('\n')

    def fill_medewerker_beschikbaarheid(self):
        for x in self.medewerker:
            medewerker_code = x[0]

            year = 2015
            month = 1
            while date(year, month, 1) < date(2020, 10, 2):
                maand = "'" + str(year) + '/' + str(month) + "/1'"
                month += 1
                if month > 12:
                    month = 1
                    year += 1

                if ran.randrange(2) == 0:
                    beschikbaar_uren = ran.randrange(182)
                    self.file.write(
                        "INSERT INTO medewerker_beschikbaarheid VALUES ('{}', {}, {})".format(medewerker_code, maand,
                                                                                              beschikbaar_uren))
                    self.file.write('\n')
                    self.medewerker_beschikbaarheid.append([medewerker_code, maand, beschikbaar_uren])
        self.file.write('\n')




generator = IseGeneration(5, 25, 3, 28, 6)
generator.create_insert_script()