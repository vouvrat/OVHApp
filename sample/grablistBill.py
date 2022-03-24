# -*- encoding: utf-8 -*-

import ovh

# create a client
client = ovh.Client()

# Grab bill list
bills = client.get('/me/bill')
for bill in bills:
    details = client.get('/me/bill/%s' % bill)
    print("%12s (%s): %10s --> %s" % (
        bill,
        details['date'],
        details['priceWithTax']['text'],
        details['pdfUrl'],
    ))