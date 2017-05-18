from PIL import Image
from time import sleep
from pprint import pprint
import numpy as np


def napoveda():
    print("Toto je napoveda k programu.\n Program funguje pouze pro obrazky ve formatu jpg a pro barevne provedeni RGB.\n Obrazek je potreba mit umisteny ve stejnem miste, jako je tento program.\n")


def menu():
    print("Nyni si vyber, co chces s obrazkem udelat. Upravena verze se ulozi na stejnem umisteni jako original, k tomu se otevre ve tvem defaultnim prohlizeci obrazku.")
    print("0. Zobrazit original")
    print("1. Prevraceni obrazu ve svisle ose")
    print("2. Prevraceni obrazu ve vodorovne ose")
    print("3. Rotace")
    print("4. Negativ")
    print("5. Prirozeny negativ")
    print("6. Odstiny sedi")
    print("7. Zesvetleni")
    print("8. Ztmaveni")
    print("9. Zvyrazneni hran")
    print("10. Ukonceni kodu")
    print("11. Napoveda")
    vyber = (input("Zvol si cislo a pak stiskni enter: "))
    print("\n")
    if vyber == '0' or vyber == '0.' or vyber == '0. Zobrazit original':
        img.show()
        menu()
    elif vyber == '1' or vyber == '1.' or vyber == '1. Prevraceni obrazu ve svisle ose':
        prevraceni_svisle()
        menu()
    elif vyber == '2' or vyber == '2.' or vyber == '2. Prevraceni obrazu ve vodorovne ose':
        prevraceni_vodorovne()
        menu()
    elif vyber == '3' or vyber == '3.' or vyber == '3. Rotace':
        rotace()
        menu()
    elif vyber == '4' or vyber == '4.' or vyber == '4. Negativ':
        negativ()
        menu()
    elif vyber == '5' or vyber == '5.' or vyber == '5. Prirozeny negativ':
        prirozenyNegativ()
        menu()
    elif vyber == '6' or vyber == '6.' or vyber == '6. Odstiny sedi':
        odstinySedi()
        menu()
    elif vyber == '7' or vyber == '7.' or vyber == '7. Zesvetleni':
        zesvetleni()
        menu()
    elif vyber == '8' or vyber == '7.' or vyber == '8. Ztmaveni':
        ztmaveni()
        menu()
    elif vyber == '9' or vyber == '9.' or vyber == '9. Zvyrazneni hran':
        hrany()
        menu()
    elif vyber == '10' or vyber == '10.' or vyber == '10. Ukonceni kodu':
        exit
    elif vyber == '11' or vyber == '11.' or vyber == '11. Napoveda':
        napoveda2()
    else:
        print("Nesprávný vstup, zkus znovu!")
        print("\n\n")
        menu()


def negativ():
    data_out = 255 - data
    img_out = Image.fromarray(data_out, 'RGB')
    img_out.save(soubor + '_negativ.jpg')
    img_out.show()

def odstinySedi():
    data_out = np.array([0.299, 0.587, 0.144]) * data
    data_out = data_out.sum(axis=2)
    img_out = Image.fromarray(np.asarray(data_out, dtype=np.uint8), 'L')
    img_out.save(soubor + '_sed.jpg')
    img_out.show()
def ztmaveni():
    data_out = data//2
    img_out = Image.fromarray(data_out, 'RGB')
    img_out.save(soubor + '_tmave.jpg')
    img_out.show()

def zesvetleni():
    data_out = np.where((255 - data) < 100, 255, data + 80)
    img_out = Image.fromarray(data_out, 'RGB')
    img_out.save(soubor + '_svetle.jpg')
    img_out.show()

def hrany():
    data_out = np.empty(shape=(data.shape[0], data.shape[1]))
    for index in np.ndindex(data.shape):
        if index[0] != 0 and index[1] != 0 and index[0] != data.shape[0] - 1 and index[1] != data.shape[1] - 1:
            vzorec = int(9 * (data[index[0], index[1]].sum()) - data[index[0] - 1, index[1] - 1].sum() - data[index[0] - 1, index[1]].sum() - data[index[0] - 1, index[1] + 1].sum() - data[index[0], index[1] - 1].sum() - data[index[0], index[1] + 1].sum() - data[index[0] + 1, index[1] - 1].sum() - data[index[0] + 1, index[1]].sum() - data[index[0] + 1, index[1] + 1].sum())
            a = vzorec - data[index[0], index[1]].sum()
            data_out[index[0], index[1]] = abs(a)
    img_out = Image.fromarray(np.asarray(data_out, dtype=np.uint8))
    img_out.save(soubor + '_hrany.jpg')
    img_out.show()


def rotace():
    a = int(input("O kolik 90° proti smeru hodinovych rucicek chces pretocit?: "))
    data_out = np.rot90(data, a)
    img_out = Image.fromarray(data_out, 'RGB')
    img_out.save(soubor + '_rotace.jpg')
    img_out.show()

def prirozenyNegativ():
    data_out = data[:, :, ::-1]
    img_out = Image.fromarray(data_out, 'RGB')
    img_out.save(soubor + '_prirozenaInverze.jpg')
    img_out.show()

def prevraceni_svisle():
    data_out = np.fliplr(data)
    img_out = Image.fromarray(data_out, 'RGB')
    img_out.save(soubor + '_prevraceni.jpg')
    img_out.show()

def prevraceni_vodorovne():
    data_out = data[::-1, :, :]
    img_out = Image.fromarray(data_out, 'RGB')
    img_out.save(soubor + '_cervena.jpg')
    img_out.show()

def nacteni():
    soubor = input("Napis nazev obrazku bez pripony a pak stiskni enter. Pro napovedu stiskni \"n\" a enter: ")
    print("\n")
    return soubor

def napoveda2():
    print("V pripade, ze vyberes 0, zobrazi se zkratka jen originalni obrazek.\n")
    print("V pripade 1 se obrazek zrcadli, jako by se dival do zrcadla.\n")
    print("V pripade 2 se obrazek obrati vzhuru nohama.\n")
    print("Pokud vyberes 3, obrazek bude rotovat vzdy o 90° proti smeru hodinovych rucicek. \n Budes vyzvan, abys vybral, kolikrat se rotace provede, pokud vyberes 4, budes mit zase puvodni obrazek.\n")
    print("V pripade 4 se invertuji vsechny barvy do opacne.\n")
    print("V pripade 5 se ctou barevne kanaly odzadu, kdo nezkusi, neuveri, vypada to hezky. :)\n")
    print("V pripade 6 se obrazek zmeni do cernobile verze.\n")
    print("Diky 7 se obrazek zesvetli na svetlejsi barvy.\n")
    print("Diky 8 se obrazek naopak ztmavi.\n")
    print("Pomoci 9 se zobrazi pouze hrany. Fotka nevypada tak hezky, nakresleny obrazek vypada krasne.\n Ale pozor, trpelivost, trva to opravdu dlouho!\n")
    print("V pripade 10 se ukonci program a okno se zavre.\n")
    print("\n")
    enter = input("Pro navrat zpet stiskni enter.\n")
    if enter == '':
        menu()
    else:
        print("Neumis stisknout jen enter? Sbohem.")
        sleep(5)
        exit()

print("\n")
soubor = nacteni()
if soubor == 'n':
    napoveda()
    soubor = nacteni()

if soubor == 'n':
    print("Nedelej ze me blazna, napovedu vidis o par radku nahoru!")
try:
    img = Image.open(soubor + '.jpg')
except FileNotFoundError as FNFE:
    print('Neplatny nebo neexistujici soubor:', FNFE)
    sleep(15)

data = np.asarray(img)

menu()