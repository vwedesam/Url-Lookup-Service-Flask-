#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

from app import db, Malwares

# setup url lookup service

malwares = []

# Creates all tables.
db.create_all()

# get all malwares from simple_malware.txt
with open('simple_malware.txt', 'r') as f:
    malwares = f.readlines()

# populate Malware table with url
for malware in malwares:
    url = Malwares(url=malware.replace('\n', ""))

    try:
        db.session.add(url)
        db.session.commit()
    except:
        print("unable to run url lookup service setup script")

print("done ...")

