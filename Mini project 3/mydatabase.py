import sqlite3

mydb = sqlite3.connect("usersdb.db")
myCursor = mydb.cursor()

# with open("face_images/user.jpg","rb") as f:
#     data = f.read()

# def InsertImg():
#     myCursor.execute(f'INSERT INTO Users(photo) VALUES {data}')

def Add(name,lastname,nationalcode,birthdate):
    myCursor.execute(f'INSERT INTO Users(Name, LastName, nationalCode, birthdate) VALUES("{name}","{lastname}","{nationalcode}","{birthdate}")')
    mydb.commit()
    
def Edit(name,lastname,nationalcode1,birthdate,id):
    myCursor.execute(f'UPDATE Users SET Name = "{name}" ,LastName = "{lastname}", nationalCode = "{nationalcode1}" ,birthdate = "{birthdate}" WHERE Id = "{id}"')
    mydb.commit()

def GetAll():
    myCursor.execute("SELECT * FROM Users")
    result = myCursor.fetchall()
    return result