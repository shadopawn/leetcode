import names
import random
import time

def str_time_prop(start, end, format):

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + random.random() * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end):
    return str_time_prop(start, end, '%d-%m-%Y')

sqlfile = open("sqlInserts.txt","w+")

for i in range(30):
    
    ID = i

    genders = ["M", "F"]
    gender = random.choice(genders)

    nameGender = "male" if gender=="M" else "female"

    firstName = names.get_first_name(gender=nameGender)
    middleName = names.get_last_name()
    lastName = names.get_last_name()

    birthDay = random_date("1-1-1970", "1-1-2019")

    tableName = "USERS"
    print("INSERT INTO "+tableName)
    print("VALUES")
    sqlInsert = "(\'{}\', \'{}\', \'{}\', \'{}\', to_date(\'{}\', \'DD-MM-YYYY\'), \'{}\');"
    print(sqlInsert.format(ID, firstName, middleName, lastName, birthDay, gender))
    
    sqlfile.write("INSERT INTO "+tableName+"\n")
    sqlfile.write("VALUES\n")
    sqlfile.write(sqlInsert.format(ID, firstName, middleName, lastName, birthDay, gender)+"\n")

sqlfile.close()
