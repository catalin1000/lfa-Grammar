# This is a sample Python script.
import sys

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

global cuvant
ok=0
def function(litera_curent,dictionar,i):
    #print(litera_curent,i,len(cuvant))
    global ok
    if len(cuvant)==i:
        if 'lambda' in dictionar[litera_curent]:
            ok=1
    if i<len(cuvant):
        for tranzitie in dictionar[litera_curent]:
            if cuvant[i] == tranzitie[0]:
                function(tranzitie[1],dictionar,i+1)

def citire(file):
    
    dictionar = {}
    with open(file, "r") as f:
        for line in f:
            prop = line.strip().split("->")
            stari = prop[0].strip()
            dictionar[stari] = []
            tranzitii = prop[1].strip().split("|")

            for tranzitie in tranzitii:
                dictionar[stari].extend(tranzitie.split())

    return dictionar
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
dictionar = citire("input".strip())
print(dictionar)
cuvant=input("Introduceti cuvantul pentru verificat: ")


if not cuvant or cuvant=='lambda':
 
    if 'lambda' in dictionar['S']:
        print("cuvant acceptat")
    else:
        print("cuvant neacceptat")
else:
    litera_curent='S'
    function('S',dictionar,0)
    if ok==1:
        print('cuvant acceptat')
    else:
        print('cuvant neacceptat')



