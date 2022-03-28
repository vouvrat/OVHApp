# -*- encoding: utf-8 -*-
'''
First, install the latest release of Python wrapper: $ pip install ovh
'''
from decimal import Clamped
from welcome import welcome
import json
import ovh
import os

# Instanciate an OVH Client.
# You can generate new credentials with full access to your account on
# the token creation page
client = ovh.Client()

def newmxmail():
    os.system("clear")
    #print(welcome("Création de boite mail MX PLAN"))
    print("Création de boite mail Exchange")


    # Vérification de la présence du nom de domaine.
    listDomain = client.get('/email/domain/'
        #whoisOwner=None, //List all domain list
    )
    NDD = input("Nom de domaine du client: ")

    if NDD in listDomain:
        print(f"Le domaine est présent: {NDD}")
    else:
        print("Le domaine saisi n'existe pas. Vérifier la saisie.") 

    ADR = input("Adresse mail :")
    DSC = input("Description (Nom Prénom) :")
    PWD = input("Mot de passe :")

    client.post('/email/domain/{NDD}/account',   
    accountName={ADR},
    description={DSC},
    password={PWD},
    size=None,
    )
    
    print(f"création de la boite mail {ADR} sur le domaine {NDD} .")

newmxmail()