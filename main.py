import oracledb


# CONFIG #######################
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
username = config['DEFAULT']['User']
password = config['DEFAULT']['Password']
hostname = config['DEFAULT']['Hostname']
port = config['DEFAULT']['Port']
servicename = config['DEFAULT']['ServiceName']
dsn = oracledb.makedsn(host=hostname,port=port,service_name=servicename)

################################



import random
number_list = []
used_numbers = set()  # przechowuje wygenerowane numery telefonów
count = 1000000  # liczba numerów do wygenerowania

def generate_phone_number():
    while True:
        number = ''.join(random.choices('0123456789', k=9))  # generuj 9-cyfrowy numer telefonu
        if number not in used_numbers:  # jeśli numer jeszcze nie został użyty
            used_numbers.add(number)  # dodaj numer do zbioru użytych numerów
            return f"{number[:3]}{number[3:6]}{number[6:]}"  # zwróć numer w formacie +48 xxx-xxx-xxx

# wygeneruj milion numerów telefonów i zapisz je do pliku
def CreateNumber():
    import os
    if (os.path.exists('data/phone_numbers.txt') == False):
     
        with open('data/phone_numbers.txt', 'w') as f:
            for i in range(count):
                phone_number = generate_phone_number()
                f.write(phone_number + '\n')
        print('Create 1 000 000 phone number')

import random
import csv
CreateNumber()
female_name_list = []
female_lastname_list = []
male_name_list = []
male_lastname_list = []
city_list = []
street_list =[]
items = []
# Wczytanie z plików ############################
with open('data/imie_f.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    for row in reader:
        female_name_list += [row[0]]
with open('data/imie_m.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    for row in reader:
        male_name_list += [row[0]]
with open('data/nazwiska_f.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    for row in reader:
        female_lastname_list += [row[0]]
with open('data/nazwiska_m.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    for row in reader:
        male_lastname_list += [row[0]]
with open('data/miasta.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    for row in reader:
        city_list += [row[2]]
with open('data/ulica.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    for row in reader:
        street_list += [row[7]]
with open('data/Stockroom.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    for row in reader:
        items += [row]
with open('data/phone_numbers.txt', 'r') as f:
    for line in f:
        number_list +=[(line.strip())]
    pass

#################################################

# Słownikowe ####################################
class Disease(object):
    """docstring for Disease"""
    ID = 1
    def __init__(self, name):
        super(Disease, self).__init__()
        self.ID = Disease.ID
        self.name = name
        Disease.ID += 1
    def display(self):
        print(self.ID,self.name)
    def insert(self):
        return f"INSERT INTO choroba VALUES ({self.ID}, '{self.name}')"
        
class Specialization(object):
    """docstring for Specialization"""
    ID = 1
    def __init__(self, name):
        super(Specialization, self).__init__()
        self.ID = Specialization.ID
        self.name = name
        Specialization.ID += 1
    def display(self):
        print(self.ID,self.name)
    def insert(self):
        return f"INSERT INTO specjalizacja (id_specjalizacja, nazwa_specjalizacji) VALUES ({self.ID}, '{self.name}')"
class Species(object):
    """docstring for Species"""
    ID = 1
    def __init__(self, name):
        super(Species, self).__init__()
        self.ID = Species.ID
        self.name = name
        Species.ID += 1
    def display(self):
        print(self.ID,self.name)
    def insert(self):
        return f"INSERT INTO gatunek VALUES ({self.ID}, '{self.name}')"
class Medical_treatment(object):
    """docstring for Medical_treatment"""
    ID = 1
    def __init__(self, name):
        super(Medical_treatment, self).__init__()
        self.ID = Medical_treatment.ID
        self.name = name
        Medical_treatment.ID += 1
    def display(self):
        print(self.ID,self.name)
    def insert(self):
        return f"INSERT INTO rodzaj_zabiegu (id_rodz_zab, nazwa) VALUES ({self.ID}, '{self.name}')"
class Control_visit(object):
    """docstring for Control_visit"""
    ID = 1
    def __init__(self, name):
        super(Control_visit, self).__init__()
        self.ID = Control_visit.ID
        self.name = name
        self.cena = random.randint(90,110)+0.99
        Control_visit.ID += 1
    def display(self):
        print(self.ID,self.name)
    def insert(self):
        return f"INSERT INTO rodzaj_wizyty VALUES ({self.ID}, '{self.name}', {self.cena})"
#################################################        
regions = [
'dolnośląskie',
'kujawsko-pomorskie',
'lubelskie',
'lubuskie',
'łódzkie',
'małopolskie',
'mazowieckie',
'opolskie',
'podkarpackie',
'podlaskie',
'pomorskie',
'śląskie',
'świętokrzyskie',
'warmińsko-mazurskie',
'wielkopolskie',
'zachodniopomorskie'
]


allPerson = []
allDoc = []
allAnimal = []
allItem = []
allSpecies = []
allSpecialization=[]
allWizyty = []
allZabiegi=[]
allPrescription = []
#------------
allMedical_treatment = []
allDisease =[]
#------------
allControl_visit = []

allH_M = []


SpecializationTmp = ['Psy',
'Koty',
'Ptaki',
'Gady/Płazy',
'Gryzonie']
for s in SpecializationTmp:
    allSpecialization += [Specialization(s)]
SpaciesTmp=['Pies',
'Kot',
'Ptak',
'Gad',
'Gryzoń']
for s in SpaciesTmp:
    allSpecies += [Species(s)]
DiseaseTmp = ['Zapalenie pęcherza moczowego',
'Zaparcia',
'Biegunka',
'Choroby serca',
'Choroby wątroby',
'Choroby nerek',
'Choroby tarczycy',
'Cukrzyca',
'Choroby skóry',
'Zapalenie ucha',
'Zakażenia dróg oddechowych',
'Zaburzenia trawienia',
'Padaczka',
'Problemy z kośćmi i stawami',
'Choroby oczu',
'Choroby jamy ustnej',
'Nowotwory',
'Stres',
'Depresja',
'Lęki i fobie',
'Pchły']
for s in DiseaseTmp:
    allDisease += [Disease(s)]
Control_visitTmp = ['Wizyta kontrolna',
'Wizyta szczepienna',
'Wizyta chirurgiczna',
'Wizyta stomatologiczna',
'Wizyta dermatologiczna',
'Wizyta kardiologiczna',
'Wizyta neurologiczna',
'Wizyta endokrynologiczna',
'Wizyta onkologiczna',
'Wizyta behawioralna']
for s in Control_visitTmp:
    allControl_visit += [Control_visit(s)]
Medical_treatmentTmp = ['Kastracja/sterylizacja',
'Amputacja kończyny',
'Usuwanie kamieni moczowych',
'Endoskopia',
'Wypełnienie zębów',
'Wycięcie guza',
'Wymiana stawu',
'Wyrównanie złamań kości',
'Usunięcie ciała obcego',
'Leczenie ran']
for s in Medical_treatmentTmp:
    allMedical_treatment += [Medical_treatment(s)]




class His_Stor(object):
    def __init__(self,ID,ID_STORAGE,ID_REC):
        self.ID = ID
        self.ID_STOR = ID_STORAGE
        self.ID_REC = ID_REC
    def display(self):
        print(self.ID,self.ID_STOR,self.ID_REC)
class Person(object):
    ID = 1
    def __init__(self):
        self.ID = Person.ID
        self.sex = random.choice(['female', 'male'])
        self.name = self.random_name()
        self.lastname = self.random_lastname()
        self.address = self.random_adress()
        self.phone_number = self.random_phone()
        Person.ID +=1
    def insert(self):
        return f"""INSERT INTO wlasciciele
        (id_wlasciciela, imie, nazwisko, adres, nr_tel)
        VALUES ({self.ID}, '{self.name}', '{self.lastname}', adres('{self.address[0]}', '{self.address[1]}', {self.address[2]}, '{self.address[3]}'), '{self.phone_number}')
        """
    def display(self):
        print(self.ID,self.name, self.lastname, self.sex , self.phone_number,self.address)
    def random_adress(self):
        adress = (random.choice(city_list),random.choice(street_list),random.randint(1,99),random.choice(regions))
        return adress
        pass
    def random_name(self):
        if self.sex == 'female':
            return random.choice(female_name_list)
        else:
            return random.choice(male_name_list)

    def random_lastname(self):
        if self.sex == 'female':
            return random.choice(female_lastname_list)
        else:
            return random.choice(male_lastname_list)
    def random_phone(self):
        num = random.choice(number_list)
        number_list.remove(num)
        return num
class Doctor(object):
    ID = 1
    def __init__(self):
        self.ID = Doctor.ID
        self.sex = random.choice(['female', 'male'])
        self.name = self.random_name()
        self.lastname = self.random_lastname()
        self.phone_number = self.random_phone()
        self.specialization = random.randint(1,Specialization.ID-1)
        Doctor.ID +=1
    def display(self):
        print(self.ID,self.name, self.lastname, self.sex , self.phone_number,self.specialization)
    def random_name(self):
        if self.sex == 'female':
            return random.choice(female_name_list)
        else:
            return random.choice(male_name_list)

    def random_lastname(self):
        if self.sex == 'female':
            return random.choice(female_lastname_list)
        else:
            return random.choice(male_lastname_list)
    def random_phone(self):
        num = random.choice(number_list)
        number_list.remove(num)
        return num
    def insert(self):
        return f"""INSERT INTO lekarze VALUES ({self.ID}, '{self.name}', '{self.lastname}', '{self.phone_number}', {self.specialization})"""
class Animal(object):
    """docstring for Animal"""
    ID = 1
    def __init__(self):
        super(Animal, self).__init__()
        self.ID = Animal.ID
        self.speciesFK = random.randint(1,Species.ID-1)
        self.age = round(random.uniform(0,10),2)
        self.weight = self.random_weight()
        self.famele = random.choice([1,0])
        self.name = self.random_name()
        self.ownerFK = random.randint(1,Person.ID-1)
        Animal.ID += 1
    def display(self):
        print(self.ID,self.name,self.age,self.weight,self.famele,self.ownerFK,self.speciesFK)
    def insert(self):
        return f"""INSERT INTO zwierzeta 
        (id_zwierzecia, imie, wiek, waga, samica, wlasciciele_id_wlasciciela, gatunek_id_gatunku)
        VALUES ({self.ID}, '{self.name}', {self.age}, {self.weight}, {self.famele}, {self.ownerFK}, {self.speciesFK})"""
        
    def random_weight(self):
        if self.speciesFK ==1: #pies
            return round(random.uniform(1.5, 10000), 2)
        elif self.speciesFK ==2:#kot
            return round(random.uniform(4000, 5000), 2)
        elif self.speciesFK ==3:#ptak
            return round(random.uniform(40, 2000), 2)
        elif self.speciesFK ==4:#gad
            return round(random.uniform(1000, 75000), 2)
        elif self.speciesFK ==5:#gryzon
            return round(random.uniform(60, 100), 2)
        else:
            return -1

    def random_name(self):
        if self.famele == 1:
            return random.choice(female_name_list)
        else:
            return random.choice(male_name_list)

class Prescription(object):
    """docstring for Prescription"""
    ID = 1
    def __init__(self):
        super(Prescription, self).__init__()
        self.ID = Prescription.ID
        self.data = self.rand_date()
        self.status = random.choice([False,True])
        self.doctorFK = random.randint(1,Doctor.ID-1)
        Prescription.ID += 1
    def rand_date(self):
        month31 = [1,3,5,7,8,10,12]
        year = random.randint(2015,2023)

        mon = random.randint(1,12)
        if mon ==2:
            day = random.randint(1,28)
        elif mon in month31:
            day = random.randint(1,31)
        else:
            day = random.randint(1,30)
        return f'{year}/{mon}/{day}'
    def display(self):
        print(self.ID,self.data,self.status,self.doctorFK)
class Stockroom(object):
    """docstring for Stockroom"""
    ID = 1 
    def __init__(self,name,producer,price):
        super(Stockroom, self).__init__()
        self.ID = Stockroom.ID
        self.name = name
        self.count = random.randint(0,100)
        self.producer = producer
        self.price = price
        Stockroom.ID += 1
        
    def display(self):
        print(self.ID,self.name,self.count,self.producer,self.price)
    def insert(self):
        return f"INSERT INTO magazyn (id_magazyn, nazwa, ilosc, producent, cena) VALUES ({self.ID}, '{self.name}', {self.count}, '{self.producer}', {self.price})"
#################################################
class History_disease(object):
    """docstring for History_disease"""
    ID = 1
    def __init__(self):
        super(History_disease, self).__init__()
        self.ID = History_disease.ID
        self.data = None
        self.description = None
        self.animalFK = None
        History_disease.ID += 1
class Zabieg(object):
    """docstring for Zabieg"""
    ID = 1
    def __init__(self):
        super(Zabieg, self).__init__()
        self.ID = Zabieg.ID
        self.data = self.rand_date()
        self.time = random.randint(30,60)
        self.znieczulenie = random.choice([True,False])
        self.animalFK = random.randint(1,Animal.ID-1)
        self.doctorFK = random.randint(1,Doctor.ID-1)
        self.med_treFK = random.randint(1,Medical_treatment.ID-1)

        Zabieg.ID+=1
    
    def rand_date(self):
        month31 = [1,3,5,7,8,10,12]
        year = random.randint(2015,2023)

        mon = random.randint(1,12)
        if mon ==2:
            day = random.randint(1,28)
        elif mon in month31:
            day = random.randint(1,31)
        else:
            day = random.randint(1,30)
        return f'{year}/{mon}/{day}'
    def display(self):
        print(self.ID,self.data,self.time,self.znieczulenie,self.animalFK,self.doctorFK,self.med_treFK)
class Wizyta(object):
    ID =1
    def __init__(self): ## Powinieniem podawać 
        self.ID = Wizyta.ID
        # self.zabiegFK = self.rand_zab()
        self.cont_visFK = random.randint(1,Control_visit.ID-1)
        self.data = self.rand_date()
        self.koszt = self.get_koszt()
        self.status = random.choice([True,False])
        self.animalFK = random.randint(1,Animal.ID-1)
        Wizyta.ID += 1
        pass    
    def rand_zab(self) :
        rnd_id = random.randint(0,Zabieg.ID-1 if Zabieg.ID-1 >0 else 0 )
        if rnd_id ==0 :
            return None
        else:
            return rnd_id
    def rand_date(self):
        month31 = [1,3,5,7,8,10,12]
        year = random.randint(2015,2023)

        mon = random.randint(1,12)
        if mon ==2:
            day = random.randint(1,28)
        elif mon in month31:
            day = random.randint(1,31)
        else:
            day = random.randint(1,30)
        return f'{year}/{mon}/{day}'
    
    def get_koszt(self):
        return allControl_visit[self.cont_visFK-1].cena #+ (0 if self.zabiegFK ==None else 213.7 )
    def display(self):
        print(self.ID,self.data,self.koszt,self.status,self.animalFK,self.cont_visFK)

#################################################

def generate(ilosc):
    global allPerson
    global allDoc
    global allAnimal
    global allItem
    global allH_M
    global allWizyty
    global allPrescription
    for p in range(ilosc): #niezależne
        allPerson.append(Person())
        allDoc.append(Doctor())
    for p in range(ilosc):#zależne 
        allAnimal.append(Animal())
        allPrescription.append(Prescription())
    for p in range(ilosc):
        allWizyty.append(Wizyta())
        allZabiegi.append(Zabieg())
    for p in range(len(items)):#ręczne
        allItem.append(Stockroom(items[p][0],items[p][1],items[p][2]))
    
    insert = connection.cursor()
    for p in allPerson:
        sql = (p.insert())
        insert.execute(sql)
    for p in allSpecialization:
        sql = (p.insert())
        insert.execute(sql)
    for p in allSpecies:
        sql = (p.insert())
        insert.execute(sql)
    for p in allDisease:
        sql = (p.insert())
        insert.execute(sql)
    for p in allControl_visit:
        sql = (p.insert())
        insert.execute(sql)
    for p in allMedical_treatment:
        sql = (p.insert())
        insert.execute(sql)
    for p in allAnimal:
        sql = (p.insert())
        insert.execute(sql)
    for p in allItem:
        sql = (p.insert())
        insert.execute(sql)
    for p in allDoc:
        sql = (p.insert())
        insert.execute(sql)
    pass
    insert.close()
    connection.commit()
def display_all():

    print('\nPersons\n')
    for x in allPerson:
        x.display()
    print('\nDoctors\n')
    for x in allDoc:
        x.display()
    print('\nAnimals\n')
    for x in allAnimal:
        x.display()
    print('\nItems\n')
    for x in allItem:
        x.display()
    print('\nSpecies\n')
    for x in allSpecies:
        x.display()
    print('\nSpecialization\n')
    for x in allSpecialization:
        x.display()

    print('\nMedical treatment\n')
    for x in allMedical_treatment:
        x.display()
    print('\nDisease\n')
    for x in allDisease:
        x.display()
    print('\nControl visit\n')
    for x in allControl_visit:
        x.display()
    print('\nVisit\n')
    for x in allWizyty:
        x.display()
    print('\nZabiegi\n')
    for x in allZabiegi:
        x.display()
    print('\nPrescription\n')
    for x in allPrescription:
        x.display()



def SELECT_WLASCICIELE():
    cursor.execute("""
    SELECT id_wlasciciela, imie, nazwisko, adres, nr_tel
    FROM WLASCICIELE
    """)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        adres = row[3]
        miejscowosc = getattr(adres,'MIEJSCOWOSC')
        ulica = getattr(adres,'ULICA')
        numer_domu = getattr(adres,'NUMER_DOMU')
        wojewodztwo = getattr(adres,'WOJEWODZTWO')
        tmp = (miejscowosc, ulica, int(numer_domu), wojewodztwo)
        print(f"{row[0]}) {row[1]} {row[2]} | {tmp[3]} {tmp[0]} {tmp[1]} {tmp[2]} | {row[4]}")
    pass
def MenuDisplay():
    print("""
    1) Symulacja
    2) CREATE
    3) DROP
    4) EXIT
    """)
tables = []
def CREATE_DATABASE():
        create = connection.cursor()
        create.execute(
            """
            CREATE OR REPLACE TYPE adres AS OBJECT (
                miejscowosc VARCHAR2(50),
                ulica       VARCHAR2(50),
                numer_domu  INTEGER,
                wojewodztwo VARCHAR2(50)
            ) NOT FINAL
            """
        )
        create.execute("""
        CREATE TABLE choroba (
            id_choroba INTEGER NOT NULL,
            nazwa      VARCHAR2(50))""")
        create.execute("ALTER TABLE choroba ADD CONSTRAINT choroba_pk PRIMARY KEY ( id_choroba )")
        create.execute("""CREATE TABLE choroba_historia (
    id_ch INTEGER NOT NULL,
    historia_chorob_id_historia INTEGER NOT NULL,
    choroba_id_choroba          INTEGER NOT NULL
)""")
        create.execute("ALTER TABLE choroba_historia ADD CONSTRAINT choroba_historia_pk PRIMARY KEY ( id_ch,historia_chorob_id_historia,choroba_id_choroba )")
        create.execute("""CREATE TABLE gatunek (
    id_gatunku INTEGER NOT NULL,
    nazwa      VARCHAR2(30)
)""")
        create.execute("ALTER TABLE gatunek ADD CONSTRAINT gatunek_pk PRIMARY KEY ( id_gatunku )")
        create.execute("""
        CREATE TABLE historia_chorob (
    id_historia             INTEGER NOT NULL,
    data_diagnozy           DATE,
    zalecane_leczenie       CLOB,
    zwierzeta_id_zwierzecia INTEGER NOT NULL
    )
        """)
        create.execute("ALTER TABLE historia_chorob ADD CONSTRAINT historia_chorob_pk PRIMARY KEY ( id_historia )")
        create.execute("""CREATE TABLE lekarze (
    id_lekarz                      INTEGER NOT NULL,
    imie                           VARCHAR2(30),
    nazwisko                       VARCHAR2(30),
    nr_tel                         VARCHAR2(9),
    specjalizacja_id_specjalizacja INTEGER NOT NULL
)""")
        create.execute("ALTER TABLE lekarze ADD CONSTRAINT lekarze_pk PRIMARY KEY ( id_lekarz )")
        create.execute("""CREATE TABLE magazyn (
    id_magazyn INTEGER NOT NULL,
    nazwa      VARCHAR2(100),
    ilosc      INTEGER,
    producent  VARCHAR2(50),
    cena       NUMBER
)""")
        create.execute("ALTER TABLE magazyn ADD CONSTRAINT magazyn_pk PRIMARY KEY ( id_magazyn )")
        create.execute("""CREATE TABLE magazyn_recepta (
    id_mag INTEGER NOT NULL,
    magazyn_id_magazyn INTEGER NOT NULL,
    recepty_id_recepty INTEGER NOT NULL
)""")
        create.execute("ALTER TABLE magazyn_recepta ADD CONSTRAINT magazyn_recepta_pk PRIMARY KEY ( id_mag,magazyn_id_magazyn,recepty_id_recepty )")
        create.execute("""CREATE TABLE recepty (
    id_recepty        INTEGER NOT NULL,
    data              DATE,
    stan_platnosci    NUMBER,
    lekarze_id_lekarz INTEGER NOT NULL
)""")
        create.execute("ALTER TABLE recepty ADD CONSTRAINT recepty_pk PRIMARY KEY ( id_recepty )")
        create.execute("""CREATE TABLE rodzaj_wizyty (
    id_rodz_wiz INTEGER NOT NULL,
    nazwa       VARCHAR2(30),
    cena	NUMBER
)""")
        create.execute("ALTER TABLE rodzaj_wizyty ADD CONSTRAINT rodzaj_wizyty_pk PRIMARY KEY ( id_rodz_wiz )")
        create.execute("""CREATE TABLE rodzaj_zabiegu (
    id_rodz_zab INTEGER NOT NULL,
    nazwa       VARCHAR2(30)
)""")
        create.execute("""ALTER TABLE rodzaj_zabiegu ADD CONSTRAINT rodzaj_zabiegu_pk PRIMARY KEY ( id_rodz_zab )""")
        create.execute("""CREATE TABLE specjalizacja (
    id_specjalizacja    INTEGER NOT NULL,
    nazwa_specjalizacji VARCHAR2(30)
)""")
        create.execute("ALTER TABLE specjalizacja ADD CONSTRAINT specjalizacja_pk PRIMARY KEY ( id_specjalizacja )")
        create.execute("""CREATE TABLE wizyty (
    id_wizyt                 INTEGER NOT NULL,
    data                     DATE,
    koszt                    NUMBER,
    stan_tranzakcji          NUMBER,
    zwierzeta_id_zwierzecia  INTEGER NOT NULL,
    zabiegi_id_zabieg        INTEGER,
    rodzaj_wizyty_id_rodz_wiz INTEGER NOT NULL
)""")
        create.execute("ALTER TABLE wizyty ADD CONSTRAINT wizyty_pk PRIMARY KEY ( id_wizyt )")
        create.execute("""CREATE TABLE wlasciciele (
    id_wlasciciela INTEGER NOT NULL,
    imie           VARCHAR2(30),
    nazwisko       VARCHAR2(30),
    adres          adres,
    nr_tel         VARCHAR2(9)
)""")
        create.execute("ALTER TABLE wlasciciele ADD CONSTRAINT wlasciciele_pk PRIMARY KEY ( id_wlasciciela )")
        create.execute("""CREATE TABLE zabiegi (
    id_zabieg                  INTEGER NOT NULL,
    data                       DATE,
    czas                       INTEGER,
    znieczulenie               NUMBER,
    zwierzeta_id_zwierzecia    INTEGER NOT NULL,
    lekarze_id_lekarz          INTEGER NOT NULL,
    rodzaj_zabiegu_id_rodz_zab INTEGER NOT NULL,
    id_wizyt                   INTEGER NOT NULL
)""")
        create.execute("ALTER TABLE zabiegi ADD CONSTRAINT zabiegi_pk PRIMARY KEY ( id_zabieg )")
        create.execute("""
CREATE TABLE zwierzeta (
    id_zwierzecia              INTEGER NOT NULL,
    imie                       VARCHAR2(30),
    wiek                       FLOAT(4),
    waga                       INTEGER,
    samica                     NUMBER,
    wlasciciele_id_wlasciciela INTEGER NOT NULL,
    gatunek_id_gatunku         INTEGER NOT NULL
)""")
        create.execute("ALTER TABLE zwierzeta ADD CONSTRAINT zwierzeta_pk PRIMARY KEY ( id_zwierzecia )")
        create.execute("""ALTER TABLE choroba_historia
    ADD CONSTRAINT choroba_historia_choroba_fk FOREIGN KEY ( id_ch )
        REFERENCES choroba ( id_choroba )""")
        create.execute("""ALTER TABLE historia_chorob
    ADD CONSTRAINT historia_chorob_zwierzeta_fk FOREIGN KEY ( zwierzeta_id_zwierzecia )
        REFERENCES zwierzeta ( id_zwierzecia )""")
        create.execute("""ALTER TABLE lekarze
    ADD CONSTRAINT lekarze_specjalizacja_fk FOREIGN KEY ( specjalizacja_id_specjalizacja )
        REFERENCES specjalizacja ( id_specjalizacja )""")
        create.execute("""ALTER TABLE choroba_historia
    ADD CONSTRAINT lista_chorob_fk FOREIGN KEY ( id_ch )
        REFERENCES historia_chorob ( id_historia )""")
        create.execute("""ALTER TABLE magazyn_recepta
    ADD CONSTRAINT magazyn_recepta_magazyn_fk FOREIGN KEY ( id_mag )
        REFERENCES magazyn ( id_magazyn )""")
        create.execute("""ALTER TABLE magazyn_recepta
    ADD CONSTRAINT magazyn_recepta_recepty_fk FOREIGN KEY ( id_mag )
        REFERENCES recepty ( id_recepty )""")
        create.execute("""ALTER TABLE recepty
    ADD CONSTRAINT recepty_lekarze_fk FOREIGN KEY ( lekarze_id_lekarz )
        REFERENCES lekarze ( id_lekarz )""")
        create.execute("""ALTER TABLE wizyty
    ADD CONSTRAINT wizyty_rodzaj_wizyty_fk FOREIGN KEY ( rodzaj_wizyty_id_rodz_wiz )
        REFERENCES rodzaj_wizyty ( id_rodz_wiz )""")
        create.execute("""ALTER TABLE wizyty
    ADD CONSTRAINT wizyty_zabiegi_fk FOREIGN KEY ( zabiegi_id_zabieg )
        REFERENCES zabiegi ( id_zabieg )""")
        create.execute("""ALTER TABLE wizyty
    ADD CONSTRAINT wizyty_zwierzeta_fk FOREIGN KEY ( zwierzeta_id_zwierzecia )
        REFERENCES zwierzeta ( id_zwierzecia )""")
        create.execute("""ALTER TABLE zabiegi
    ADD CONSTRAINT zabiegi_lekarze_fk FOREIGN KEY ( lekarze_id_lekarz )
        REFERENCES lekarze ( id_lekarz )""")
        create.execute("""ALTER TABLE zabiegi
    ADD CONSTRAINT zabiegi_rodzaj_zabiegu_fk FOREIGN KEY ( rodzaj_zabiegu_id_rodz_zab )
        REFERENCES rodzaj_zabiegu ( id_rodz_zab )""")
        create.execute("""ALTER TABLE zabiegi
    ADD CONSTRAINT zabiegi_zwierzeta_fk FOREIGN KEY ( zwierzeta_id_zwierzecia )
        REFERENCES zwierzeta ( id_zwierzecia )""")
        create.execute("""ALTER TABLE zwierzeta
    ADD CONSTRAINT zwierzeta_gatunek_fk FOREIGN KEY ( gatunek_id_gatunku )
        REFERENCES gatunek ( id_gatunku )""")
        create.execute("""ALTER TABLE zwierzeta
    ADD CONSTRAINT zwierzeta_wlasciciele_fk FOREIGN KEY ( wlasciciele_id_wlasciciela )
        REFERENCES wlasciciele ( id_wlasciciela )""")
        create.close()
        connection.commit()
        
        pass
if __name__ == '__main__':
    connection = oracledb.connect(
    user=username,
    password=password,
    dsn=dsn)
    cursor = connection.cursor()
    while True:
        MenuDisplay()
        prompt = input('>')
        if prompt == "1":
            
            cursor.execute("""
            SELECT object_name, object_type 
            FROM user_objects 
            WHERE object_type 
            IN ('TABLE', 'VIEW', 'PACKAGE', 'PROCEDURE', 'FUNCTION', 'SEQUENCE', 'SYNONYM', 'PACKAGE BODY' )""")
            rows = cursor.fetchall()
            index = 1
            for row in rows:
                tables.append((index, row[0]))
                index += 1
            for table in tables:
                print(f'{table[0]}) {table[1]}')
            select_table = int(input("Wybierz tabelę >"))
            generate(100)
            # if select_table == 1:
            #     SELECT_CHOROBA()
            # elif select_table == 2:
            #     SELECT_CHOROBA_HISTORIA()
            # elif select_table == 3:
            #     SELECT_GATUNEK()
            # elif select_table == 4:
            #     SELECT_HISTORIA_CHOROB()
            # elif select_table == 5:
            #     SELECT_LEKARZE()
            # elif select_table == 6:
            #     SELECT_MAGAZYN()
            # elif select_table == 7:
            #     SELECT_MAGAZYN_RECEPTA()
            # elif select_table == 8:
            #     SELECT_RECEPTY()
            # elif select_table == 9:
            #     SELECT_RODZAJ_WIZYTY()
            # elif select_table == 10:
            #     SELECT_RODZAJ_ZABIEGU()
            # elif select_table == 11:
            #     SELECT_SPECJALIZACJA()
            # elif select_table == 12:
            #     SELECT_WIZYTY()
            # elif select_table == 13:
            #     SELECT_WLASCICIELE()
            # elif select_table == 14:
            #     SELECT_ZABIEGI()
            # elif select_table == 15:
            #     SELECT_ZWIERZETA()
                
        elif prompt =="2":
            print("CREATE")
            CREATE_DATABASE()
            connection.commit()


        elif prompt=="3":
            print("DROP")
            drop = connection.cursor()
            
            drop.execute('DROP TABLE choroba CASCADE CONSTRAINTS')
            drop.execute('DROP TABLE choroba_historia CASCADE CONSTRAINTS')
            drop.execute('DROP TABLE gatunek CASCADE CONSTRAINTS')
            drop.execute('DROP TABLE historia_chorob CASCADE CONSTRAINTS')
            drop.execute('DROP TABLE lekarze CASCADE CONSTRAINTS')
            drop.execute('DROP TABLE magazyn CASCADE CONSTRAINTS')
            drop.execute('DROP TABLE magazyn_recepta CASCADE CONSTRAINTS')
            drop.execute('DROP TABLE recepty CASCADE CONSTRAINTS')
            drop.execute('DROP TABLE rodzaj_wizyty CASCADE CONSTRAINTS')
            drop.execute('DROP TABLE rodzaj_zabiegu CASCADE CONSTRAINTS')
            drop.execute('DROP TABLE specjalizacja CASCADE CONSTRAINTS')
            drop.execute('DROP TABLE wizyty CASCADE CONSTRAINTS')
            drop.execute('DROP TABLE wlasciciele CASCADE CONSTRAINTS')
            drop.execute('DROP TABLE zabiegi CASCADE CONSTRAINTS')
            drop.execute('DROP TABLE zwierzeta CASCADE CONSTRAINTS')

            drop.close()
        elif prompt =="4":
            
            cursor.close()
            connection.close()
            
            exit(0)

    

    # display_all()
    pass
    


    