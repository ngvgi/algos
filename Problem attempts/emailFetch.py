import imaplib
import email
from email.header import decode_header
import re

# account credentials
username = "ab18215520@kusccoagm.co.ke"
password = "hiltonagm2021??"


def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)


# create an IMAP4 class with SSL
imap = imaplib.IMAP4_SSL("kusccoagm.co.ke")
# authenticate
imap.login(username, password)

status, messages = imap.select(mailbox="INBOX.spam")
# number of top emails to fetch
N = 1
# total number of emails
messages = int(messages[0])
print(messages)

for i in range(messages, messages - N, -1):
    # fetch the email message by ID
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
            # decode the email subject
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                # if it's a bytes, decode to str
                subject = subject.decode(encoding)
            # decode email sender
            From, encoding = decode_header(msg.get("From"))[0]
            if isinstance(From, bytes):
                From = From.decode(encoding)
            print("Subject:", subject)
            print("From:", From)
            # if the email message is multipart
            # if msg.is_multipart():
            #     # iterate over email parts
            #     for part in msg.walk():
            #         # extract content type of email
            #         content_type = part.get_content_type()
            #         content_disposition = str(part.get("Content-Disposition"))
            #         try:
            #             # get the email body
            #             body = part.get_payload(decode=True).decode()
            #         except:
            #             pass
            #         if content_type == "text/plain" and "attachment" not in content_disposition:
            #             # print text/plain emails and skip attachments
            #             print(body)
            #         elif "attachment" in content_disposition:
            #             # download attachment
            #             filename = part.get_filename()
            #             if filename:
            #                 folder_name = clean(subject)
            #                 if not os.path.isdir(folder_name):
            #                     # make a folder for this email (named after the subject)
            #                     os.mkdir(folder_name)
            #                 filepath = os.path.join(folder_name, filename)
            #                 # download attachment and save it
            #                 open(filepath,
            #                      "wb").write(part.get_payload(decode=True))
            # else:
            # extract content type of email
            content_type = msg.get_content_type()
            # get the email body
            body = msg.get_payload(decode=True).decode()
            if content_type == "text/plain":
                # print only text email parts
                print(body)
            if content_type == "text/html":
                expression = re.compile(r'Password:\s{1}\w+', re.IGNORECASE)
                results = expression.search(body)
                if results:
                    password = results.group()
                    print(password[10:])

            print("_" * 50)
# close the connection and logout
imap.close()
imap.logout()
