##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import smtplib
import pandas as pd

with open('./letter_templates/letter_1.txt') as letter:
    letter_0 = letter.readlines()
with open('./letter_templates/letter_2.txt') as letter:
    letter_1 = letter.readlines()
with open('./letter_templates/letter_3.txt') as letter:
    letter_2 = letter.readlines()
    # print(letter_1[0])


def letter_select(person):
    selection = random.randint(0, 2)
    if selection == 0:
        common = [sub.replace('[NAME]', f'{person}') for sub in letter_0]
        return common
    elif selection == 1:
        common = [sub.replace('[NAME]', f'{person}') for sub in letter_1]
        return common
    else:
        common = [sub.replace('[NAME]', f'{person}') for sub in letter_2]
        return common


def send(address, message):
    joined = ''.join(message)
    print(joined)
    with smtplib.SMTP('smtp.mail.yahoo.com', port=587) as connection:
        connection.starttls()
        connection.login(user='omar.python1@yahoo.com', password="nagwtkkjtefbonum")
        connection.sendmail(from_addr='omar.python1@yahoo.com', to_addrs=address,
                            msg=f"Subject: It's your Day!\n\n {joined}")


now = dt.datetime.now()
with open('birthdays.csv') as bdays:
    birthdays = pd.read_csv(bdays)
    birthdays_dict = birthdays.to_dict('records')
    print(birthdays_dict)
try:
    found = next(dictionary for dictionary in birthdays_dict if
                 dictionary['month'] == now.month and dictionary['day'] == now.day)
    email_recipient = found['email']
    name = found['name']
    send(email_recipient, letter_select(name))
except StopIteration:
    print('Birthday not found')

# if any(d['month'] == 12 for d in birthdays_dict) and any(a['day'] == 21 for a in birthdays_dict):
#     print(birthdays_dict[0])
# check = '2021-12-27'
# if now.day == 27 and now.month == 12:
#     print('True')


