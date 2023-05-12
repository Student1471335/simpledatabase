Customer= """CREATE TABLE IF NOT EXISTS Customer (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    Surname TEXT,
    Postcode TEXT,
    HouseNumber INTEGER,
    PhoneNumber INTEGER

);"""

BouncyCastle= """CREATE TABLE IF NOT EXISTS BouncyCastle (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Size TEXT,
    MainColour TEXT,
    MaxOccupants INTEGER,
    HirePrice INTEGER

);"""

BookingInfo= """CREATE TABLE IF NOT EXISTS BookingInfo (
    CustomerID INTEGER,
    BouncyCastleID INTEGER,
    Bookingdate INTEGER,
    AdditionalNotes TEXT,
    FOREIGN KEY (CustomerID) REFERENCES Customer(ID) ON UPDATE RESTRICT ON DELETE RESTRICT,
    FOREIGN KEY (BouncyCastleID) REFERENCES BouncyCastle(ID) ON UPDATE RESTRICT ON DELETE RESTRICT

);"""