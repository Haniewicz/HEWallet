import random
from secrets import randbelow
import string

def random_char(y):
       return ''.join(random.choice(string.ascii_letters + '[]/!@#$%^&*()1234567890') for x in range(y))

def generate_scheme(seed):
    litery = string.printable
    klucz = {}
    random.seed(seed)
    for litera in litery:
        klucz[litera] = random_char(6)
    return klucz

def encrypt(klucz, text):
    wynik = ""
    for litera in text:
        wynik += klucz[litera]
    return wynik

def decrypt(klucz, name):
    with open('./wallets/'+name+'.txt', 'r') as plik:
        text = plik.read()
        wynik = text
        for index, value in klucz.items():
            wynik = wynik.replace(value, index)
        print(wynik)
