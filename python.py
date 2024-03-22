# stampo i numeri pari fino a 7
cont=0
for i in range(0, 30 + 1):
    if i % 2 == 0:
        print(i, 'Pari')
        cont += 1  

    if cont >= 7:
        break


# stampo quante m ci sono nella frase
string = 'lorem ipsium mamma mia'
contatore_m= 0
for letter in string:
    if letter == 'm':
        contatore_m += 1
print('La lettera m appare ', contatore_m, ' volte')

# stampo i numeri da 0 a 6
n = 0

while n <= 6:
    print(n)
    n += 1

# stampo la serie di fibonacci fino a 10
x = 0
y = 1
s = 0
while s < 10:
    print(s)
    x = y
    y = s
    s = x + y 

# stampo la teballina del 7
tab = 7
molt = 1

while molt <= 10:
    print(tab, 'x', molt, '=', tab * molt)
    molt += 1

# stampo sempre la tabellina del 7 ma con il ciclo for
tab = 7
for i in range(1,11):
    print(tab, 'x', i, '=', tab*i)

# Metto in ordine crescente e alfabetico gli array
    
numbers = [10,10000,-3,98,32,-23]
names = ['pippo', 'pluto', 'paperino', 'topolino', 'carla', 'giuliano']
l = len(numbers)
numbers.sort()
print(numbers)
names.sort()
print(names)


# Stampo la media dei numeri
avarage = 0 
sum = 0 
for i in numbers:
    print("Sono l'elemento ", i)
    sum += i

avarage = sum / len(numbers)
print(avarage) 

# metodo split

s = 'lorem ipsum dolor sit amet hello spitto hello due hello 6 hello'

l = s.split()
cont = 0

for i in l:
    if i == 'hello':
        cont += 1
        
print("La parola Hello è contenuta ",  cont, " volte")

# tupla -> oggetto immutabile, operazioni più veloci rispetto ad una lista, si usano le parentesi tonde.
# es. t = (1,2,3)

car = {
    'brand': 'Ford',
    'model': 'Mustang',
}

print(car.get('brand'))

del car['brand'] # per eliminare una chiave, uso "del"
print(car)

movies = [{
    "titolo" : "Avengers",
    "regia" : "Marvel",
    "anno" : "2012",
    "genere" : "Action"
    
},
{
    "titolo" : "Forest Gump",
    "regia" : "Robert",
    "anno" : "2008",
    "genere" : "Drammatico" 
}]

for movie in movies:
    print(movie.get('titolo'), "Regia di:", movie.get("regia") )
    print("Anno di produzione:", movie.get('anno'))
    print("Genere:", movie.get('genere'))


# un set-> assomigliano gl'insiemi in matematica, si usano le parentesi graffe. Sono ordinati, univoci e modificabili. (l'univocità nel senso che se, per esempio, ripeto due volte "mario", me ne riporterà solo 1)
    
x = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
x2 = {1,11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    
x.union(x2) # unisco i due set
x.intersection(x2) # interseco i due set, mi compare quale hanno in comune

# charset ed encoding

# charset ascii -> praticamente come il pc codifica le varie lettere,numeri ecc che noi digitiamo da alto livello(a,b,c, tutto quello che scriviamo) al basso livello(codice macchina)

# .format si usa quando devo stampare una stringa con più variabili dentro, in questo caso voglio stampare il nome, cognome e l'età.

first_name = 'Mario'
last_name = 'Rossi'
age = '19'
print("{} {} is a nice guy and he's {} years old".format(first_name,last_name,age))

# nelle versioni più recenti di python, posso usare anche il metodo f-string, in questo caso voglio stampare il nome, cognome e l'età.

print(f"{first_name} {last_name} is a nice guy and he's {age} years old") #avrò lo stesso risultato di quello sopra

# \n stampa in una nuova riga
# \t stampa una tabulazione (spazio usando tab)

import sys
import decimal
import math 


a = 0
print(sys.getsizeof(a)) # stampa la dimensione in byte della variabile




def calc(num = []):
    pari = []
    dispari = []
    for i in num:
        if i % 2 == 0:
            pari.append("{} Pari".format(i))
        else:
            dispari.append("{} Dispari".format(i))
    return pari, dispari
pari, dispari = calc(num = [1,2,3,4,5,6,7,8,9,10,11,12])
print(" ".join(pari + dispari))


# apertura file

# stampa tutto il contunto
with open('file.txt', mode='r') as file:
    c= file.readlines()
    print(c)

print("\n")

# stampa una riga alla volta
with open('file.txt', mode='r') as file:
    cont = file.readline()
    while cont:
        print(cont)
        cont = file.readline()

print("\n")

# stampa una riga alla volta con il metodo read()
with open('file.txt', mode='r') as file:
    line = file.read()
    print(line)

print("\n")

# stampa il contenuto e va a capo ogni 8 caratteri
with open('file.txt', mode='r') as file:
    chunk_size = 8
    contenuto = file.read(chunk_size)
    while contenuto:
        print(contenuto)
        contenuto = file.read(chunk_size)

print("\n")

# contuto del file riga per riga
with open('file.txt', mode='r') as file:
    for line in file:
        print(line)

print("\n")

with open('file.txt', mode='r') as file:
    c = file.read(1) #qui sto dicendo di stampare solo il primo carattere
    print(c)

print("\n")

with open('file.txt', mode='rb') as file: #con la modifica della modalità(rb = modalità binaria) qui vado a stampare in modalità binaria
    ci = file.read(1) #qui sto dicendo di stampare solo il primo bite
    print(ci)

# Riga 30 readme
with open('file.txt', mode='rb') as file:
    c = file.readline()
    c = file.readline()

    print(f"Posizione puntatore: {file.tell()}")
    print(f"Settiamo il puntatore a -10 byte dalla fine del file")
    file.seek(-30, 2)
    print(file.read(30))

# Qui creo un file da zero, gli inserisco la parola hello, poi mi sposto con file.seek all'inizio del file e ci aggiungo la lettere m
    
with open("to_write.txt", mode='w') as file:
    file.write("hello")
    file.seek(0)
    file.write("M")

#qui andiamo a copiare una foto, aggiungendo all'interno una scritta "nascosta", ovvero che semplicemente visualizzando l'immagine non troveremmo, ma dovremmo usare un editor esadecimale(hexed) per riuscire a vedere la scritta aggiunta.
    
with open("Afressia.jpeg", mode= 'rb') as reader:
    with open("Afressia_copy.jpeg", mode='wb') as writer:
        writer.write(reader.read()) #leggo e copio il contenuto in byte
        reader.seek(-2,2) #mi sposto all'indietro di 2 byte partendo dalla fine del file
        tail = reader.read(2) #memorizzo gli ultimi due byte 
        writer.seek(-2,2) #mi sposto all'indietro di 2 byte partendo dalla fine del file
        writer.write(b"HELLO, STEGANOGRAPHY IS BEAUTIFUL") #scrivo il messaggio che va inserito dopo essermi spostato di 2 byte prima della fine del file
        writer.write(tail) #aggiungo i due byte che mi servono per tornare alla fine del file


# mutability

a = 500
b = 500

print(a == b) # stampa true 
print(a is b) # stampa false, va a ricercare l'id della variabile, ed essendo due varibili diverse, hanno id diverso.


#In questo caso la lista 2 prende sia le variabili contenuti in list 1, sia l'id, percui sono completamente uguali.
list1 = [1, 2, 3]
list2 = list1
print(list1 is list2)
print(list1 == list2)

#se però andassimo a modificare la lista due, automaticamente andremmo a modificare anche la lista 1. Es.
list2.append(4)
print("list1", list1)
print("list2", list2)
print(list1 is list2)
print(list1 == list2)
#in questo caso da come risultato che viene aggiunto il numero 4 anche nella lista 1.

#possiamo schivare questo problema facendo una copia della lista

#in questo caso passiamo alla funzione due liste. La funzione ha le variabili locali "n" e "v" che si riferiscono rispettivamente allo stesso oggetto a cui si riferiscono list1 e list2
#La funzione assegna "n" all'oggetto a cui si riferisce "v". Quindi "n" e "v" si riferiscono allo stesso oggetto. Quindi "n" e "v" e "list2" si rifersicono a tutte e tre [4,5,6]. "list1", al contrario, punta ancora all'oggetto [1,2,3], che in effetti viene poi stampato nella print finale.
def copy_ref(n,v):
    n = v

list1 = [1, 2, 3]
list2 = [4,5,6]
copy_ref(list1, list2)

#passiamo a copy_list una lista per reference. La funzione conterrà una variabile locale (n) che punta allo stesso oggetto di "l". Tuttavia, in questo caso, abbiamo usato lo "SLICE OPERATOR (:)"per creare una copia della lista e ritornarla in output alla funzione. In output avremo un reference a quella copia! Adesso "nl" si riferirà ad yb oggetto diverso da quello originariamente passato alla funzione.
def copy_list(n):
    out = n[:]
    return out
l = [1,2,3]
nl = copy_list(l)

#Creiamo due liste contententi i quadrati dei numeri presenti in una lista di partenza:
#•una con un classico ciclo for
#•una con list comprehension

#con ciclo for
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
legacy_list = []
for i in l:
    legacy_list.append(i**2)
print(legacy_list)

#con list comprehension
lc_list = [ item**2 for item in l]
print(lc_list)

# ora aggiungiamo anche una condizione

list1 = [1, 2 ,3 ,4, 5, 6, 7, 8, 9, 10]
le_list = []
for i in list1:
    if i % 2 == 0:
        le_list.append(i**2)
print(le_list)

#questo metodo è molto più compatto
lec_list = [item**2 for item in list1 if item % 2 == 0]
print(lec_list)

#qui vado a stampare 1 se è vocale, 0 se è consonante
import string

def is_volwes(n):
    return n in 'aeiouy'

def vowel_or_consonant(n):
    if is_volwes(n):
        return 1
    else:
        return 0

def not_punctation(n):
    return n not in string.punctuation #è un metodo contenuto nella libreria "string" e restituisce i caratteri (!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~)

s = 'the quick brown fox jumps over the lazy dog'
print(len(s))

vowels = [ vowel_or_consonant(i) for i in s if not_punctation(i)]
print(vowels)
print(len(vowels))

#qui vado a creare una lista di dizionari, con le chiavi e i valori che voglio inserire. In questo caso voglio inserire le chiavi "first_name", "last_name" e "age" e i valori "Mario", "Rossi", "19"
keys = ['first_name', 'last_name', 'age']
values = ['Mario', 'Rossi', '19']

person = {keys[i]:values[i]for i in range(0, len(values))}
print(person)

#vado a creare una matrice di 4 righe e 5 colonne, con i valori 0-4.
m = [[j for j in range(0, 5)] for i in range(0,4)]
print(m)

#posso fare il procedimento inverso
matrix = [[0,1,2,3,4], [5,6,7,8,9], [10,11,12,13,14], [15,16,17,18,19]]
flattened = [cell for row in matrix for cell in row]
print(flattened)

#posso agiungere anche delle condizioni ai cicli

flat = [cell for row in matrix for cell in row if cell % 4 ==0]
print(flat)
flatty = [cell if cell < 10 else "too high" for row in matrix for cell in row if cell % 4 == 0]
print(flatty)

import requests
from IPython.display import Image
from requests.exceptions import HTTPError

resp = requests.get("https://theguardian.com/")
req = resp.request

print(dir(resp))
print(dir(req))

for url in ['https://www.theguardian.com', 'https://repubblica.it/doesNotExist']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(type(http_err))
        print(dir(http_err))
        print(f'HTTP error: {http_err}')
    except Exception as err:
        print(f'Gerenic error: {err}')
    else:
        print('Success!!')

# ad esempio per scaricare immagini
        
image = requests.get("https://images.unsplash.com/photo-1682687982360-3fbab65f9d50?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")

with open("files/image.jpeg", "wb") as f:
    f.write(image.content)
from IPython.display import Image
Image(filename='files/image.jpeg')


#abbiamo creato una classe che funge da oggetto
class Point:
    pass
p = Point()

#definiamo un punto su un piano cartesiano

p.x = 5

class Point:
    counter = 0 #possiamo tenere traccia di quante volte facciamo girare la funzione, quello che scriviamo dentro la classe, prende il nome di attributo di classe
    def __init__(self, ascissa=0, ordinata=0):#posso assegnare dei valori di default con =0 #self rappresenta l'oggetto sul quale stiamo esguendo la funzione di turno
        #per ogni oggetto che creaiamo, creiamo un attributo il cui nome è x e il valore è n
        self.x = ascissa
        self.y = ordinata
        Point.counter += 1 #incrementiamo il contatore di 1 per ogni oggetto creato
        #quello che scriviamo dentro la funzione si chiamano attributi di istanza

        print("costruttore")

p1 = Point(3, 6)
p2 = Point(5)
p3 = Point(ordinata=7)
print(p1.x, p1.y)
print(p2.x, p2.y)
print(p3.x, p3.y)
print(Point.counter)

class Point:
    counter = 0
    def __init__(self, ascissa=0, ordinata=0):
        self.x = ascissa
        self.y = ordinata
        Point.counter += 1 
        print("Ricostruttore")
    def print_info(self):
        print (f"Punto {self.x}, {self.y}")

    def create_point_equals_x_y():
        import random
        n = random.randint(0,100)
        return Point(n, n)

x_y_equals = Point.create_point_equals_x_y()
print(x_y_equals.print_info())


#Ereditarietà
class Person:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        def greet(self):
            return f"My name is {self.first_name} {self.last_name}"
me = Person("Ismaele", "Nichele")


class Student(Person):
    def __init__(self,first_name,last_name, cdl):
        super().__init__(first_name,last_name)
        self.cdl = cdl

    def greet(self):
            return f"My name is {self.first_name} {self.last_name} (corso {self.cdl})"

class LiteratureStudent(Student):
    def __init__(self, first_name, last_name, cdl):
        super().__init__(first_name, last_name,cdl)
        

me = Person("Ismaele" ,"Nichele")
s = Student("Mario", "Rossi", "ITT")
l=Student("Luigi", "Verdi", "Lettere")

#DUNDER METHODS
class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im
    def __str__(self):
        s= f"{self.re} + i{self.im}"
        return s
    def __eq__(self,other):
        if isinstance(other, ComplexNumber):
            return self.re == other.re and self.im == other.im
        else:
            raise Exception(f"{other} is not an istance of ComplexNumber")
    def __setitem__(self, k, v):
        if k not in ['re','im']:
            raise Exception(f"{k} is not a valid key for class ComplexNumber")
        elif k=='re':
            self.re = v
        else:
            self.im = v
    def __getitem__(self, k):
        if k not in ['re','im']:
            raise Exception(f"{k} is not a valid key for class ComplexNumber")
        elif k=='re':
            return self.re
        else:
            return self.im
    def __add__(self,other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.re + other.re, self.im + other.im)
        else:
            raise Exception(f"{type(other)} is not an istance of ComplexNumber")
    def __len__(self):
        from math import sqrt #sqrt ritorna un numero float
        return int(sqrt(self.re**2 + self.im**2))
cl = ComplexNumber(5,6)
c2 = ComplexNumber(5, 6)
print(cl == c2)
print(cl, c2)
cl['re'] = 10
c2['im'] = 15
print(cl['re'])
print(c2['im'])

#Incapsulamento
class Person:
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class BankAccountOwner(Person):
    def __init__(self, first_name, last_name, bank_account_id):
        super().__init__(first_name, last_name)
        self.__bank_account_id = bank_account_id
    def __str__(self):
        return f"{super().__str__()} Con conto bancario {self.__bank_account_id}"

p1 = Person("Ismaele", "Nichele")
p2 = BankAccountOwner("Ismaele", "Nichele", "asdrew")

print(p2)
p2.__bank_account_id = "XXXX" #aggiungedo questo, l'id non cambia, perchè il doppio underscore prima di "bank_account_owner" è come se ne bloccasse la proprietà,rendendolo privato.
print(p2)

p3 = BankAccountOwner("Mario", "Rossi", "asdrew")
#il doppio underscore posso anche assegnarlo ad un metodo, rendendolo anchesso privato e non accessibile.