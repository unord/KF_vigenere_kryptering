from krypter import krypter
from dekrypter import dekrypter

def startup():
    input1 = input("Goddag, venligst vaelg en handling: krypter, dekrypter")

    if input1 == "krypter":
        text = input("Venligst skriv den tekst du vil kryptere:")
        print("Den dekrypterede tekst er: ", krypter(text))
    elif input1 == "dekrypter":
        text = input("Venligst skriv den tekst du vil dekryptere:")
        print("Den dekrypterede tekst er: ", dekrypter(text))
    else:
        print("Den skrevne kommando er ikke registeret. Husk at bruge lowercase, når du skriver kommandoer.")
        startup()
startup()

#Simpelt program der kun kører 1 gang, med mindre du skriver en kommando forkert