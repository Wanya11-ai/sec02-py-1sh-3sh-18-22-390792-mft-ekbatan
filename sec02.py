#takilf1:


students = []

# ezafe kardan yek danesh amooz be list
text1="Ezafe kardan danesh amooz"
print(text1.center(20,"="))

name = input("Esm va familit chie? ")
username = input("Ye username entekhab kon: ")
password = input("Ye password bezan: ")
python = input("Nomre Python-et chand shode? ")
java = input("Nomre Java-et chand shode? ")
html = input("Nomre HTML-et chand shode? ")
sql = input("Nomre SQL-et chand shode? ")

if python.isdecimal() and java.isdecimal() and html.isdecimal() and sql.isdecimal():
    print("Nomreha dorost vared shodan")
else:
    print("Nomre bayad faghat adad bashe!")

student = [name, username, password, python, java, html, sql]

students.append(student)

print("Danesh amooz ba movafaghiat ezafe shod ")


# login
textt="login"
print(textt.center(20,"="))

user = input("Username-et ro bezan: ")
passw = input("Password-et ro bezan: ")

login = False

for student in students:
    if student[1] == user and student[2] == passw:
        print("Khosh oomadi", student[0], "!")
        print("Login ba movafaghiat anjam shod :)")
        login = True
        break

if login == False:
    print("Oops! Username ya password eshtebahe :(")


# sabtenam
text2="sabtenam"
print(text2.center(20,"="))

name = input("Esm va familit ro bezan: ")
username = input("Ye username baraye khodet entekhab kon: ")
password = input("Ye password baraye hesab bezan: ")

python = input("Nomre Python-et: ")
java = input("Nomre Java-et: ")
html = input("Nomre HTML-et: ")
sql = input("Nomre SQL-et: ")

new_student = [name, username, password, python, java, html, sql]

students.append(new_student)

print("Afarin! Sabetnamet ba movafaghiat anjam shod ")

print("\nDanesh amooz haye sabtenam shode:")
print(students)







#taklif2:

import random

people = []
texxt="be barname ghore keshi khosh omadid!"
print(texxt.center(20,"-="))
for i in range(5):
    namee = input("5 Esm ro baraye ghore keshibezan: ")
    people.append(namee)

winner = random.choice(people)

print(f"{winner} shoma barande shodid!")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

password = ""

for i in range(18):
    password += random.choice(chars)

print(f"Password pishnahadi ma be shoma: /nlotfan in pass ro hefz bashid ta badan betonid jayxe daryaft konid: {password}")
 