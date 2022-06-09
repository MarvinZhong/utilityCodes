import win32com.client as win32
import win32api
from datetime import datetime
import os


def readFile(textPath):
    file = open(textPath, 'r')
    # read the file line by line save to listText
    listText = []
    for line in file:
        listText.append(line)
        # replace '\n' with '<br>'
        listText[-1] = listText[-1].replace('\n', '<br>')
    # print join the listText with '<br>'
    text = ''.join(listText)
    # print(listText)
    return text


def sendEmail():
    # Open the Outlook
    outlook = win32.Dispatch('outlook.application')
    # Create the email
    mail = outlook.CreateItem(0)
    # Set the email subject
    mail.Subject = 'Subject ' + str(date)
    # Set the receiver email
    mail.To = "emailTo@example.com"
    mail.CC = "emailCC@example.com"
    # Add an image or file    
    mail.Attachments.Add(os.path.join(os.getcwd(), filePath))

    # Set the email body
    text = readFile(textPath)
    # Write the email content
    mail.HTMLBody = r"""
    <h1>""" + str(date) + """</h1>
    <hr>
    """ + text + """
    """

    # Send the email
    mail.Send()
    print('The Email is sent.')


def main():
    # readFile(textPath)
    sendEmail()


if __name__ == '__main__':
    textPath = 'D:\\Code\\automation\\savedFile\\20220601.txt'
    # customizable file path 
    filePath = textPath 
    date = 20220601
    # date = datetime.now()
    main()
