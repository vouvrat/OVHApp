# -*- encoding: utf-8 -*-
'''
First, install the latest release of Python wrapper: $ pip install ovh
'''
import json
import ovh
import csv

# Instanciate an OVH Client.
# You can generate new credentials with full access to your account on
# the token creation page
client = ovh.Client(
    endpoint='ovh-eu',               # Endpoint of API OVH Europe (List of available endpoints)
    application_key='xxxxxxxxxx',    # Application Key
    application_secret='xxxxxxxxxx', # Application Secret
    consumer_key='xxxxxxxxxx',       # Consumer Key
)

listmaillingList = []

listMailinglist = client.get('/email/domain/'.arrayDomainlist.'/mailingList', 
    #name=None, // Mailing list name (type: string)
)

result = client.get('/email/domain/vouvrat.com/mailingList/direct/subscriber', 
    email=None, // Subscriber email (type: string)
)


# Pretty print
print (json.dumps(result, indent=4))
