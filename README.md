
# Project Title

This project intends to automate the report sending process written in python. This project sends daily report to a list of customers at a specfic time each day, and also keeps a record of sent emails and erros. The libraries used in this project are (smtplib, email, os, logging, schedule, time).


### Configuration

1. Replace `'sender@gmail.com'` and `'password'` in the `server.login()` function with your Gmail credentials. Ensure that you allow less secure apps to access your Gmail account or use an App Password if you have two-factor authentication enabled.

2. Update the `recipients` list with the email addresses of the people you want to send the daily reports to.

3. Make sure you have the daily reports named as `report1.txt`, `report2.txt`, and so on, corresponding to each recipient.

### Sending the Emails

Once you have set up the configuration, the script will run daily at 11:00 AM and send the daily reports to each recipient. If a report for a recipient is not found, the script will log an error in the `automation_log.txt` file.

## Error Handling

This project also logs errors. If a report file is not found for a recipient, it logs the error in the `automation_log.txt` file.

## Logging

The script logs all the successfully sent emails and errors in the `automation_log.txt` file. The file is created in the working directory and is appended with new logs every time the script is run.

## Contribution

Although this is a small project, contributions to this project are welcome! If you find any issues or want to add new features, please feel free to create a pull request or open an issue, or message me.

## License

This project is licensed under the [MIT License](LICENSE).

## Schedule

The script is scheduled to run every day at 11:00 AM using the `schedule` library.

## Note

Please use this script responsibly and ensure you have the necessary permissions to send emails to the recipients.


