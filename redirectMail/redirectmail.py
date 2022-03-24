# -*- encoding: utf-8 -*-
'''
First, install the latest release of Python wrapper: $ pip install ovh
'''
import json
import ovh
from welcome import welcome


# Instanciate an OVH Client.
# You can generate new credentials with full access to your account on
# the token creation page
client = ovh.Client()

print(welcome("OVHApp - MXPlan"))

# Variable d'adresse mail
DOMAIN = input("Quel est le nom de domaine de travail? :")
SOURCE = input("Adresse mail source: ")
DESTINATION = input("Adresse mail de destination: ")

# Create a new alias
client.post('/email/domain/%s/redirection' % DOMAIN,
        _from=SOURCE,
        to=DESTINATION,
        localCopy=False
    )
print("Installed new mail redirection from %s to %s" % (SOURCE, DESTINATION))