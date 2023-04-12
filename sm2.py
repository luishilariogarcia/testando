#!/usr/bin/env python3
from smartcard.System import *
from smartcard.util import *
r = readers()
connection = r[0].createConnection()
connection.connect()

print("Selecting ICCID File")
data, sw1, sw2 = connection.transmit(toBytes('00a40004022fe2'))
print("Returned data: " + str(data))
print("Returned Status Word 1: " + str(sw1))
print("Returned Status Word 2: " + str(sw2))