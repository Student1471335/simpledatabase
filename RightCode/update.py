customeradd = ('''INSERT INTO customer
    (FirstName, Surname, Postcode, HouseNumber, PhoneNumber) 
   VALUES("Mike", "BillyBob", "BB9 7ED", 1234567789, 071456879)''')
bouncyadd= ('''INSERT INTO BouncyCastle
(Name, Size, MainColour, MaxOccupants, HirePrice)
 VALUES("BIgbounce", "BIG", "BLue", 12, 250)''')

Bookingadd = ('''INSERT INTO BookingInfo
(Bookingdate, AdditionalNotes)
 VALUES(010123, "leave in good condion")''')

customerdelete = '''DELETE from Customer WHERE 'ID'=2'''
updatecustomer = '''UPDATE Customer SET 'FirstName'='Mike',
'SurName'='BillyBob'
WHERE 'ID'=5'''