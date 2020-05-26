import re
import couchdb
import couchdb.design
import pandas as pd
from couchdb import Server


couch = couchdb.Server("http://admin:admin1234@172.26.129.166:5984/")
database = couch['instance3_new']
aurin = couch['aurin']
key_ms = []
key_syd = []

aurin_ms = []
aurin_syd = []

# Creating Views

#map = 'function (doc) { if( (doc.place.name=="Melbourne") && ((doc.lang=="ar") || (doc.lang=="de") || (doc.lang=="el") || (doc.lang=="it") || (doc.lang=="zh"))) {emit(doc.lang, doc.text);}}'
#view = couchdb.design.ViewDefinition('Languages', "Melbourne", map)
#view.sync(database)

#map = 'function(doc) {if ((doc.place.name == "Sydney") && ((doc.lang == "ar") || (doc.lang == "de") || (doc.lang == "el") || (doc.lang == "it") || (doc.lang == "zh"))) {emit(doc.lang, doc.text);}}'
#view = couchdb.design.ViewDefinition("Languages", "Sydney", map)
# view.sync(database)


# Aurin
#map = 'function (doc) {if(doc.city=="Melbourne") emit(doc.lang, doc.count);}'
#view = couchdb.design.ViewDefinition('Languages', "Melbourne", map)
# view.sync(database)

#map = 'function (doc) {if(doc.city=="Sydney") emit(doc.lang, doc.count);}'
#view = couchdb.design.ViewDefinition('Languages', "Sydney", map)
# view.sync(database)

for doc in database.view('Languages/Melbourne', reduce=True, group_level=1):
    key_ms.append(doc['key']),
    key_ms.append(doc['value'])

print("Melbourne Twitter data", key_ms)

for doc in database.view('Languages/Sydney', reduce=True, group_level=1):
    key_syd.append(doc['key'])
    key_syd.append(doc['value'])

print("Sydney Twitter data", key_syd)

for doc in aurin.view('Languages/Melbourne'):
    aurin_ms.append(doc['key'])
    aurin_ms.append(doc['value'])

print("Melbourne Aurin data", aurin_ms)

for doc in aurin.view('Languages/Sydney'):
    aurin_syd.append(doc['key'])
    aurin_syd.append(doc['value'])

print("Sydney Aurin data", aurin_syd)
