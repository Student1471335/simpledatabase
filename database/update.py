import sqlite3  
customeradd = cursor.execute('''INSERT INTO customer
    (FirstName, Surename, Postcode, HouseNumber, PhoneNumber) 
   VALUES(,"John", "Smith", "BB9 7ED", 1234567789, 071456879)''')
bouncyadd= cursor.execute('''INSERT INTO BouncyCastle
(Name, Size, MainColour, MaxOccupants, HirePrice)
 VALUES(,"BIgbounce", "BIG", "BLue", 12, 250)''')

Bookingadd = cursor.execute('''INSERT INTO BookingInfo
(Bookingdate, AdditionalNotes)
 VALUES(010123, "leave in good condion")''')
