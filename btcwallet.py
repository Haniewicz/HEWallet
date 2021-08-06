from pywallet import wallet
import datetime
from functions.encryption import *
from functions.file_actions import *
from functions.handling import *
import os
import os.path
import re
import random
import pywallet
import string

if not os.path.isdir("wallets"):
    os.system("mkdir wallets")

def error(msg):
    os.system("cls")
    print(msg + " co chcesz teraz zrobić:")
    print("1. Powrót do menu")
    print("2. Zamknij program")
    choice = input("Wybór: ")
    if choice == "1":
        menu()
    elif choice == "2":
        exit()
    else:
        error(error1)
def success(msg):
    os.system("cls")
    print(msg + " co chcesz teraz zrobić:")
    print("1. Powrót do menu")
    print("2. Zamknij program")
    choice = input("Wybór: ")
    if choice == "1":
        menu()
    elif choice == "2":
        exit()
    else:
        error(error1)

def generate_wallet():
    # generate 12 word mnemonic seed
    seed = wallet.generate_mnemonic()

    # create bitcoin wallet
    w = wallet.create_wallet(network="BTC", seed=seed, children=1)
    return w

def save_wallet(name, seed):
    w = generate_wallet()
    f = open("wallets/"+name+".txt", "a")
    f.write("Coin: "+ w["coin"] + "\n" +
            "Seed: " + encrypt(generate_scheme(seed), w["seed"]) + "\n" +
            "Adres: "+w["address"] + "\n" +
            "Klucz prywatny: "+ encrypt(generate_scheme(seed), w["xprivate_key"]) + "\n" +
            "Klucz publiczny: "+ w["xpublic_key"] + "\n")
    f.close()

def delete_menu():
    choice = input("Nazwa portfela lub 0:  ")
    if choice == "0":
        menu()
    elif choice != "0":
        if os.path.isfile("wallets/"+choice+".txt"):
            os.remove("wallets/"+choice+".txt")
            success("Portfel poprawnie usunięty!")
        else:
            error("Nieprawidłowa nazwa portfela do usunięcia!")

def menu():
    os.system("cls")
    print("Witaj w swoim nowym szyfrowanym portfelu kryptowalutowym. Co chcesz zrobić:\n")
    print("1. Stwórz nowy portfel")
    print("2. Usuń istniejący portfel")
    print("3. Zobacz portfel")
    print("4. Zamknij program")
    choice = input("Wybór: ")

    if choice == "1":
        os.system("cls")
        name = input("Podaj nazwę swojego portfela (0 nie może być nazwą): ")
        seed = input("Podaj hasło do szyfrowania: ")
        if name != "" and name != "0" and seed != "":
            save_wallet(name, seed)
            success("Portfel utworzony!")
        else:
            error("Nie podałeś nazwy portfela lub seedu szyfrowania lub próbowałeś nazwać portfel nazwą 0,")
    elif choice == "2":
        os.system("cls")
        print("Oto twoje dostępne portfele. Wpisz nazwę portfela który chcesz usunąć lub 0 jeśli chcesz wrócić do menu.")
        list_wallets()
        delete_menu()
    elif choice == "3":
        os.system("cls")
        print("Oto twoje dostępne portfele. Wpisz nazwę portfela który chcesz zobaczyć lub 0 jeśli chcesz wrócić do menu.")
        list_wallets()
        name = input("Nazwa portfela lub 0: ")
        if os.path.isfile("wallets/"+name+".txt"):
            os.system("cls")
            print("Portfel: "+name)
            klucz = input("Hasło: ")
            os.system("cls")
            decrypt(generate_scheme(klucz), name)
            print("\n")
            choice = input("Aby wrócić do menu wybierz 0, a żeby zamknąć program wybierz 1: ")
            if choice == "0":
                menu()
            elif choice == "1":
                exit()
            else:
                error(error1)
        elif name == "0":
            menu()
        else:
            error("Nieprawidłowa nazwa portfela do usunięcia!")
    elif choice == "4":
        exit()

menu()
