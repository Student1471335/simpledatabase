import sqlite3
from tables import Customer
from tables import BouncyCastle
from tables import BookingInfo
from update import customeradd
from update import bouncyadd
from update import Bookingadd

connection = sqlite3.connect("bouncycastle.db")
cursor = connection.cursor()

cursor.execute(Customer)
cursor.execute(BouncyCastle)
cursor.execute(BookingInfo)
cursor.execute(customeradd)
cursor.execute(bouncyadd)
cursor.execute(Bookingadd)
connection.commit()
connection.close()