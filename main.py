# -*- encoding: utf-8 -*-

import os
from welcome import welcome
from createMX.createmx import newmxmail
from deleteMX.deletemx import deletemx_mail
from createEX.createex import createex_mail
from deleteEX.deleteex import deleteex_mail
from redirectMail.redirectmail import redirectMail

def main():
    while True:
        os.system("clear")
        print(welcome("OVHApp"))
        print("\nChoisissez la fonction que vous souhaitez utiliser : ")
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
            newmxmail()
        elif choice == '2' :
            delmxmail()
        elif choice == '3' :
            newexmail()
        elif choice == '4' :
            delexmail()
        elif choice == '5' :
            redirectMail()
        elif choice == '0':
            exit()
        os.system("clear")


if __name__ == "__main__":
    main()