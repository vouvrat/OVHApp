# -*- encoding: utf-8 -*-
'''
First, install the latest release of Python wrapper: $ pip install ovh
'''
import json
from unittest import result
import ovh
import keyboard
import csv

# Instanciate an OVH Client.
# You can generate new credentials with full access to your account on
# the token creation page
client = ovh.Client()


#MAILINGLISTNAME = input("Nom de la liste à afficher: ")
#MAILADRESSOURCE = input("Adresse mail source: ")
#MAILADRESSDEST = input("Adresse mail de destination: ")


# Vérification de la présence du nom de domaine.
listDomain = client.get('/email/domain/'
    #whoisOwner=None, //List all domain list
)
DOMAIN = input("Nom de domaine du client: ")

if DOMAIN in listDomain:
    print(f"Le domaine est présent: ", DOMAIN)
else:
    print("Le domaine saisi n'existe pas. Vérifier la saisie.")

# Affiche les informations du domaine saisi précédement.
#infoDomain = client.get('/email/domain/%s/' % DOMAIN,
    #whoisOwner=None, //List all domain list
#)

# Affiche les listes de diffusions du domaine saisi précédement.
#mailingListDomain = client.get('/email/domain/%s/mailingList/' % DOMAIN,
#)

# Affiche les personnes étant inscrit dans la liste de diffusions choisie préalablement.
#mailingListSubscriber = client.get('/email/domain/%s/mailingList/%s/subscriber/' % (DOMAIN, MAILINGLISTNAME),
    #whoisOwner=None, //List all domain list
#)

# Create a new alias
#client.post('/email/domain/%s/redirection' % DOMAIN,
#        _from=MAILADRESSOURCE,
#        to=MAILADRESSDEST,
#        localCopy=False
#    )
#print("Ajout de la redirection %s vers %s" % (MAILADRESSOURCE, MAILADRESSDEST))


# Pretty print
#print (json.dumps(listDomain, indent=4))
# Pretty print
#print (json.dumps(infoDomain, indent=4))
# Pretty print
#print (json.dumps(mailingListDomain, indent=4))
# Pretty print
#print (json.dumps(mailingListSubscriber, indent=4))