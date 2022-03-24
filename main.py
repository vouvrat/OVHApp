# -*- encoding: utf-8 -*-

import os
from welcome import welcome
from createMX.createmx import createmx
from deleteMX.deletemx import deletemx
from createEX.createex import createex
from deleteEX.deleteex import deleteex
from redirectMail.redirectmail import redirectMail

def main():
    while True:
        os.system("clear")
        print(welcome("OVHApp"))
        print("\nChoisissez le service que vous souhaitez utiliser : ")
        print("""
        1 : Créer une boite mail - MXPlan 
        2 : Supprimer une boite mail - MXPlan
        3 : Créer une boite mail - Exchange
        4 : Supprimer une boite mail - Exchange
        5 : Mettre en place une redirection
        0 : Exit"""
              )
        choice = input("\nEntrez votre choix : ")

        if choice == '1':
            createmx()
        elif choice == '2' :
            deletemx()
        elif choice == '3' :
            createex()
        elif choice == '4' :
            deleteex()
        elif choice == '5' :
            redirectMail()
        elif choice == '0':
            exit()
        os.system("clear")


if __name__ == "__main__":
    main()