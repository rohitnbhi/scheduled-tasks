##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import os
import pandas, datetime, random, smtplib
EMAIL= os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")

def send_mail(name, email):
    letter_lists =["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]
    letter_path =random.choice(letter_lists)
    print(email)
    with open(letter_path) as file:
        letter = file.read()
        mail_msg = letter.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=email, msg=f"Subject:Happy Birthday\n\n{mail_msg}")


data = pandas.read_csv("birthdays.csv")
now = datetime.datetime.now()
list = [send_mail(row["name"], row.email) for _, row in data.iterrows()
        if now.month ==row.month and now.day == row.day]

# [print(row.name, row.email) for row in data.iterrows()]
