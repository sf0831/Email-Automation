import smtplib
import email
import os
import logging
import schedule
import time

def send_automated_email():
    # creating ta smtplib object
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sender@gmail.com', 'password')

    sender = 'sender@gmail.com'
    recipient = ''
    person_number = 1
    # recipients list
    recipients = ['person1@gmail.com', 'person2@gmail.com', 'person3@gmail.com', 
                  'person4@gmail.com', 'person5@gmail.com', 'person6@gmail.com', 
                  'person7@gmail.com', 'person8@gmail.com', 'person9@gmail.com']

    # creating a text file to track the emails sent and the errors
    track_file = open("automation_log.txt", "w+")

    for recipient in recipients:
        # using the email library to create the body and header of the email
        message = email.message.Message()
        message['From'] = sender
        message['To'] = recipient
        message['Subject'] = 'Automatic replay - Your Daily Report'

        text = 'This is an automated email intended to show you the daily report. Check the text file in the attachement to download your report.'
        message.body = text

        # accessing the report file using os, and attaching using email library
        daily_report = f'report{person_number}.txt'

    try:
        with open(daily_report, 'rb') as f:
            #creating an attachement object
            attachement = email.message.Attachment()
            attachement.content = f.read()
            attachement.filename = os.path.basename(daily_report)
            message.attach(attachement)
    except:
        # adding the error to the log file
        if FileNotFoundError:
            logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.ERROR)
            logging.error("File has not been found.")


    finally:
        print('Cotinuing the sending process..')



    
    server.sendmail(sender, recipient, message.as_string())

    # logging the sent emails to a file
    logging.basicConfig(filename='automation_log.txt', filemode='w+', format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info(f"Email successfully sent to the custumer number {person_number} - Email: ({recipient}) ")


    
    # going to the next recipient, updating the person number by 1
    person_number += 1




    server.quit()


# Scheduling the emails to be sent every day at 11:00 am
schedule.every().day.at("11:00").do(send_automated_email)

# Creating a while loop so that the scheduled task keeps running all the time
while True:
    # Check if the scheduled task is pending to run or not
    schedule.run_pending()
    time.sleep(1)
