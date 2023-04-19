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
dsn = f'{hostname}:{port}/{servicename}'
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
    else:
        print("File Exists") 

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
class Control_visit(object):
    """docstring for Control_visit"""
    ID = 1
    def __init__(self, name):
        super(Control_visit, self).__init__()
        self.ID = Control_visit.ID
        self.name = name
        Control_visit.ID += 1
    def display(self):
        print(self.ID,self.name)
#################################################        

allPerson = []
allDoc = []
allAnimal = []
allItem = []
allSpecies = []
allSpecialization=[]
#------------
allMedical_treatment = []
allDisease =[]
#------------
allControl_visit = []


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
    def display(self):
        print(self.ID,self.name, self.lastname, self.sex , self.phone_number,self.address)
    def random_adress(self):
        adress = (random.choice(city_list),random.choice(street_list),random.randint(1,99))
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
        self.data = None
        self.status = False
        self.doctorFK = None
        Prescription.ID += 1
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
        self.arg = Zabieg.ID
        self.data = None
        self.time = None
        self.znieczulenie = True
        self.animalFK = None
        self.doctorFK = None
        self.med_treFK = None
        self.visitFK = None
        Zabieg.ID+=1
class Visit(object):
        """docstring for Visit"""
        ID = 1
        def __init__(self):
            super(Visit, self).__init__()
            self.ID = Visit.ID
            self.data = None
            self.koszt = None
            self.status = None
            self.animalFK = None
            self.c_visitFK = None
            self.med_treFK = None

            Visit.ID += 1
                
#################################################

def generate(ilosc):
    global allPerson
    global allDoc
    global allAnimal
    global allItem
    for p in range(ilosc): #niezależne
        allPerson +=[Person()]
        allDoc +=[Doctor()]
    for p in range(ilosc):#zależne 
        allAnimal +=[Animal()]
    for p in range(len(items)):#ręczne
        allItem += [Stockroom(items[p][0],items[p][1],items[p][2])] 

    pass

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
if __name__ == '__main__':
    connection = oracledb.connect(
    user=username,
    password=password,
    dsn=dsn)
    cursor = connection.cursor()
    query = cursor.execute("SELECT * FROM CHOROBA")
    for row in query:
        print(row)
    connection.close()
    generate(100)
    display_all()
    